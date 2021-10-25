import pandas as pd
ts = pd.Timestamp(year = 2000,month = 11,day = 21,hour = 10,second = 47,tz = 'US/CENTRAL')
print(ts)
print(ts.now())
print(ts.isoformat())