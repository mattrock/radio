# -*- coding: utf-8 -*-
#quickstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       None
#
#

#This is just a work-around for a Python2.7 issue causing
#interpreter crash at exit when trying to log an info message.
try:
    import logging
    import multiprocessing
except:
    pass

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

testpkgs=['WebTest >= 1.2.3',
               'nose',
               'coverage',
               'wsgiref',
               ]
install_requires=[
    "TurboGears2 >= 2.2.2",
    "Genshi",
    "zope.sqlalchemy >= 0.4",
    "repoze.tm2 >= 1.0a5",
    "sqlalchemy<0.8b1",
    "sqlalchemy-migrate",
    "repoze.who",
    "repoze.who-friendlyform >= 1.0.4",
    "tgext.admin >= 0.5.1",
    "repoze.who.plugins.sa",
    "tw2.forms",
    ]

setup(
    name='radio',
    version='0.1',
    description='Radio Stream Server',
    author='Matt Rockwell',
    author_email='matt.rockwell@gmail.com',
    url='http://mattrock.net',
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2', 'tg.devtools'],
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'radio': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 'public/*/*']},
    message_extractors={'radio': [
            ('**.py', 'python', None),
            ('templates/**.html', 'genshi', None),
            ('public/**', 'ignore', None)]},

    entry_points="""
    [paste.app_factory]
    main = radio.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
    dependency_links=[
        "http://tg.gy/222"
        ],
    zip_safe=False
)
