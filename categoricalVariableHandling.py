import pandas as pd

data = pd.read_csv('train.csv')
print(data.columns)
print(data.isnull().sum())
print(data.isnull().mean().sort_values(ascending=True))

# replace with mode if missing is not so much
# use Capturing Nan Value if to many missing values