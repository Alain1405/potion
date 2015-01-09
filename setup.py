# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup

setup(
    name='Flask-Potion',
    version='0.1.0',
    packages=['flask_potion'],
    url='http://potion.readthedocs.org/en/latest/',
    license='MIT',
    author='Lars Schöning',
    author_email='lays@biosustain.dtu.dk',
    description='REST API framework for Flask and SQLAlchemy',
    test_suite='nose.collector',
    tests_require=[
        'Flask-Testing>=0.4.1',
        'Flask-Principal',
        'nose>=1.1.2',
    ],
    install_requires=[
        'Flask>=0.10',
        'Flask-SQLAlchemy>=2.0',
        'jsonschema>=2.4.0',
        'iso8601>=0.1.8',
        'blinker>=1.3',
        'six>=1.8.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
    extras_require={
        'docs': ['sphinx', 'Flask-Principal'],
        'principal': [
            'Flask-Principal',
        ]
    }
)
