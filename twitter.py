import csv
import pandas as pd

df = pd.read_csv('twitter.csv')

df.dtypes

df['statsdate'] = pd.to_datetime(df['statsdate'], format= "%m/%d/%Y")

with open("pandastwitter.csv", "w") as f:
    df.to_csv(f, index=False, header=True)

