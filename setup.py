#!/usr/bin/env python
#
# Setup script for the Artificial Intelligence Toolkit
#
# Copyright (C) 2018 AITK Project
# Author: Daohan Chong <d.chong@aitk.ai>
# For license information, see LICENSE

# Versioning code from NLTK, Apache License, Version 2.0:
# Use the VERSION file to get the version
import os
from setuptools import setup, find_packages

version_file = os.path.join(os.path.dirname(__file__), 'aitk', 'VERSION')
with open(version_file) as fh:
    aitk_version = fh.read().strip()

with open('requirements.txt') as f:
    required = f.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name="aitk",
    description="Artificial Intelligence Toolkit",
    version=aitk_version,
    url="https://aitk.ai/",
    long_description=long_description,
    keywords=['NLP', 'CL', 'natural language processing',
              'CV', 'computer vision', 'face recognition',
                'speech to text', 'text to speech', 'translation', 'chatbot',
                'OCR', 'optical character recognition', 'artificial intelligence', ],
    maintainer="Daohan Chong",
    maintainer_email="daohanchong@gmail.com",
    author="Daohan Chong",
    author_email="d.chong@aitk.ai",
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    package_data={'aitk': ['test/*.doctest', 'VERSION']},
    install_requires=required,
    # extras_require=extras_require,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    # TODO: Add CLI tools
    # entry_points={
    #     'console_scripts': ['aitk = aitk.cli:main']
    # },
    include_package_data=True,
)
