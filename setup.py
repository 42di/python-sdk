# coding: utf-8

"""
    42di Python SDK

    No description provided
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "42di"
VERSION = "0.2.6"
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
    long_description_content_type="text/markdown",
    long_description="""
# 42di Python SDK

**42di is the python sdk for 42di.com**

**42di.com is a platform for data science.**


## Install

```bash

pip install 42di

```

OR

```bash
pip install git+https://github.com/42di/python-sdk
```

## Put to / read from 42di

```python
import di #42di

import pandas_datareader as pdr

di.TOKEN = "<YOUR_ACCESS_TOKEN>"

df = pdr.get_data_fred('GDP')


di.put("42di.cn/shellc/testing/my_dataset", df, create=True, update_schema=True)

df = di.read("42di.cn/shellc/testing/my_dataset")

print(df.head(100))
```
    """
)
