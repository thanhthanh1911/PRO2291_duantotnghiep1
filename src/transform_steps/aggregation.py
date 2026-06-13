import pandas as pd
from pathlib import Path

# Đường dẫn đến file dữ liệu đã được làm sạch
INPUT_PATH = Path("data/cleaned/sales_cleaned.csv")

# Thư mục lưu các file tổng hợp sau khi xử lý
OUTPUT_DIR = Path("data/aggregates")


def create_aggregates():

    # Tạo thư mục aggregates nếu chưa tồn tại
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Đọc dữ liệu từ file CSV vào DataFrame
    # low_memory=False giúp tránh cảnh báo kiểu dữ liệu không đồng nhất
    df = pd.read_csv(INPUT_PATH, low_memory=False)

    # ==================================================
    # 1. TỔNG DOANH THU THEO NĂM
    # ==================================================

    # Nhóm dữ liệu theo cột year
    # Sau đó tính tổng doanh thu (total) của từng năm
    sales_by_year = (
        df.groupby("year")["total"]
        .sum()
        .reset_index()
    )

    # Lưu kết quả ra file CSV
    sales_by_year.to_csv(
        OUTPUT_DIR / "sales_by_year.csv",
        index=False
    )

    # ==================================================
    # 2. TỔNG DOANH THU THEO THÁNG
    # ==================================================

    # Nhóm dữ liệu theo tháng
    # Tính tổng doanh thu từng tháng
    sales_by_month = (
        df.groupby("month")["total"]
        .sum()
        .reset_index()
        .sort_values("month")  # Sắp xếp tháng từ 1 đến 12
    )

    # Xuất kết quả ra CSV
    sales_by_month.to_csv(
        OUTPUT_DIR / "sales_by_month.csv",
        index=False
    )

    # ==================================================
    # 3. TỔNG DOANH THU THEO VÙNG (REGION)
    # ==================================================

    # Nhóm dữ liệu theo vùng
    # Tính tổng doanh thu của từng vùng
    sales_by_region = (
        df.groupby("region")["total"]
        .sum()
        .reset_index()
        .sort_values("total", ascending=False)  # Cao xuống thấp
    )

    # Xuất kết quả ra CSV
    sales_by_region.to_csv(
        OUTPUT_DIR / "sales_by_region.csv",
        index=False
    )

    # ==================================================
    # 4. TỔNG DOANH THU THEO DANH MỤC SẢN PHẨM
    # ==================================================

    # Nhóm dữ liệu theo category
    # Tính tổng doanh thu từng danh mục
    sales_by_category = (
        df.groupby("category")["total"]
        .sum()
        .reset_index()
        .sort_values("total", ascending=False)
    )

    # Xuất kết quả ra CSV
    sales_by_category.to_csv(
        OUTPUT_DIR / "sales_by_category.csv",
        index=False
    )

    # ==================================================
    # 5. TOP 10 SẢN PHẨM CÓ DOANH THU CAO NHẤT
    # ==================================================

    # Nhóm dữ liệu theo mã sản phẩm (sku)
    # Tính tổng doanh thu từng sản phẩm
    # Sắp xếp giảm dần và lấy 10 sản phẩm đầu tiên
    top_products = (
        df.groupby("sku")["total"]
        .sum()
        .reset_index()
        .sort_values("total", ascending=False)
        .head(10)
    )

    # Xuất danh sách Top 10 sản phẩm
    top_products.to_csv(
        OUTPUT_DIR / "top_10_products.csv",
        index=False
    )

    # Thông báo hoàn thành
    print("Aggregation completed!")


# Điểm bắt đầu của chương trình
# Khi chạy file aggregation.py trực tiếp,
# hàm create_aggregates() sẽ được thực thi
if __name__ == "__main__":
    create_aggregates()