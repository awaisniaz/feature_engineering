import pandas as pd
import numpy as np

data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}

df = pd.DataFrame(data1)
for Name,group in df.groupby('Name'):
    print(Name)
    print(group)
    
groupData = df.groupby('Name')
print(groupData.get_group('Princi'))

#  Applying Single Function on data set
print(groupData.aggregate(np.sum))

#  Applying Multiple data from Single Dat frame

grp = df.groupby('Name')
grp['Age'].agg([np.sum,np.mean,np.std])

grp.agg({
    'Age':'sum',
    'Score':'std'
})

