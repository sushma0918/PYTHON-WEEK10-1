import pandas as pd
df = pd.read_csv("data.csv")
# Inspect data
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())