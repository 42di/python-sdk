# 42di Python SDK 

### Install

```bash

pip install 42di

```

OR

```bash
pip install git+https://github.com/42di/python-sdk
```

### Put to / read from 42di

```python
import di #42di

import pandas_datareader as pdr

di.TOKEN = "<YOUR_ACCESS_TOKEN>"

df = pdr.get_data_fred('GDP')


di.put("42di.cn/shellc/testing/my_dataset", df, create=True, update_schema=True)

df = di.read("42di.cn/shellc/testing/my_dataset")

print(df.head(100))
```