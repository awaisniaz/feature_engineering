# Count and Frequency Encoding for Handling Categorical Features
import pandas as pd
import numpy as np

data = pd.read_csv('mercedesbenz.csv',usecols=['X1','X2'])

data2 = pd.get_dummies(data).shape
col = data.columns
for X in col:
    print(X, ':',len(data[X].unique()),'labels')


# Converted into Dictionary
data_frequancy = data.X2.value_counts().to_dict()
data.X2 = data.X2.map(data_frequancy)