#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='steam-swissapiknife',
    version='0.1',
    description='A tool to explore the Steam API.',
    url='https://github.com/Lagg/steam-swissapiknife',
    author='Lagg',
    author_email='lagg@lagg.me',
    license='ISC',
    packages=['steamswissapiknife'],
    test_suite='nose.collector',
    tests_require=['nose'],
    keywords=['Steam', 'WebAPI'],
    classifiers = [
          "License :: OSI Approved :: ISC License (ISCL)",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
          ],
    entry_points={
        'console_scripts': [
            'steamswissapiknife = steamswissapiknife.main:main',
        ],
    },
        )