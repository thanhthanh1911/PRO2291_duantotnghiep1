import re
import unicodedata
import pandas as pd


def standardize_columns(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(".", "_", regex=False)
        .str.replace("/", "_", regex=False)
    )

    return df


def clean_text(value):
    if pd.isna(value):
        return value

    value = str(value)
    value = unicodedata.normalize("NFC", value)
    value = re.sub(r"\s+", " ", value).strip()

    return value


def standardize_data(df):
    df = df.copy()

    df = standardize_columns(df)

    text_cols = [
        "status",
        "sku",
        "category",
        "payment_method",
        "bi_st",
        "region",
        "city",
        "state",
        "county",
        "user_name",
        "place_name",
    ]

    for col in text_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype("string")
                .apply(clean_text)
                .str.lower()
            )

    name_cols = [
        "first_name",
        "last_name",
        "full_name",
        "place_name",
        "city",
        "county",
        "state",
        "region",
    ]

    for col in name_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype("string")
                .apply(clean_text)
                .str.title()
            )

    if "gender" in df.columns:
        df["gender"] = (
            df["gender"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        df["gender"] = df["gender"].replace({
            "m": "male",
            "male": "male",
            "f": "female",
            "female": "female",
        })

        df.loc[
            ~df["gender"].isin(["male", "female"]),
            "gender"
        ] = "unknown"

    if "e_mail" in df.columns:
        df["e_mail"] = (
            df["e_mail"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    if "phone_no_" in df.columns:
        df["phone_no_"] = (
            df["phone_no_"]
            .astype("string")
            .str.replace(r"\D", "", regex=True)
        )

    print("Tiêu chuẩn hóa hoàn tất.")

    return df