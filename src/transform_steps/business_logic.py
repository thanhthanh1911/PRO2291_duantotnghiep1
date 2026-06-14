import pandas as pd


def standardize_order_status(df):
    """
    Chuẩn hóa trạng thái đơn hàng
    """
    df = df.copy()

    if "status" not in df.columns:
        return df

    df["status"] = (
        df["status"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    status_mapping = {
        "complete": "completed",
        "completed": "completed",
        "received": "received",
        "pending": "pending",
        "processing": "processing",
        "cancel": "cancelled",
        "cancelled": "cancelled",
        "canceled": "cancelled",
        "closed": "closed"
    }

    df["status"] = df["status"].replace(status_mapping)

    return df


def classify_customer_age(df):
    """
    Phân loại khách hàng theo độ tuổi
    """
    df = df.copy()

    if "age" not in df.columns:
        return df

    def age_group(age):

        if pd.isna(age):
            return "Unknown"

        if age < 18:
            return "Teen"

        elif age <= 25:
            return "Young Adult"

        elif age <= 40:
            return "Adult"

        elif age <= 60:
            return "Middle Age"

        else:
            return "Senior"

    df["customer_segment"] = df["age"].apply(age_group)

    return df


def classify_order_value(df):
    """
    Phân loại giá trị đơn hàng
    """
    df = df.copy()

    if "total" not in df.columns:
        return df

    def order_value(total):

        if pd.isna(total):
            return "Unknown"

        if total < 100:
            return "Low"

        elif total <= 500:
            return "Medium"

        else:
            return "High"

    df["order_value_group"] = df["total"].apply(order_value)

    return df


def classify_discount(df):
    """
    Phân loại mức giảm giá
    """
    df = df.copy()

    if "discount_percent" not in df.columns:
        return df

    def discount_group(discount):

        if pd.isna(discount):
            return "Unknown"

        if discount == 0:
            return "No Discount"

        elif discount <= 10:
            return "Low Discount"

        elif discount <= 30:
            return "Medium Discount"

        else:
            return "High Discount"

    df["discount_group"] = (
        df["discount_percent"] * 100
    ).apply(discount_group)

    return df


def classify_order_size(df):
    """
    Phân loại số lượng sản phẩm mua
    """
    df = df.copy()

    if "qty_ordered" not in df.columns:
        return df

    def order_size(qty):

        if pd.isna(qty):
            return "Unknown"

        if qty == 1:
            return "Single Purchase"

        elif qty <= 5:
            return "Small Order"

        else:
            return "Bulk Order"

    df["order_size"] = df["qty_ordered"].apply(order_size)

    return df


def classify_customer_type(df):
    """
    Phân loại khách hàng VIP
    """
    df = df.copy()

    if (
        "cust_id" not in df.columns
        or
        "total" not in df.columns
    ):
        return df

    customer_spending = (
        df.groupby("cust_id")["total"]
        .sum()
        .reset_index()
    )

    customer_spending["customer_type"] = (
        customer_spending["total"]
        .apply(
            lambda x:
            "VIP"
            if x >= 5000
            else "Regular"
        )
    )

    df = df.merge(
        customer_spending[
            ["cust_id", "customer_type"]
        ],
        on="cust_id",
        how="left"
    )

    return df


def detect_business_errors(df):
    """
    Phát hiện lỗi nghiệp vụ
    """
    df = df.copy()

    df["is_business_error"] = False

    if "total" in df.columns:
        df["is_business_error"] |= (
            df["total"] < 0
        )

    if "qty_ordered" in df.columns:
        df["is_business_error"] |= (
            df["qty_ordered"] <= 0
        )

    if "discount_percent" in df.columns:
        df["is_business_error"] |= (
            df["discount_percent"] > 1
        )

    return df


def apply_business_logic(df):
    """
    Pipeline Business Logic
    """

    print("\n" + "=" * 50)
    print("BUSINESS LOGIC PROCESSING")
    print("=" * 50)

    df = standardize_order_status(df)
    df = classify_customer_age(df)
    df = classify_order_value(df)
    df = classify_discount(df)
    df = classify_order_size(df)
    df = classify_customer_type(df)
    df = detect_business_errors(df)

    print("Business Logic hoàn tất.")

    return df

# Note cho nhóm trưởng nếu có lỗi thì thêm này dô
# Ở file "cleaner.py" thêm from cleaning.business_logic import apply_business_logic
# Sau câu lệnh df = handle_nulls(df) thêm df = apply_business_logic(df)

# Pipeline:
# Read CSV
# ↓
# Standardizer
# ↓
# Datatype
# ↓
# Null
# ↓
# Business Logic
# ↓
# Outlier
# ↓
# sales_cleaned.csv