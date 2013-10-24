#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    raise ImportError("Install setuptools: pip install setuptools")

"""
to test the setup script from terminal type:
pip uninstall pyfetcher && python setup.py install && python setup.py clean && pyfetcher
"""

setup(
    name='PyFetcher',
    version='0.0.1',
    description='Python media streaming url fetcher',
    author='Marc Webbie',
    author_email='marcwebbie@gmail.com',
    url='https://bitbucket.org/marcwebbie/pyfetcher/',
    packages=[
        'pyfetcher',
        'pyfetcher.crawlers'
    ],
    scripts=['bin/pyfetcher'],
    license='MIT',
    install_requires=[
        'lxml',
        'cssselect',
        'pyquery',
    ],
)
