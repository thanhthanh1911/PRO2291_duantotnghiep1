import pandas as pd
from pathlib import Path

CLEANED_PATH = Path("data/cleaned/sales_cleaned.csv")
OUTPUT_DIR = Path("data/dim_fact")

def transform_to_star_schema():
    df = pd.read_csv(CLEANED_PATH, low_memory=False)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dim_customer = df[[
        "cust_id", "gender", "age", "customer_since"
    ]].drop_duplicates().rename(columns={
        "cust_id": "customer_id"
    })

    dim_product = df[[
        "sku", "category", "price"
    ]].drop_duplicates().rename(columns={
        "sku": "product_id"
    })

    dim_location = df[[
        "city", "state", "region", "zip"
    ]].drop_duplicates().reset_index(drop=True)

    dim_location["location_id"] = dim_location.index + 1

    dim_time = df[["order_date"]].drop_duplicates()
    dim_time["date_id"] = dim_time["order_date"].dt.strftime("%Y%m%d")
    dim_time["day"] = dim_time["order_date"].dt.day
    dim_time["month"] = dim_time["order_date"].dt.month
    dim_time["quarter"] = dim_time["order_date"].dt.quarter
    dim_time["year"] = dim_time["order_date"].dt.year

    fact_sales = df.merge(
        dim_location,
        on=["city", "state", "region", "zip"],
        how="left"
    )

    fact_sales["date_id"] = fact_sales["order_date"].dt.strftime("%Y%m%d")

    fact_sales = fact_sales[[
        "order_id",
        "cust_id",
        "sku",
        "location_id",
        "date_id",
        "qty_ordered",
        "price",
        "discount_amount",
        "discount_percent",
        "total",
        "status",
        "payment_method"
    ]].rename(columns={
        "cust_id": "customer_id",
        "sku": "product_id",
        "total": "revenue"
    })

    dim_customer.to_csv(OUTPUT_DIR / "dim_customer.csv", index=False)
    dim_product.to_csv(OUTPUT_DIR / "dim_product.csv", index=False)
    dim_location.to_csv(OUTPUT_DIR / "dim_location.csv", index=False)
    dim_time.to_csv(OUTPUT_DIR / "dim_time.csv", index=False)
    fact_sales.to_csv(OUTPUT_DIR / "fact_sales.csv", index=False)

    print("Star Schema created successfully.")

if __name__ == "__main__":
    transform_to_star_schema()



    






    import pandas as pd
from pathlib import Path

CLEANED_PATH = Path("data/cleaned/sales_cleaned.csv")
OUTPUT_DIR = Path("data/dim_fact")

def transform_to_star_schema():
    df = pd.read_csv(CLEANED_PATH, low_memory=False)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dim_customer = df[[
        "cust_id", "gender", "age", "customer_since"
    ]].drop_duplicates().rename(columns={
        "cust_id": "customer_id"
    })

    dim_product = df[[
        "sku", "category", "price"
    ]].drop_duplicates().rename(columns={
        "sku": "product_id"
    })

    dim_location = df[[
        "city", "state", "region", "zip"
    ]].drop_duplicates().reset_index(drop=True)

    dim_location["location_id"] = dim_location.index + 1

    dim_time = df[["order_date"]].drop_duplicates()
    dim_time["date_id"] = dim_time["order_date"].dt.strftime("%Y%m%d")
    dim_time["day"] = dim_time["order_date"].dt.day
    dim_time["month"] = dim_time["order_date"].dt.month
    dim_time["quarter"] = dim_time["order_date"].dt.quarter
    dim_time["year"] = dim_time["order_date"].dt.year

    fact_sales = df.merge(
        dim_location,
        on=["city", "state", "region", "zip"],
        how="left"
    )

    fact_sales["date_id"] = fact_sales["order_date"].dt.strftime("%Y%m%d")

    fact_sales = fact_sales[[
        "order_id",
        "cust_id",
        "sku",
        "location_id",
        "date_id",
        "qty_ordered",
        "price",
        "discount_amount",
        "discount_percent",
        "total",
        "status",
        "payment_method"
    ]].rename(columns={
        "cust_id": "customer_id",
        "sku": "product_id",
        "total": "revenue"
    })

    dim_customer.to_csv(OUTPUT_DIR / "dim_customer.csv", index=False)
    dim_product.to_csv(OUTPUT_DIR / "dim_product.csv", index=False)
    dim_location.to_csv(OUTPUT_DIR / "dim_location.csv", index=False)
    dim_time.to_csv(OUTPUT_DIR / "dim_time.csv", index=False)
    fact_sales.to_csv(OUTPUT_DIR / "fact_sales.csv", index=False)

    print("Star Schema created successfully.")

if __name__ == "__main__":
    transform_to_star_schema()



    