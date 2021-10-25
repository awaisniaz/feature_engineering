import pandas as pd
# One Hot Encoding
df = pd.read_csv('train.csv',usecols=["Sex"])
print(df)
print(pd.get_dummies(df,drop_first=True))
