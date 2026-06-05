import pandas as pd
import numpy as np



# HÀM ĐỌC DỮ LIỆU
def doc_du_lieu(duong_dan_file):
    """
    Đọc file CSV vào DataFrame.

    Tham số:
        duong_dan_file: Đường dẫn đến file CSV cần đọc.

    Trả về:
        bang_du_lieu: DataFrame gốc chưa xử lý.
    """
    bang_du_lieu = pd.read_csv(duong_dan_file, low_memory=False)
    print(f"[✔] Đã đọc file: {duong_dan_file}")
    print(f"    → Số dòng: {len(bang_du_lieu):,} | Số cột: {len(bang_du_lieu.columns)}")
    return bang_du_lieu


# XỬ LÝ TRÙNG LẶP
def xu_ly_trung_lap(bang_du_lieu):
    """
    Xóa các dòng bị trùng lặp hoàn toàn trong DataFrame.

    Tham số:
        bang_du_lieu: DataFrame đầu vào.

    Trả về:
        bang_du_lieu: DataFrame sau khi loại bỏ dòng trùng lặp.
    """
    so_dong_truoc = len(bang_du_lieu)
    bang_du_lieu = bang_du_lieu.drop_duplicates()
    so_dong_sau = len(bang_du_lieu)
    so_dong_da_xoa = so_dong_truoc - so_dong_sau
    print(f"[✔] Xử lý trùng lặp: đã xóa {so_dong_da_xoa:,} dòng ({so_dong_da_xoa / so_dong_truoc * 100:.1f}%)")
    return bang_du_lieu


# XỬ LÝ GIÁ TRỊ THIẾU (NULL)
def xu_ly_gia_tri_thieu(bang_du_lieu):
    """
    Xử lý các giá trị null theo từng loại cột:
      - Cột quan trọng (order_id, order_date, total, cust_id) → xóa cả dòng nếu null.
      - Cột số (int/float) → điền bằng giá trị trung vị (median).
      - Cột chuỗi (object/string) → điền bằng 'Unknown'.

    Tham số:
        bang_du_lieu: DataFrame đầu vào.

    Trả về:
        bang_du_lieu: DataFrame sau khi xử lý giá trị thiếu.
    """
    # Cột quan trọng: nếu null thì xóa cả dòng
    danh_sach_cot_quan_trong = ['order_id', 'order_date', 'total', 'cust_id']
    so_dong_truoc = len(bang_du_lieu)
    bang_du_lieu = bang_du_lieu.dropna(subset=danh_sach_cot_quan_trong)
    so_dong_da_xoa = so_dong_truoc - len(bang_du_lieu)
    if so_dong_da_xoa > 0:
        print(f"[✔] Xóa {so_dong_da_xoa:,} dòng thiếu dữ liệu ở cột quan trọng: {danh_sach_cot_quan_trong}")

    # Cột số: điền median
    danh_sach_cot_so = bang_du_lieu.select_dtypes(include=[np.number]).columns.tolist()
    danh_sach_cot_so = [cot for cot in danh_sach_cot_so if cot not in danh_sach_cot_quan_trong]
    for ten_cot in danh_sach_cot_so:
        so_gia_tri_null = bang_du_lieu[ten_cot].isnull().sum()
        if so_gia_tri_null > 0:
            gia_tri_trung_vi = bang_du_lieu[ten_cot].median()
            bang_du_lieu[ten_cot] = bang_du_lieu[ten_cot].fillna(gia_tri_trung_vi)
            print(f"    [số]  '{ten_cot}': điền {so_gia_tri_null:,} giá trị null → trung vị = {gia_tri_trung_vi}")

    # Cột chuỗi: điền 'Unknown'
    danh_sach_cot_chuoi = bang_du_lieu.select_dtypes(include=['object', 'string']).columns.tolist()
    danh_sach_cot_chuoi = [cot for cot in danh_sach_cot_chuoi if cot not in danh_sach_cot_quan_trong]
    for ten_cot in danh_sach_cot_chuoi:
        so_gia_tri_null = bang_du_lieu[ten_cot].isnull().sum()
        if so_gia_tri_null > 0:
            bang_du_lieu[ten_cot] = bang_du_lieu[ten_cot].fillna('Unknown')
            print(f"    [str] '{ten_cot}': điền {so_gia_tri_null:,} giá trị null → 'Unknown'")

    tong_null_con_lai = bang_du_lieu.isnull().sum().sum()
    print(f"[✔] Xử lý giá trị thiếu hoàn tất. Null còn lại: {tong_null_con_lai}")
    return bang_du_lieu


