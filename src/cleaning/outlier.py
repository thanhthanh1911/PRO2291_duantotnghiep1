import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("data/raw/sales_06_FY2020-21.csv")

# Chọn các cột số
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("=== OUTLIER REPORT ===\n")

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[col] < lower_bound) |
        (df[col] > upper_bound)
    ]

    print(f"Column: {col}")
    print(f"Lower Bound: {lower_bound:.2f}")
    print(f"Upper Bound: {upper_bound:.2f}")
    print(f"Number of Outliers: {len(outliers)}")
    print(f"Outliers:\n{outliers[[col]]}\n")