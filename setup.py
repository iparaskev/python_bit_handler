#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = []

test_requirements = []

setup(
    author="Iasonas Paraskevopoulos",
    author_email='iaswnparaskev@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A small python module for handling bits in registers with "
                "hardware interfaces communication libraries.",
    entry_points={
        'console_scripts': [
            'python_bit_handler=python_bit_handler.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n',
    include_package_data=True,
    keywords='python_bit_handler',
    name='python_bit_handler',
    packages=find_packages(include=['python_bit_handler']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/iparaskev/python_bit_handler',
    version='0.1.0',
    zip_safe=False,
)
