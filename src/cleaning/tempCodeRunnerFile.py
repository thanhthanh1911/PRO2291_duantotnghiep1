import pandas as pd

df = pd.read_csv("data/raw/sales_06_FY2020-21.csv")

clean_df = df.copy()

for col in clean_df.select_dtypes(include=['int64', 'float64']).columns:
    Q1 = clean_df[col].quantile(0.25)
    Q3 = clean_df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    clean_df = clean_df[
        (clean_df[col] >= lower_bound) &
        (clean_df[col] <= upper_bound)
    ]

print("Số dòng sau khi loại bỏ outlier:", len(clean_df))