import pandas as pd

df = pd.read_csv("data/raw/sales_06_FY2020-21.csv")

print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())