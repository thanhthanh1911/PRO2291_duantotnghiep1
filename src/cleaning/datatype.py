import pandas as pd


def convert_datatypes(df):
    df = df.copy()

    print("\n" + "=" * 50)
    print("CHUYỂN ĐỔI KIỂU DỮ LIỆU")
    print("=" * 50)

    date_cols = [
        "order_date",
        "customer_since"
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col].astype(str).str.strip(),
                errors="coerce",
                format="mixed"
            )

            print(f"Đã chuyển đổi {col} → datetime")
            print(f"Null sau convert {col}: {df[col].isnull().sum():,}")

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

            print(f"Đã chuyển đổi {col} → numeric")

    print("Chuyển đổi kiểu dữ liệu đã hoàn tất.")

    return df