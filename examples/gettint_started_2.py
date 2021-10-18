import di
from pandas_datareader import wb

token = "{your_token}"

# Get data
humans = wb.download(indicator='SP.POP.TOTL', country=['CHN', 'US'], start=1970, end=2021)

# Put data
di.put("42di.cn/marvin/tutorials/humans", humans, token, update_schema=True)

# Get data
humans = di.read("42di.cn/marvin/tutorials/humans", token)

print(humans[humans['country'] == 'China'].head(10))