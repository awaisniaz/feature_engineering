import pandas as pd
dataframe = pd.DataFrame()
data = pd.date_range('1/1/2021',periods=30,freq='H')
dataframe['Dates'] = data
# print(dataframe)


url = 'http://bit.ly/uforeports'
df = pd.read_csv(url)
print(df.head(5))
df['Time'] = pd.to_datetime(df.Time)

print(df.head(2))
print(df.dtypes)
print(df.Time.dt.hour.head())

import pandas as pd
ts = pd.Timestamp(year = 2011,month = 11,day = 21,hour = 10,second = 49,tz = 'US/Central')
print(ts)