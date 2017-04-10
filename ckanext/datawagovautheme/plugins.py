
from ckan.plugins import (toolkit, IConfigurer, SingletonPlugin,
                          ITemplateHelpers, implements)
import datetime


def get_current_year():
    return datetime.datetime.today().year


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
