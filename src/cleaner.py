import pandas as pd
from pathlib import Path

from cleaning.null import handle_nulls
from cleaning.outlier import detect_outliers
from cleaning.standardizer import standardize_data
from cleaning.datatype import convert_datatypes

RAW_PATH = Path("data/raw/sales_06_FY2020-21.csv")
CLEANED_PATH = Path("data/cleaned/sales_cleaned.csv")
OUTLIER_PATH = Path("data/cleaned/outliers.csv")

def clean_data():
    print("=" * 50)
    print("START DATA CLEANING")
    print("=" * 50)

    df = pd.read_csv(RAW_PATH, low_memory=False)

    print("Original shape:", df.shape)

    # 1. Chuẩn hóa tên cột, text, category
    df = standardize_data(df)

    # 2. Chuẩn hóa kiểu dữ liệu
    df = convert_datatypes(df)

    # 3. Kiểm tra và xử lý null
    df = handle_nulls(df)

    # 4. Xóa duplicate
    duplicate_count = df.duplicated().sum()
    print("Duplicate rows:", duplicate_count)
    df = df.drop_duplicates()

    # 5. Phát hiện outlier
    outliers = detect_outliers(df)

    OUTLIER_PATH.parent.mkdir(parents=True, exist_ok=True)
    outliers.to_csv(OUTLIER_PATH, index=False)

    print("Outliers saved:", OUTLIER_PATH)
    print("Outlier rows:", len(outliers))

    # 6. Lưu dữ liệu sạch
    CLEANED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEANED_PATH, index=False)

    print("Cleaning completed:", df.shape)

    return df

if __name__ == "__main__":
    clean_data()