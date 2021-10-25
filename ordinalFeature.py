import datetime as dt
import pandas as pd
today_date = dt.datetime.today()
print(today_date)
time_difference = today_date - dt.timedelta(20)
print(time_difference)

### list comprehension

### Ordinal Encoding
data = pd.DataFrame([today_date - dt.timedelta(i) for i in range(20)],columns=["Days Difference"])
data['week days']= data['Days Difference'].dt.day_name()
prinweekDaysDict = {
    'Monday':1,
    'Tuesday':2,
    'Wednesday':3,
    'Thursday':4,
    'Friday':5,
    'Saturday':6,
    'Sunday':7
}
data['ordinalWeekDays'] = data['week days'].map(prinweekDaysDict)
print(data)


## Count and Frequancy Encoding

## Count number of Each attribute in Colum and replace with that

## Easy to use
## Not increase the any feature space
##

# Disadvantage

## It will not handle the provide same weight



## Target Guided Ordinal Encoding Technique

## Ordering the label according to the target

## Replace the label by the joint probability of being 1 or 0

titanic_data = pd.read_csv('train.csv',usecols=['Cabin','Survived'])
titanic_data['Cabin'].fillna('Missing',inplace=True)
titanic_data['Cabin'] = titanic_data['Cabin'].astype(str).str[0]
print(titanic_data.Cabin.value_counts())
ordinalLabels = titanic_data.groupby(['Cabin'])['Survived'].mean().sort_values().index
orderinalLabel2 = {k:i for i,k in enumerate(ordinalLabels,0)}
titanic_data['Cabin_ordinal_labels'] = titanic_data['Cabin'].map(orderinalLabel2)
print(titanic_data)

# mean Encoding
meanOrdinal = titanic_data.groupby(['Cabin'])['Survived'].mean().to_dict()

# Probility ratio encoding

probaility = pd.read_csv('train.csv',usecols=['Cabin','Survived'])
p_data  = probaility.fillna('Missing',axis=1)
p_data['Cabin'] = p_data['Cabin'].astype(str).str[0]
print(p_data)
unique_data = p_data.Cabin.unique()
print(unique_data)

prob_df = p_data.groupby(['Cabin'])['Survived'].mean()
prob_df = pd.DataFrame(prob_df)
print(prob_df)

prob_df['Died'] = 1- prob_df['Survived']
print(prob_df.head(10))

prob_df['P_ratio'] = prob_df['Survived'] / prob_df['Died']
print(prob_df.head(4))


