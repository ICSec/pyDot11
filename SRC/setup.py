#!/usr/bin/env python
# Copyright (C) 2016 stryngs.

from setuptools import setup

setup(
    name = 'pyDot11',
    version = '1.1.5',
    author = 'stryngs',
    author_email = 'info@ethicalreporting.org',
    packages = ['pyDot11', 'pyDot11.lib'],
    include_package_data = True,
    url = 'https://github.com/ICSec/pyDot11',
    license ='GNU General Public License v2',
    keywords = '802.11 wep wpa encryption decryption on-the-fly',
    description='Encrypt and Decrypt 802.11(WEP or WPA) on-the-fly'
)
