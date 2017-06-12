#!/usr/bin/env python
#
# This file is a standalone package intended to be used on a variety of different projects.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# https://github.com/ecaldwe1/file-type-converters

import os

from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "vecnet", "openmalaria", "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name="file-type-converters",
    version=about["VERSION"],
    author="E. Caldwell for University of Notre Dame",
    author_email="ecaldwe1@nd.edu",
    description="File Conversion Library",
    license="Mozilla Public License 2.0 (MPL 2.0)",
    keywords="filetype yaml json",
    url="https://github.com/ecaldwe1/file-type-converters",
    # find_packages() takes a source directory and two lists of package name patterns to exclude and include.
    # If omitted, the source directory defaults to the same directory as the setup script.
    packages=find_packages(),  # https://pythonhosted.org/setuptools/setuptools.html#using-find-packages
    #namespace_packages=['file-type-converters', ],
    scripts=['scripts/om_expand.cmd', 'scripts/om_expand'],
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
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)