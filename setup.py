""" pyuci a python module to parse uci via json """

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
 long_description = f.read()

setup(
name='pyuci',
version='0.0',
description='module for parsing uci via json',
long_description=long_description,
url='https://github.com/hpfmn/pyuci',
author='Lynxis, Johannes "hpfmn" Wegener',
author_email='mail@johanneswegener.de',
classifiers=[
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'Programming Language :: Python :: 3.4'
],
keywords='uci openwrt',
packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
install_requires=[]
)
