import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/sales_06_FY2020-21.csv")
CLEANED_PATH = Path("data/cleaned/sales_cleaned.csv")

def clean_data():
    df = pd.read_csv(RAW_PATH, low_memory=False)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(".", "_")
    )

    df = df.drop_duplicates()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    df = df.dropna(subset=["order_id", "order_date", "total"])

    df["order_id"] = df["order_id"].astype(str)
    df["cust_id"] = df["cust_id"].astype(str)
    df["sku"] = df["sku"].astype(str)

    CLEANED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEANED_PATH, index=False)

    print("Cleaning completed:", df.shape)

if __name__ == "__main__":
    clean_data()

    