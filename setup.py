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
    entry_points = """
        [ckan.plugins]
        datawagovau_theme = ckanext.datawagovautheme.plugins:CustomTheme
    """
)
