import pandas as pd


def convert_datatypes(df):
    """
    Chuyển đổi kiểu dữ liệu cho DataFrame.
    """

    df = df.copy()

    print("\n" + "=" * 50)
    print("DATA TYPE CONVERSION")
    print("=" * 50)


    date_cols = [
        "order_date",
        "customer_since"
    ]

    for col in date_cols:

        if col in df.columns:

            df[col] = pd.to_datetime(
                df[col],
                dayfirst=True,
                errors="coerce"
            )

            print(f"[✔] Converted {col} → datetime")

    # ------------------
    # Chuyển cột số
    # ------------------

    numeric_cols = [

        "age",

        "qty_ordered",
        "price",
        "value",
        "discount_amount",
        "discount_percent",
        "total",

        "cust_id",
        "item_id",
        "year",
        "ref_num",
        "zip"

    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

            print(f"[✔] Converted {col} → numeric")

    print("[✔] Data type conversion completed.")

    return df