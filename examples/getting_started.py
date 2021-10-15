import di
import pandas_datareader as pdr

p = di.Project("42di.cn/<YOUR_USER_ID>/<YOUR_PROJECT_ID>", "<YOUR_ACCESS_TOKEN>")

t = p.table("us_gdp")

if not t.exists():
    t.create()

t.update("title", "US GDP")

df = pdr.get_data_fred('GDP')

t.update_schema(di.schema(df))
t.put_csv(df)

df = t.read()

print(df)
