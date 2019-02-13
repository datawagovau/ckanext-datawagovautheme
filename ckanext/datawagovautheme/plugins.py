import datetime
from collections import OrderedDict

from ckan.common import c, _
import ckan.lib.helpers as h
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from markupsafe import Markup

import ckanext.scheming.helpers as sh


def get_current_year():
    return datetime.datetime.today().year


def wa_license_icon(id):
    icons = {
        'cc-by': ['cc', 'cc-by'],
        'cc-nc': ['cc', 'cc-by', 'cc-nc'],
        'cc-by-sa': ['cc', 'cc-by', 'cc-sa'],
        'cc-zero': ['cc', 'cc-zero'],
    }
    if id not in icons:
        return ''
    # return h.url_for_static('license-{}.png'.format(id))
    return Markup(
        ''.join(
            '<img width=20 src="{}">'.
            format(h.url_for_static('{}.png'.format(icon)))
            for icon in icons[id]
        )
    )


def datawa_scheming_select_options(field_name):
    schema = sh.scheming_get_dataset_schema('dataset')
    try:
        access_level_options = sh.scheming_field_by_name(
            schema['dataset_fields'], field_name)['choices']
        options = {i['value']: i['label'] for i in access_level_options}
    except Exception as e:
        raise e
    return options


def datawa_get_option_label(options, option):
    if option in options:
        option_label = options[option]
        return option_label
    return option


def access_level_text(access_level):
    access_level_text = {
        'open': "This dataset is available for use by everyone",
        'open_login': "This dataset is available for use by everyone - login required",
        'fees_apply': "This dataset is available for use subject to payment",
        'restricted': "This dataset is available for use subject to approval",
        'govt_only': "This dataset is available for government use only",
        'mixed': "A variety of access levels apply to this dataset's resources"
    }
    if access_level in access_level_text:
        return access_level_text[access_level]
    return ''


def license_data(pkg):
    license_id = ''
    license_icon= ''
    license_title = ''
    license_url = ''
    license_specified = True

    if 'license_id' in pkg and pkg['license_id']:
        license_id = pkg['license_id']
        license_title = pkg['license_title']
        if license_id.startswith('custom'):
            license_icon = 'custom'
            if 'custom_license_url' in pkg and pkg['custom_license_url']:
                license_url = pkg['custom_license_url']
            else:
                license_title = 'Custom licence not supplied'
                license_specified = False
        else:
            license_icon = license_id
            if 'license_url' in pkg:
                license_url = pkg['license_url']
    else:
        license_id = 'not_specified'
        license_icon = 'not_specified'
        license_title = 'Licence not supplied'
        license_specified = False


    license_data = {
        'license_id' : license_id,
        'license_icon': license_icon,
        'license_title': license_title,
        'license_url': license_url,
        'license_specified': license_specified
    }

    return license_data


class CustomTheme(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IFacets, inherit=True)

    # IPackageController

    def before_search(self, search_params):
        # fix for ckanext-hierarchy required by migration to 2.8
        try:
            c.fields
        except AttributeError:
            c.fields = []
        return search_params

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "static")
        toolkit.add_resource('fanstatic', 'datawagovautheme')

    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator('ignore_missing')
        schema.update({
            'ckanext.datawa.slip_harvester_token': [ignore_missing, unicode],
        })

        return schema

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'get_current_year': get_current_year,
            'wa_license_icon': wa_license_icon,
            'access_level_text': access_level_text,
            'license_data': license_data,
            'datawa_scheming_select_options': datawa_scheming_select_options,
            'datawa_get_option_label': datawa_get_option_label
        }

    # Ifacets
    def dataset_facets(self, facets_dict, package_type):
        ## Updating Formats position
        fct_keys = [key for key in facets_dict.keys()]
        res_fmt = fct_keys.pop(fct_keys.index('res_format')) if 'res_format' in fct_keys else None
        org_fct_index = fct_keys.index('organization') if 'organization' in fct_keys else None
        if res_fmt and org_fct_index is not None:
            fct_keys.insert(org_fct_index + 1, res_fmt)
            updated_facet_dict = OrderedDict([(key,facets_dict[key]) for key in fct_keys])
            facets_dict = updated_facet_dict

        facets_dict['access_level'] = _('Access Level')
        return facets_dict
