#!/usr/bin/env python

import os
import re

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'Pipfile')) as pipfile:
    content = pipfile.read()
    REQUIREMENTS = re.findall(r'''\\n[ '"]*(\S*)[ '"]*=''', content.split('packages]')[1])
    PYTHON_VERSION = re.search(r'python_version = "([\d.]+)"', content)[1]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ndh',
    version='3.7.0',
    packages=['ndh'],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    license='BSD',
    description='Nim’s Django Helpers',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/nim65s/ndh',
    author='Guilhem Saurel',
    author_email='webmaster@saurel.me',
    python_requires=f'>={PYTHON_VERSION}',
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
