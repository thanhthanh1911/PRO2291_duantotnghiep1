import pandas as pd

def convert_datatypes(df):
    # Chuyển ngày tháng
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(
            df["order_date"],
            dayfirst=True,
            errors="coerce"
        )

    if "customer_since" in df.columns:
        df["customer_since"] = pd.to_datetime(
            df["customer_since"],
            dayfirst=True,
            errors="coerce"
        )

    # Chuyển các cột số
    numeric_cols = [
        "age",
        "price",
        "quantity",
        "discount",
        "profit",
        "total"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df