#!/usr/bin/env python

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="pyTSP",
    version="0.0.4",
    description="A simple and module TSP solver",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Behnam Lal",
    author_email='dev@behnamlal.xyz',
    url="https://github.com/CheesyChocolate/TSP",
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent"
        ],
    python_requires='>=3.6',
    install_requires=[
        'scipy',
        'matplotlib',
                 ],
)
