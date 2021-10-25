import pandas as pd
import numpy as np

# why is data Missing

df = pd.read_csv('train.csv')
print(df.head())
print(df.isnull().sum())
print(df[df['Embarked'].isnull()])

df['Cabin_null'] = np.where(df['Cabin'].isnull(), 1, 0)

# find the percentage of null value in column
print(df['Cabin_null'].mean())

# Handling Missing Value

# Mean Median Mode Imputation
# When should we Apply it

df2 = pd.read_csv('train.csv', usecols=['Age', 'Fare', 'Survived'])
print(df2.isnull().mean())


def impute_nan(df, variable, median):
    df[variable + '_median'] = df[variable].fillna(median)


median = df.Age.median

impute_nan(df, 'Age', median)

# Disadvantages of Mean and median imputation
# Impact on Corelation
# overfitting and underfitting in dataset


# Random Sampling Imputation
# Take a random observation to fill the NaN value

data = pd.read_csv('train.csv', usecols=['Age', 'Fare', 'Survived'])
print(data.isnull().mean())

# picking up any random value
print(data['Age'].sample(data['Age'].isnull().sum(), random_state=0))

# Some time random is not work


## Capturing Nan Values with a new Features
## is used when missing value is not random It may have some relationship with other values

# Disadvantage is lead to curse of dimensionality


## End of Distibution imputation

# Get the value away from 3rd standard deviation in normal distribution
# This technique also handle the outlier
print(data.Age.mean() + 3 * data.Age.std())


## Arbitrary Value Imputation

def impute(df,variable):
    df[variable+'_hundred'] = df[variable].fillna(0)
    #It should not be more frequantly present in dataset

