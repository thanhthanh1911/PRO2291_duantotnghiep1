# PRO2291_duantotnghiep1
phân tích doanh thu bán hàng 
---

##  Mục lục

- [Tổng quan dự án](#-tổng-quan-dự-án)
- [Phát hiện chính](#-phát-hiện-chính-key-findings)
- [Kiến trúc hệ thống](#-kiến-trúc-hệ-thống)
- [Dashboard](#-dashboard)
- [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [Hướng dẫn cài đặt](#-hướng-dẫn-cài-đặt--chạy)
- [Dữ liệu đầu ra](#-dữ-liệu-đầu-ra)
- [Kết quả phân tích](#-kết-quả-phân-tích)
- [Nhóm thực hiện](#-nhóm-thực-hiện)

---
##  Tổng quan dự án


Dự án xây dựng hệ thống phân tích doanh thu bán hàng và hành vi khách hàng nhằm hỗ trợ doanh nghiệp:

* theo dõi hiệu quả kinh doanh,
* tối ưu chiến lược bán hàng,
* đánh giá hiệu quả giảm giá,
* và dự báo xu hướng doanh thu.

<<<<<<< HEAD
---
### 1. Ý nghĩa của dòng dữ liệu

- Mỗi dòng trong tập dữ liệu đại diện cho một giao dịch bán hàng hoặc một sản phẩm xuất hiện trong đơn hàng. Dòng dữ liệu chứa đầy đủ thông tin liên quan đến đơn hàng, bao gồm mã đơn hàng, thời gian giao dịch, số lượng sản phẩm, giá bán, doanh thu, khách hàng và khu vực địa lý.

- Việc phân tích theo từng dòng dữ liệu giúp xác định:

    * Doanh thu của từng giao dịch.
    * Sản phẩm bán chạy nhất.
    * Khu vực có doanh số cao.
    * Hành vi mua sắm của khách hàng.
    * Hiệu quả của các chương trình giảm giá.


### 2. Ý nghĩa của các cột dữ liệu

Bảng của phần 3 mô tả các trường dữ liệu được sử dụng trong nghiên cứu.

| STT | Tên cột          | Ý nghĩa                              |
| --- | ---------------- | ------------------------------------ |
| 1   | order_id         | Mã định danh đơn hàng                |
| 2   | order_date       | Ngày phát sinh đơn hàng              |
| 3   | status           | Trạng thái đơn hàng                  |
| 4   | item_id          | Mã sản phẩm                          |
| 5   | sku              | Mã SKU của sản phẩm                  |
| 6   | qty_ordered      | Số lượng sản phẩm được đặt mua       |
| 7   | price            | Giá bán của một đơn vị sản phẩm      |
| 8   | value            | Giá trị đơn hàng trước giảm giá      |
| 9   | discount_amount  | Số tiền được giảm giá                |
| 10  | total            | Tổng giá trị thanh toán cuối cùng    |
| 11  | category         | Danh mục sản phẩm                    |
| 12  | payment_method   | Phương thức thanh toán               |
| 13  | bi_st            | Trạng thái nghiệp vụ của đơn hàng    |
| 14  | cust_id          | Mã khách hàng                        |
| 15  | year             | Năm giao dịch                        |
| 16  | month            | Tháng giao dịch                      |
| 17  | ref_num          | Mã tham chiếu giao dịch              |
| 18  | Name Prefix      | Danh xưng khách hàng (Mr., Mrs.,...) |
| 19  | First Name       | Tên khách hàng                       |
| 20  | Middle Initial   | Chữ cái đầu tên đệm                  |
| 21  | Last Name        | Họ khách hàng                        |
| 22  | Gender           | Giới tính khách hàng                 |
| 23  | age              | Tuổi khách hàng                      |
| 24  | full_name        | Họ và tên đầy đủ                     |
| 25  | E Mail           | Địa chỉ thư điện tử                  |
| 26  | Customer Since   | Thời điểm trở thành khách hàng       |
| 27  | SSN              | Mã định danh khách hàng              |
| 28  | Phone No.        | Số điện thoại                        |
| 29  | Place Name       | Tên địa điểm                         |
| 30  | County           | Quận/Huyện                           |
| 31  | City             | Thành phố                            |
| 32  | State            | Bang/Tỉnh                            |
| 33  | Zip              | Mã bưu chính                         |
| 34  | Region           | Khu vực địa lý                       |
| 35  | User Name        | Tên tài khoản khách hàng             |
| 36  | Discount_Percent | Tỷ lệ phần trăm giảm giá             |


### 3. Vai trò của dữ liệu trong bài toán phân tích doanh thu

- Tập dữ liệu đóng vai trò là nền tảng cho toàn bộ quá trình phân tích doanh thu bán hàng. Các trường dữ liệu về giá bán, số lượng sản phẩm, giá trị đơn hàng và mức giảm giá được sử dụng để tính toán doanh thu thực tế. Thông tin về danh mục sản phẩm giúp xác định nhóm sản phẩm mang lại doanh thu cao nhất. Dữ liệu khách hàng hỗ trợ phân tích hành vi mua sắm và phân khúc khách hàng. Ngoài ra, dữ liệu vị trí địa lý như thành phố, khu vực và mã vùng cho phép đánh giá hiệu quả kinh doanh theo từng khu vực thị trường.

- Thông qua việc khai thác và phân tích tập dữ liệu này, nhóm có thể xây dựng các báo cáo trực quan nhằm đánh giá tình hình kinh doanh, nhận diện xu hướng bán hàng và đề xuất các giải pháp nâng cao doanh thu cho doanh nghiệp.
---

=======
>>>>>>> 70a820003d7e8a54f83e29601cdabab6379d1321
## Phát hiện chính (Key Findings)

Dựa trên 286.392 giao dịch bán hàng trong giai đoạn 2020–2021, hệ thống phân tích đã phát hiện nhiều xu hướng quan trọng hỗ trợ doanh nghiệp trong việc ra quyết định kinh doanh.

### 1. Quy mô kinh doanh

| Chỉ số                | Giá trị      |
| --------------------- | ------------ |
| Tổng giao dịch        | 286.392      |
| Tổng doanh thu        | 233,65 triệu |
| Số nhóm sản phẩm      | 15           |
| Số khu vực kinh doanh | 4            |
| Giảm giá trung bình   | 6,07%        |

### 2. Danh mục sản phẩm tạo doanh thu cao nhất

| Danh mục          |    Doanh thu |
| ----------------- | -----------: |
| Mobiles & Tablets | 130,11 triệu |
| Appliances        |  30,06 triệu |
| Entertainment     |  27,14 triệu |
| Others            |  15,56 triệu |
| Computing         |   9,36 triệu |

**Nhận xét:**

* Nhóm **Mobiles & Tablets** là nguồn doanh thu chủ lực của doanh nghiệp.
* Doanh thu từ Mobiles & Tablets cao hơn rất nhiều so với các nhóm còn lại.
* Các chiến lược Marketing và bán hàng nên tập trung vào nhóm sản phẩm này để tối đa hóa doanh thu.

### 3. Sản phẩm được mua nhiều nhất

| Danh mục          | Số giao dịch |
| ----------------- | -----------: |
| Mobiles & Tablets |       61.761 |
| Men's Fashion     |       40.713 |
| Appliances        |       33.034 |
| Women's Fashion   |       28.334 |
| Others            |       26.108 |

**Nhận xét:**

* Khách hàng có xu hướng mua các mặt hàng công nghệ và thiết bị điện tử nhiều hơn các nhóm khác.
* Thời trang nam và nữ có lượng giao dịch lớn nhưng giá trị đơn hàng thấp hơn nhóm công nghệ.

### 4. Hiệu quả kinh doanh theo khu vực

| Khu vực   |   Doanh thu |
| --------- | ----------: |
| South     | 89,65 triệu |
| Midwest   | 62,92 triệu |
| West      | 41,12 triệu |
| Northeast | 39,96 triệu |

**Nhận xét:**

* Khu vực **South** đóng góp doanh thu lớn nhất toàn hệ thống.
* South chiếm tỷ trọng đáng kể trong tổng doanh thu và là thị trường trọng điểm.
* Northeast là khu vực có doanh thu thấp nhất, cần nghiên cứu thêm về nhu cầu khách hàng và chiến lược bán hàng.

### 5. Tác động của chính sách giảm giá

* Mức giảm giá trung bình của toàn bộ giao dịch là **6,07%**.
* Doanh nghiệp thường áp dụng mức giảm giá thấp để duy trì doanh thu.
* Cần tiếp tục phân tích sâu mối quan hệ giữa Discount và Revenue để xác định ngưỡng giảm giá tối ưu.

### 6. Cơ hội kinh doanh

Từ các kết quả phân tích ban đầu, doanh nghiệp có thể:

* Tập trung đầu tư vào nhóm Mobiles & Tablets.
* Tăng cường chiến dịch bán hàng tại khu vực South.
* Nghiên cứu cải thiện doanh số tại Northeast.
* Tối ưu chính sách giảm giá nhằm cân bằng giữa doanh thu và lợi nhuận.
* Xây dựng mô hình dự báo doanh thu phục vụ lập kế hoạch kinh doanh trong tương lai.
<<<<<<< HEAD
---
=======


>>>>>>> 70a820003d7e8a54f83e29601cdabab6379d1321
## Các vấn đề doanh nghiệp có thể giải quyết
| # | Vấn đề                                 | Giải pháp phân tích                |
| - | -------------------------------------- | ---------------------------------- |
| 1 | Không theo dõi được xu hướng doanh thu | Dashboard doanh thu theo thời gian |
| 2 | Không biết sản phẩm nào hiệu quả       | Product Performance Analysis       |
| 3 | Giảm giá ảnh hưởng lợi nhuận           | Discount Impact Analysis           |
| 4 | Không hiểu hành vi khách hàng          | Customer Segmentation              |
| 5 | Không biết khu vực bán mạnh            | Regional Sales Analysis            |
| 6 | Khó dự báo doanh thu                   | Forecasting Dashboard              |

## Dataset
| Tiêu chí   | Giá trị                                  |
| ---------- | ---------------------------------------- |
| Nguồn      | https://www.kaggle.com/datasets/datafish101/sales-06-fy2020-21-copy        |
| Quy mô     | 286,393 giao dịch                       |
| Thời gian  | 2020–2021                              |
| Phạm vi    | Bán hàng thương mại điện tử              |
| Thành phần | Sales, Customer, Product, Geography      |
| Mục tiêu   | Phân tích doanh thu & hành vi khách hàng |


---
## Kiến trúc hệ thống

Dự án được xây dựng theo quy trình Data Pipeline gồm 6 lớp, từ dữ liệu thô ban đầu đến Dashboard phân tích cuối cùng.

```text
DATA PIPELINE (6 LAYERS)

┌──────────────┬──────────────┬──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┐
│ Layer 1      │ Layer 2      │ Layer 3              │ Layer 4              │ Layer 5              │ Layer 6              │
│ Source       │ Explore      │ Transform & Clean    │ Model                │ Aggregate            │ Visualize            │
├──────────────┼──────────────┼──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ Raw CSV      │ EDA          │ Cleaning             │ Star Schema          │ Data Marts           │ Dashboard            │
│ sales_06     │ Pandas       │ Feature Engineering  │ Fact & Dimension     │ Aggregated Tables    │ Tableau  / Python    │
│ FY2020-21    │ NumPy        │ KPI Calculation      │ SQL Server Ready     │ CSV Outputs          │ Visualization        │
└──────────────┴──────────────┴──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┘
```
---
## Star Schema
```
                         ┌──────────────────┐
                         │    dim_time      │
                         │──────────────────│
                         │ date_id          │
                         │ order_date       │
                         │ day              │
                         │ month            │
                         │ quarter          │
                         │ year             │
                         └────────┬─────────┘
                                  │
                                  │
┌──────────────────┐      ┌───────▼────────┐      ┌──────────────────┐
│  dim_customer    │      │   fact_sales   │      │   dim_product    │
│──────────────────│      │────────────────│      │──────────────────│
│ customer_id      │──────│ customer_id    │──────│ product_id       │
│ gender           │      │ product_id     │      │ sku              │
│ age              │      │ date_id        │      │ category         │
│ customer_since   │      │ location_id    │      │ price            │
└──────────────────┘      │ order_id       │      └──────────────────┘
                          │ qty_ordered    │
                          │ price          │
                          │ discount       │
                          │ revenue        │
                          │ status         │
                          └───────┬────────┘
                                  │
                                  │
                         ┌────────▼─────────┐
                         │  dim_location    │
                         │──────────────────│
                         │ location_id      │
                         │ city             │
                         │ state            │
                         │ region           │
                         │ zip              │
                         └──────────────────┘

```
---
##  Cấu trúc thư mục

```
PRO2291_duantotnghiep1/
│
├── data/
│   ├── raw/
│   │   └── sales_06_FY2020-21.csv
│   │
│   ├── cleaned/
│   │   ├── sales_cleaned.csv
│   │   └── outliers.csv
│   │
│   ├── dim_fact/
│   │   ├── dim_customer.csv
│   │   ├── dim_product.csv
│   │   ├── dim_location.csv
│   │   ├── dim_time.csv
│   │   └── fact_sales.csv
│   │
│   └── aggregates/
│       ├── revenue_by_month.csv
│       ├── revenue_by_region.csv
│       ├── revenue_by_category.csv
│       └── top_customers.csv
│
├── src/
│   ├── cleaner.py
│   ├── eda.py
│   ├── check_integrity.py
│   ├── main.py
│   ├── transform.py
│   ├── forecast.py
│   └── cleaning/
│       ├── __init__.py
│       ├── null.py
│       ├── outlier.py
│       ├── standardizer.py
│       └── datatype.py
│
├── notebooks/
│   └── eda.ipynb
│
├── dashboards/
│   └── dashboard_final.twb
│
├── docs/
│   ├── bao_cao_final.docx
│   └── images/
│
├── README.md
├── requirements.txt
└── .gitignore
```
