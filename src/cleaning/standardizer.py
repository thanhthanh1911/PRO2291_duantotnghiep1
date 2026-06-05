
import re
import unicodedata
import pandas as pd

#df = pd.read_csv(r"E:\DATN - Three Correct\PRO2291_duantotnghiep1\data\raw\sales_06_FY2020-21.csv")
#df.head() 
 
class Standardizer:
    def __init__(self):
        pass
 
    def clean_text(self, text):
        """Làm sạch text chung: bỏ ký tự đặc biệt, chuẩn hóa Unicode, lowercase."""
        if pd.isna(text):
            return ""
 
        text = str(text)
        text = unicodedata.normalize("NFC", text)
 
        # Bỏ ký tự đặc biệt (giữ chữ, số, email symbols cơ bản)
        text = re.sub(r"[^0-9a-zA-ZÀ-ỹ\s@._-]", " ", text)
 
        # Gộp khoảng trắng
        text = re.sub(r"\s+", " ", text).strip()
 
        return text.lower()
 
    def clean_name(self, text):
        """Chuẩn hóa tên: capitalize từng từ."""
        text = self.clean_text(text)
        return " ".join([w.capitalize() for w in text.split()])
 
    def clean_phone(self, text):
        """Chỉ giữ chữ số trong số điện thoại."""
        if pd.isna(text):
            return ""
        digits = re.sub(r"\D", "", str(text))
        return digits
 
    def validate_phone(self, phone: str) -> bool:
        """Kiểm tra độ dài hợp lệ (9–11 chữ số cho VN)."""
        return 9 <= len(phone) <= 11
 
    def validate_email(self, email: str) -> bool:
        """Kiểm tra email có chứa @ không."""
        return "@" in email
 
    def validate(self, df: pd.DataFrame) -> None:
        """Log ra các dòng bất thường sau khi transform."""
        issues = []
 
        if "Phone No." in df.columns:
            bad_phone = df[~df["Phone No."].apply(self.validate_phone) & (df["Phone No."] != "")]
            if not bad_phone.empty:
                issues.append(f"  - {len(bad_phone)} dòng số điện thoại không hợp lệ (< 9 hoặc > 11 chữ số)")
 
        if "E Mail" in df.columns:
            bad_email = df[~df["E Mail"].apply(self.validate_email) & (df["E Mail"] != "")]
            if not bad_email.empty:
                issues.append(f"  - {len(bad_email)} dòng email không hợp lệ (thiếu @)")
 
        if issues:
            print("[validate] Phát hiện dữ liệu bất thường:")
            for msg in issues:
                print(msg)
        else:
            print("[validate] Dữ liệu hợp lệ, không có vấn đề.")
 
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Pipeline chính: làm sạch và chuẩn hóa toàn bộ DataFrame."""
        df = df.copy()
 
        # Normalize tên cột: bỏ khoảng trắng thừa ở đầu/cuối
        df.columns = df.columns.str.strip()
 
        # Xóa dòng rỗng hoàn toàn
        df = df.dropna(how="all")
 
        # Xóa duplicate
        df = df.drop_duplicates()
 
        # Text columns
        text_cols = [
            "status", "sku", "category", "payment_method",
            "bi_st", "Region", "City", "State", "County",
            "User Name", "Place Name",
        ]
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].apply(self.clean_text)
 
        # Tên
        for col in ["First Name", "Last Name", "full_name"]:
            if col in df.columns:
                df[col] = df[col].apply(self.clean_name)
 
        # Email
        if "E Mail" in df.columns:
            df["E Mail"] = df["E Mail"].apply(self.clean_text)
 
        # Số điện thoại
        if "Phone No." in df.columns:
            df["Phone No."] = df["Phone No."].apply(self.clean_phone)
 
        # Ngày (vectorized, dd/mm/yyyy của VN)
        if "order_date" in df.columns:
            df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True, errors="coerce")
 
        if "Customer Since" in df.columns:
            df["Customer Since"] = pd.to_datetime(df["Customer Since"], dayfirst=True, errors="coerce")
 
        # Validate sau khi transform
        self.validate(df)
 
        return df