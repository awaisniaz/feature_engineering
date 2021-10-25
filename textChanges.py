import pandas  as pd
data = {'Name':['Awqaus Biaz','Usman Niaz']}
df = pd.DataFrame(data)
df['Name'] = df['Name'].str.upper()
print(df)