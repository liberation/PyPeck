# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="PyPeck",
    version='0.1',
    author='Libération',
    author_email='devweb@liberation.fr',
    licence='GNU GPL v2',
    packages=[
        'pypeck',
        'pypeck.scrapper',
    ],
    long_description=open('README').read(),
    install_requires=[
        'BeautifulSoup==3.2',
        'html5lib<=1.0',
        'pyconst==1.0',
        'tweepy==3.5'
    ],
)
