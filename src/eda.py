import pandas as pd
#khám phá 
df = pd.read_csv("data/raw/sales_06_FY2020-21.csv")

print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())