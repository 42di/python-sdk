import di
from pandas_datareader import wb

project = di.Project("42di.cn/Marvin/tutorials", "{your_token}")

table = project.table("humans")

if not table.exists():
    table.create()
    table.update("title", "Humans")

df = wb.download(indicator='SP.POP.TOTL', country=['CHN', 'US'], start=1970, end=2021)

table.update_schema(di.schema(df))
table.put_parquet(df)

df = table.read()

print(df)
