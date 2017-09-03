#/usr/bin/env python

# Setup OVERWATCH
# Derived from the setup.py in aliBuild
#  and based on: https://python-packaging.readthedocs.io/en/latest/index.html

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="aziz_light",
    version="0.1",

    description="Control Limitless LED lights",
    long_description=long_description,

    author="Raymond Ehlers",
    author_email="raymond.ehlers@gmail.com",

    url="https://github.com/raymondEhlers/azizLight",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7'
    ],

    # What does your project relate to?
    keywords='LED',

    packages=find_packages(exclude=(".git")),

    # Rename scripts to the desired executable names
    # See: https://stackoverflow.com/a/8506532
    entry_points = {
        "console_scripts" : [
            # Note that the flask apss only run the flask development server through these scripts
            # because they will be launched directly via uwsgi (ie not through these scripts)
            "azizLight = azizLight.run:runDevelopment"
        ],
    },

    # This is usually the minimal set of the required packages.
    # Packages should be installed via pip -r requirements.txt !
    install_requires=[
        "flask",
        "flask_restful",
        "limitlessled",
        "pyyaml",
        "ruamel.yaml"
    ],

    # Include additional files
    include_package_data=True
  )
