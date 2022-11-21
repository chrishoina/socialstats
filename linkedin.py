import csv
import pandas as pd

df = pd.read_csv('linkedinconnections.csv')

df['Connected On'] = pd.to_datetime(df['Connected On'], format= "%d %b %Y")
df = df.rename(columns={"Connected On": "connectdate", "First Name": "firstname", "Last Name": "lastname", "Email Address": "email", "Company": "company", "Position": "position"})

df.columns
with open("pandaslinkedinconnections.csv", "w") as f:
    df.to_csv(f, index=False, header=True)

