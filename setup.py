#!/usr/bin/env python

import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.in')) as requirements:
    REQUIREMENTS = [req.split('#egg=')[1] if '#egg=' in req else req for req in requirements.readlines()]


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ndh',
    version='3.0.0',
    packages=['ndh'],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    license='BSD',
    description='Nim’s Django Helpers',
    long_description=README,
    url='https://github.com/nim65s/ndh',
    author='Guilhem Saurel',
    author_email='webmaster@saurel.me',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
