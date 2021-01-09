import pandas as pd

df = pd.read_csv("sbi.csv")

print(df.head())
print(df.iloc[0:7,0:6])