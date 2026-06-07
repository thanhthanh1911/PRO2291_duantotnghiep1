import pandas as pd
from pathlib import Path

from cleaning.standardizer import standardize_data
from cleaning.datatype import convert_datatypes
from cleaning.null import handle_nulls
from cleaning.outlier import detect_outliers, flag_outliers

RAW_PATH = Path("data/raw/sales_06_FY2020-21.csv")
CLEANED_PATH = Path("data/cleaned/sales_cleaned.csv")
OUTLIER_PATH = Path("data/cleaned/outliers.csv")


def clean_data():
    print("=" * 60)
    print("START DATA CLEANING")
    print("=" * 60)

    df = pd.read_csv(
        RAW_PATH,
        low_memory=False
    )

    print("Original shape:", df.shape)

    df = standardize_data(df)

    df = convert_datatypes(df)

    df = handle_nulls(df)

    duplicate_count = df.duplicated().sum()
    print("Duplicate rows:", duplicate_count)

    df = df.drop_duplicates()

    outliers = detect_outliers(df)

    OUTLIER_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    outliers.to_csv(
        OUTLIER_PATH,
        index=False,
        encoding="utf-8-sig"
    )

    df = flag_outliers(df)

    CLEANED_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        CLEANED_PATH,
        index=False,
        encoding="utf-8-sig"
    )

    print("Outliers saved:", OUTLIER_PATH)
    print("Outlier rows:", len(outliers))
    print("Cleaning completed:", df.shape)

    return df


if __name__ == "__main__":
    clean_data()