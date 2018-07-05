# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    tech_license = f.read()

setup(
    name='py_techinterview',
    version='1.0',
    description='Tech interview work',
    long_description=readme,
    author='val09072010',
    author_email='val09072010@gmail.com',
    url='https://github.com/val09072010/py_techinterview',
    license=tech_license,
    packages=find_packages(exclude=('tests', 'docs'))
)
