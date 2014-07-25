# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='skempy',
    version='0.0.1',
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
