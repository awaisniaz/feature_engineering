import pandas as pd
import numpy as np

# why is data Missing

df = pd.read_csv('train.csv')
print(df.head())
print(df.isnull().sum())
print(df[df['Embarked'].isnull()])

df['Cabin_null'] = np.where(df['Cabin'].isnull(),1,0)

# find the percentage of null value in column
print(df['Cabin_null'].mean())

# Handling Missing Value

# Mean Median Mode Imputation
# When should we Apply it

df2 = pd.read_csv('train.csv',usecols=['Age','Fare','Survived'])
print(df2.isnull().mean())

def impute_nan(df,variable,median):
    df[variable+'_median'] = df[variable].fillna(median)


median = df.Age.median

impute_nan(df,'Age',median)

# Disadvantages of Mean and median imputation
# Impact on Corelation
# overfitting and underfitting in dataset




# Random Sampling Imputation
