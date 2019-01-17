import datetime

from ckan.common import c
import ckan.lib.helpers as h
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from markupsafe import Markup


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


class CustomTheme(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IPackageController, inherit=True)

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
            'wa_license_icon': wa_license_icon
        }
