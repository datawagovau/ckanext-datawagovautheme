#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-datawagovautheme',
    version='2.0.2',
    description='',
    license='AGPL3',
    author='data.wa.gov.au team',
    author_email='florian.mayer@dpaw.wa.gov.au',
    url='http://govhack2015.readthedocs.org/',
    namespace_packages=['ckanext'],
    packages=['ckanext.datawagovautheme'],
    zip_safe=False,
    include_package_data=True,
    package_dir={'ckanext.datawagovautheme': 'ckanext/datawagovautheme'},
    package_data={'ckanext.datawagovautheme': ['*.json', 'fanstatic/*.js', 'fanstatic/styles/*.css', 'fanstatic/styles/*.scss', 'templates/*.html', 'templates/*/*.html',
                                               'templates/*/*/*.html', 'static/datacats/*.png', 'static/fonts/arial/*.eot', 'static/fonts/arial/*.svg', 'static/fonts/arial/*.woff', 'static/fonts/arial/*.woff2', 'static/fonts/arial/*.ttf', 'static/*.png', 'static/*.ico']},

    entry_points="""
        [ckan.plugins]
        datawagovau_theme = ckanext.datawagovautheme.plugins:CustomTheme
        [paste.paster_command]
        wa = ckanext.datawagovautheme.command:WaCommand

    """
)
