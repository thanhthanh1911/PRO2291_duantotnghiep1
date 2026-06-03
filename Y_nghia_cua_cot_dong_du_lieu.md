# KHẢO SÁT VÀ MÔ TẢ CHI TIẾT TẬP DỮ LIỆU DỰ ÁN

---
1. TỔNG QUAN VỀ TẬP DỮ LIỆU 

- Trong dự án "Phân tích doanh thu bán hàng", nhóm sử dụng tập dữ liệu sales_06_FY2020-21.csv làm nguồn dữ liệu chính để thực hiện quá trình tiền xử lý, phân tích và trực quan hóa dữ liệu.

- Tập dữ liệu chứa thông tin về các giao dịch bán hàng, khách hàng, sản phẩm, phương thức thanh toán và doanh thu phát sinh trong năm tài chính 2020–2021. Đây là nguồn dữ liệu có quy mô lớn, phù hợp để áp dụng các kỹ thuật phân tích dữ liệu nhằm đánh giá hiệu quả kinh doanh và hỗ trợ ra quyết định.

- Dữ liệu gốc bao gồm 36 thuộc tính (cột) và hơn 500 nghìn bản ghi (dòng). Nhưng thông qua quá trình xử lý dữ liệu đã loại bỏ   227.452 dòng trống hoặc trùng lặp, dữ liệu của nhóm hiện tại có 286.393 dòng chứa dữ liệu hợp lệ, từ đó phản ánh đúng chi tiết từng giao dịch bán hàng phát sinh trong hệ thống.

---
2. Ý nghĩa của dòng dữ liệu

- Mỗi dòng trong tập dữ liệu đại diện cho một giao dịch bán hàng hoặc một sản phẩm xuất hiện trong đơn hàng. Dòng dữ liệu chứa đầy đủ thông tin liên quan đến đơn hàng, bao gồm mã đơn hàng, thời gian giao dịch, số lượng sản phẩm, giá bán, doanh thu, khách hàng và khu vực địa lý.

- Việc phân tích theo từng dòng dữ liệu giúp xác định:

    * Doanh thu của từng giao dịch.
    * Sản phẩm bán chạy nhất.
    * Khu vực có doanh số cao.
    * Hành vi mua sắm của khách hàng.
    * Hiệu quả của các chương trình giảm giá.

---
3. Ý nghĩa của các cột dữ liệu

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

---
4. Vai trò của dữ liệu trong bài toán phân tích doanh thu

- Tập dữ liệu đóng vai trò là nền tảng cho toàn bộ quá trình phân tích doanh thu bán hàng. Các trường dữ liệu về giá bán, số lượng sản phẩm, giá trị đơn hàng và mức giảm giá được sử dụng để tính toán doanh thu thực tế. Thông tin về danh mục sản phẩm giúp xác định nhóm sản phẩm mang lại doanh thu cao nhất. Dữ liệu khách hàng hỗ trợ phân tích hành vi mua sắm và phân khúc khách hàng. Ngoài ra, dữ liệu vị trí địa lý như thành phố, khu vực và mã vùng cho phép đánh giá hiệu quả kinh doanh theo từng khu vực thị trường.

- Thông qua việc khai thác và phân tích tập dữ liệu này, nhóm có thể xây dựng các báo cáo trực quan nhằm đánh giá tình hình kinh doanh, nhận diện xu hướng bán hàng và đề xuất các giải pháp nâng cao doanh thu cho doanh nghiệp.