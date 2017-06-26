#!/usr/bin/env python
#
# This file is a standalone package intended to be used on a variety of different projects.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# https://github.com/ecaldwe1/file-type-converters
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

setup(
    name="file-type-converters",
    version="0.0.4",
    author="E. Caldwell",
    author_email="ecaldwe1@nd.edu",
    description="File conversion library to translate YAML into JSON and vice versa",
    license="Mozilla Public License 2.0 (MPL 2.0)",
    keywords="filetype yaml json",
    url="https://github.com/ecaldwe1/file-type-converters",
    # find_packages() takes a source directory and two lists of package name patterns to exclude and include.
    # If omitted, the source directory defaults to the same directory as the setup script.
    packages=find_packages(),  # https://pythonhosted.org/setuptools/setuptools.html#using-find-packages
    scripts=['converters/json2yaml.py', 'converters/yaml2json.py'],
    install_requires=[
        'pyYAML'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
)