# XỬ LÝ LỖI ĐỊNH DẠNG
def xu_ly_loi_dinh_dang(bang_du_lieu):
    """
    Sửa các lỗi định dạng phổ biến trong dữ liệu:
      - order_date, Customer Since  → chuyển sang kiểu ngày tháng (datetime).
      - Cột số (price, value, total) → đảm bảo không có giá trị âm.
      - Cột chuỗi (status, Gender)  → chuẩn hóa chữ hoa/thường, bỏ khoảng trắng.
      - Phone No.                   → chỉ giữ lại chữ số và dấu '-'.
      - E Mail                      → chuyển thành chữ thường.
      - Cột tên người, địa danh     → viết hoa chữ cái đầu mỗi từ.

    Tham số:
        bang_du_lieu: DataFrame đầu vào.

    Trả về:
        bang_du_lieu: DataFrame sau khi sửa lỗi định dạng.
    """

    # 1. Cột ngày tháng
    danh_sach_cot_ngay = ['order_date', 'Customer Since']
    for ten_cot in danh_sach_cot_ngay:
        if ten_cot in bang_du_lieu.columns:
            bang_du_lieu[ten_cot] = pd.to_datetime(bang_du_lieu[ten_cot], errors='coerce')
            so_gia_tri_sai = bang_du_lieu[ten_cot].isnull().sum()
            print(f"[✔] '{ten_cot}': chuyển sang kiểu ngày tháng ({so_gia_tri_sai:,} giá trị không hợp lệ → NaT)")

    # 2. Cột số: loại bỏ giá trị âm không hợp lệ
    danh_sach_cot_khong_am = ['price', 'value', 'total', 'qty_ordered', 'discount_amount', 'Discount_Percent']
    for ten_cot in danh_sach_cot_khong_am:
        if ten_cot in bang_du_lieu.columns:
            so_gia_tri_am = (bang_du_lieu[ten_cot] < 0).sum()
            if so_gia_tri_am > 0:
                bang_du_lieu[ten_cot] = bang_du_lieu[ten_cot].clip(lower=0)
                print(f"[✔] '{ten_cot}': đặt {so_gia_tri_am:,} giá trị âm về 0")

    # 3. Cột chuỗi: chuẩn hóa chữ hoa/thường và bỏ khoảng trắng
    danh_sach_cot_chuan_hoa = ['status', 'category', 'payment_method', 'bi_st', 'Region', 'Gender']
    for ten_cot in danh_sach_cot_chuan_hoa:
        if ten_cot in bang_du_lieu.columns:
            bang_du_lieu[ten_cot] = bang_du_lieu[ten_cot].astype(str).str.strip().str.lower()

    # Chuẩn hóa riêng cột giới tính: chỉ giữ 'm' / 'f' / 'unknown'
    if 'Gender' in bang_du_lieu.columns:
        bang_du_lieu['Gender'] = bang_du_lieu['Gender'].map(
            lambda gia_tri: gia_tri if gia_tri in ('m', 'f') else 'unknown'
        )
        print("[✔] 'Gender': chuẩn hóa thành 'm' / 'f' / 'unknown'")

    # 4. Email: chuyển thành chữ thường, bỏ khoảng trắng ---
    if 'E Mail' in bang_du_lieu.columns:
        bang_du_lieu['E Mail'] = bang_du_lieu['E Mail'].astype(str).str.strip().str.lower()
        print("[✔] 'E Mail': chuẩn hóa chữ thường và bỏ khoảng trắng")

    # 5. Số điện thoại: chỉ giữ chữ số và dấu gạch ngang ---
    if 'Phone No. ' in bang_du_lieu.columns:
        bang_du_lieu['Phone No. '] = (
            bang_du_lieu['Phone No. ']
            .astype(str)
            .str.replace(r'[^\d\-]', '', regex=True)
            .str.strip()
        )
        print("[✔] 'Phone No.': đã chuẩn hóa, chỉ giữ chữ số và dấu '-'")

    # 6. Tên người và địa danh: viết hoa chữ cái đầu, bỏ khoảng trắng thừa ---
    danh_sach_cot_ten = ['First Name', 'Last Name', 'full_name', 'Place Name', 'City', 'County']
    for ten_cot in danh_sach_cot_ten:
        if ten_cot in bang_du_lieu.columns:
            bang_du_lieu[ten_cot] = bang_du_lieu[ten_cot].astype(str).str.strip().str.title()

    print("[✔] Xử lý lỗi định dạng hoàn tất.")
    return bang_du_lieu


