
from ckan.plugins import (toolkit, IConfigurer, SingletonPlugin,
                          ITemplateHelpers, implements, IPackageController)
import datetime
from ckan.common import _, c
from ckan.model.license import LicenseRegister, DefaultLicense


class CustomLicense(DefaultLicense):
    id = "custom_license"
    is_generic = True

    @property
    def title(self):
        return _("Custom License (See attached resource)")


def get_current_year():
    return datetime.datetime.today().year


original_licenses = LicenseRegister._create_license_list


def updated_licenses(self, license_data, license_url=''):
    if isinstance(license_data, list):
        license_data.append(CustomLicense())
    original_licenses(self, license_data, license_url)


LicenseRegister._create_license_list = updated_licenses


class CustomTheme(SingletonPlugin):
    implements(IConfigurer)
    implements(ITemplateHelpers)
    implements(IPackageController, inherit=True)

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
            'get_current_year': get_current_year
        }
