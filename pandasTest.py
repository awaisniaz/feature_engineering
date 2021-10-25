import pandas as pd

# example dataframe
example = {'Team': ['Arsenal', 'Manchester United', 'Arsenal',
                    'Arsenal', 'Chelsea', 'Manchester United',
                    'Manchester United', 'Chelsea', 'Chelsea', 'Chelsea'],

           'Player': ['Ozil', 'Pogba', 'Lucas', 'Aubameyang',
                      'Hazard', 'Mata', 'Lukaku', 'Morata',
                      'Giroud', 'Kante'],

           'Goals': [5, 3, 6, 4, 9, 2, 0, 5, 2, 3]}

df = pd.DataFrame(example)
totalGoals = df['Goals'].groupby(df['Team'])
print(totalGoals.mean())
