#!/usr/bin/env python

"""UWUM (Unified WeGovNow User Management) provider for django-allauth."""

from os import path
from setuptools import setup, find_packages


name = 'django-allauth-uwum'
version = __import__('allauth_uwum').__version__
repository = path.join('https://github.com/ExCiteS', name)

setup(
    name=name,
    version=version,
    description='UWUM provider for django-allauth',
    url=repository,
    download_url=path.join(repository, 'tarball', version),
    author='Julius Osokinas',
    author_email='j.osokinas@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*']),
    include_package_data=True,
    install_requires=['django-allauth >= 0.27.0'],
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
    ],
)
