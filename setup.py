#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    raise ImportError("Install setuptools: pip install setuptools")


def readme():
    with open('README') as f:
        return f.read()

setup(
    name='PyFetcher',
    version='0.0.1',
    description='Python media streaming url fetcher',
    long_description=readme(),
    author='Marc Webbie',
    author_email='marcwebbie@gmail.com',
    url='https://bitbucket.org/marcwebbie/pyfetcher/',
    packages=['pyfetcher'],
    scripts=['bin/pyfetcher'],
    license='MIT',
    install_requires=[
        'PyQuery',
    ],
)
