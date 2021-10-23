# coding: utf-8

"""
    42di Python SDK

    No description provided
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "42di"
VERSION = "0.2.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="42di is the python sdk for 42di.com",
    author_email="support@42di.com",
    url="https://42di.com",
    keywords=["42DI", "42di Python SDK", "42di.com", "42di.cn"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""

    42di is the python sdk for 42di.com

    42di.com is a platform for data science.

    """
)
