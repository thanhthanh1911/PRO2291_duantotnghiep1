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
│   │   └── sales_cleaned.csv
│   │
│   ├── dim_fact/
│   │   ├── dim_customer.csv
│   │   ├── dim_product.csv
│   │   ├── dim_location.csv
│   │   ├── dim_time.csv
│   │   └── fact_sales.csv
│   │
│   └── aggregates/
│       ├── agg_monthly_sales.csv
│       ├── agg_region_sales.csv
│       └── agg_discount_analysis.csv
│
├── src/
│   ├── cleaner.py
│   ├── eda.py
│   ├── transform.py
│   └── forecast.py
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
