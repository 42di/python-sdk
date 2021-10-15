# 42di Python SDK 

### Install

```bash
pip install git+https://github.com/42di/python-sdk
```

### import

```python
import di #42di

import pandas_datareader as pdr
```

### Init SDK

```python
project = di.Project("42di.cn/<YOUR_USER_ID>/<YOUR_PROJECT_ID>", "<YOUR_ACCESS_TOKEN>")
```

### Create table

```python
table = project.table("us_gdp")

if not table.exists():
    table.create()

table.update("title", "US GDP")
```

### Upload data

```python
df = pdr.get_data_fred('GDP')

# Update table schema
table.update_schema(di.schema(df))

table.put_csv(df)
```

### Read data

```python
df = t.read()

print(df)
```