# LƯU KẾT QUẢ
def luu_du_lieu_sach(bang_du_lieu, duong_dan_luu):
    """
    Lưu DataFrame đã làm sạch ra file CSV.

    Tham số:
        bang_du_lieu:   DataFrame đã được xử lý.
        duong_dan_luu:  Đường dẫn file CSV đầu ra.
    """
    bang_du_lieu.to_csv(duong_dan_luu, index=False, encoding='utf-8-sig')
    print(f"[✔] Đã lưu file sạch: {duong_dan_luu}")
    print(f"    → Số dòng còn lại: {len(bang_du_lieu):,}")


# HÀM CHÍNH – QUY TRÌNH LÀM SẠCH
def quy_trinh_lam_sach(duong_dan_file_goc, duong_dan_file_sach):
    """
    Quy trình hoàn chỉnh: đọc → xử lý trùng lặp → xử lý null → sửa định dạng → lưu.

    Tham số:
        duong_dan_file_goc:  Đường dẫn file CSV gốc.
        duong_dan_file_sach: Đường dẫn file CSV sau khi làm sạch.

    Trả về:
        bang_du_lieu_sach: DataFrame đã làm sạch.
    """
    print("=" * 60)
    print("  BẮT ĐẦU QUY TRÌNH LÀM SẠCH DỮ LIỆU")
    print("=" * 60)

    bang_du_lieu_sach = doc_du_lieu(duong_dan_file_goc)

    print("\n--- BƯỚC 1: XỬ LÝ TRÙNG LẶP ---")
    bang_du_lieu_sach = xu_ly_trung_lap(bang_du_lieu_sach)

    print("\n--- BƯỚC 2: XỬ LÝ GIÁ TRỊ THIẾU (NULL) ---")
    bang_du_lieu_sach = xu_ly_gia_tri_thieu(bang_du_lieu_sach)

    print("\n--- BƯỚC 3: SỬA LỖI ĐỊNH DẠNG ---")
    bang_du_lieu_sach = xu_ly_loi_dinh_dang(bang_du_lieu_sach)

    print("\n--- BƯỚC 4: LƯU KẾT QUẢ ---")
    luu_du_lieu_sach(bang_du_lieu_sach, duong_dan_file_sach)

    print("\n" + "=" * 60)
    print("  HOÀN TẤT! Dữ liệu sạch đã sẵn sàng.")
    print("=" * 60)
    return bang_du_lieu_sach


# CHẠY TRỰC TIẾP
if __name__ == "__main__":
    TEN_FILE_GOC  = "sales_06_FY2020-21.csv"
    TEN_FILE_SACH = "sales_06_FY2020-21_cleaned.csv"

    bang_du_lieu_sach = quy_trinh_lam_sach(TEN_FILE_GOC, TEN_FILE_SACH)