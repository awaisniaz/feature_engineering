import pandas as pd

# dictionary of lists
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

df = pd.DataFrame(dict, index=[0,1,2,3,])
address = ['dehli','Bangalore','Chennai','Patna']
df['address'] = address
print(df)
date_data = pd.date_range("2021,01,01 8:45",periods=100,freq='Y')
after_truncate = pd.truncate()
print(date_data)
df.insert(2,'Age',[3,4,5,6])
print(df)