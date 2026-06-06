import pandas as pd
import numpy as np


# XỬ LÝ TRÙNG LẶP
def xu_ly_trung_lap(bang_du_lieu):

    so_dong_truoc = len(bang_du_lieu)

    bang_du_lieu = bang_du_lieu.drop_duplicates()

    so_dong_sau = len(bang_du_lieu)

    so_dong_da_xoa = (
        so_dong_truoc - so_dong_sau
    )

    print(
        f"[✔] Xử lý trùng lặp: "
        f"đã xóa {so_dong_da_xoa:,} dòng"
    )

    return bang_du_lieu


# XỬ LÝ GIÁ TRỊ THIẾU (NULL)
def xu_ly_gia_tri_thieu(bang_du_lieu):

    danh_sach_cot_quan_trong = [
        'order_id',
        'order_date',
        'total',
        'cust_id',
        'sku'
    ]

    so_dong_truoc = len(
        bang_du_lieu
    )

    bang_du_lieu = bang_du_lieu.dropna(
        subset=danh_sach_cot_quan_trong
    )

    so_dong_da_xoa = (
        so_dong_truoc -
        len(bang_du_lieu)
    )

    if so_dong_da_xoa > 0:
        print(
            f"[✔] Xóa "
            f"{so_dong_da_xoa:,} dòng "
            f"thiếu dữ liệu"
        )

    danh_sach_cot_so = (
        bang_du_lieu
        .select_dtypes(
            include=[np.number]
        )
        .columns
        .tolist()
    )

    danh_sach_cot_so = [
        cot
        for cot in danh_sach_cot_so
        if cot not in danh_sach_cot_quan_trong
    ]

    for ten_cot in danh_sach_cot_so:

        so_gia_tri_null = (
            bang_du_lieu[ten_cot]
            .isnull()
            .sum()
        )

        if so_gia_tri_null > 0:

            gia_tri_trung_vi = (
                bang_du_lieu[ten_cot]
                .median()
            )

            bang_du_lieu[
                ten_cot
            ] = bang_du_lieu[
                ten_cot
            ].fillna(
                gia_tri_trung_vi
            )

    danh_sach_cot_chuoi = (
        bang_du_lieu
        .select_dtypes(
            include=[
                'object',
                'string'
            ]
        )
        .columns
        .tolist()
    )

    danh_sach_cot_chuoi = [
        cot
        for cot in danh_sach_cot_chuoi
        if cot not in danh_sach_cot_quan_trong
    ]

    for ten_cot in danh_sach_cot_chuoi:

        so_gia_tri_null = (
            bang_du_lieu[ten_cot]
            .isnull()
            .sum()
        )

        if so_gia_tri_null > 0:

            bang_du_lieu[
                ten_cot
            ] = bang_du_lieu[
                ten_cot
            ].fillna(
                'Unknown'
            )

    tong_null_con_lai = (
        bang_du_lieu
        .isnull()
        .sum()
        .sum()
    )

    print(
        f"[✔] Null còn lại: "
        f"{tong_null_con_lai}"
    )

    return bang_du_lieu

def handle_nulls(df):
    df = xu_ly_gia_tri_thieu(df)
    return df