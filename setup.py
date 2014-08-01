# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages

# The following approach to retrieve the version number is inspired by this
# comment:
#
#   https://github.com/zestsoftware/zest.releaser/issues/37#issuecomment-14496733
#
# With this approach, development installs always show the right version number
# and do not require a reinstall (as the definition of the verdion umber in
# this setup file would).

version = 'no version defined'
current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, "skempy", "__init__.py")) as f:
    rx = re.compile("__version__ = '(.*)'")
    for line in f:
        m = rx.match(line)
        if m:
            version = m.group(1)

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='skempy',
    version=version,
    description='Provides functionality to support Python development in Emacs',
    long_description=readme,
    author='P.C.J. Swinkels',
    author_email='swinkels.pieter@yahoo.com',
    # url='home page of the project',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'skempy-find-test=skempy.find_path:main',
        ],
    },
)
