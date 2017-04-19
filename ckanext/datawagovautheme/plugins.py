
from ckan.plugins import (toolkit, IConfigurer, SingletonPlugin,
                          ITemplateHelpers, implements)
import datetime
from ckan.common import _
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

    def update_config(self, config):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "static")
        toolkit.add_resource('fanstatic', 'datawagovautheme')

    def get_helpers(self):
        return {
            'get_current_year': get_current_year
        }
