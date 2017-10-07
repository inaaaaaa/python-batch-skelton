# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-batch-skelton',
    version='0.1.0',
    description='Batch application skelton',
    long_description=readme,
    author='inaaaaaa',
    author_email='inaba1115@gmail.com',
    url='https://github.com/inaaaaaa/python-batch-skelton',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
