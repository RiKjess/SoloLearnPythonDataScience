"""
You continue working with the COVID dataset for California.
Now, add the weekday names for each row as a new column, named 'weekday'.
Then, output the last 7 days data of the dataset.
Do not set any index on the DataFrame.
"""

import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")

df['weekday'] = pd.to_datetime(df['date'], format="%d.%m.%y").dt.strftime("%A")

print(df.iloc[-7:])
