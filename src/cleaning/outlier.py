import pandas as pd


class OutlierDetector:
    def __init__(self, df):
        self.df = df.copy()

        # Các cột không cần kiểm tra outlier
        self.ignore_cols = [
            "cust_id",
            "item_id",
            "ref_num",
            "year"
        ]

    def check_data_loaded(self):
        """Kiểm tra dữ liệu đã được load chưa"""
        if self.df is None:
            raise ValueError(
                "Dữ liệu chưa được truyền vào!"
            )

    def get_numeric_columns(self):
        """Lấy danh sách các cột số cần kiểm tra"""
        self.check_data_loaded()

        return [
            col
            for col in self.df.select_dtypes(
                include=["int64", "float64", "int32", "float32"]
            ).columns
            if col not in self.ignore_cols
        ]

    def calculate_iqr(self, column):
        """Tính ngưỡng IQR cho một cột"""

        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        return lower_bound, upper_bound

    def detect_outliers(self):
        """Thống kê outlier từng cột"""

        self.check_data_loaded()

        result = {}

        for col in self.get_numeric_columns():

            lower_bound, upper_bound = self.calculate_iqr(col)

            outliers = self.df[
                (self.df[col] < lower_bound)
                | (self.df[col] > upper_bound)
            ]

            result[col] = {
                "lower_bound": lower_bound,
                "upper_bound": upper_bound,
                "outlier_count": len(outliers)
            }

        return result

    def show_outliers(self, column, n=10):
        """Hiển thị một số outlier của cột"""

        self.check_data_loaded()

        lower_bound, upper_bound = self.calculate_iqr(column)

        outliers = self.df[
            (self.df[column] < lower_bound)
            | (self.df[column] > upper_bound)
        ]

        print(f"\n===== OUTLIERS CỦA {column} =====")
        print(f"Tổng số outlier: {len(outliers)}")

        if len(outliers) > 0:
            print(outliers[[column]].head(n))

    def get_outlier_rows(self):
        """Lấy tất cả các dòng chứa outlier"""

        self.check_data_loaded()

        mask = pd.Series(
            False,
            index=self.df.index
        )

        for col in self.get_numeric_columns():

            lower_bound, upper_bound = self.calculate_iqr(col)

            mask |= (
                (self.df[col] < lower_bound)
                | (self.df[col] > upper_bound)
            )

        return self.df[mask]

    def flag_outliers(self):
        """Đánh dấu các dòng chứa outlier"""

        self.check_data_loaded()

        df_flagged = self.df.copy()

        df_flagged["is_outlier"] = False

        for col in self.get_numeric_columns():

            lower_bound, upper_bound = self.calculate_iqr(col)

            df_flagged["is_outlier"] = (
                df_flagged["is_outlier"]
                | (df_flagged[col] < lower_bound)
                | (df_flagged[col] > upper_bound)
            )

        return df_flagged

    def remove_outliers(self):
        """Loại bỏ outlier ở các cột quan trọng"""

        self.check_data_loaded()

        clean_df = self.df.copy()

        important_cols = [
            "qty_ordered",
            "price",
            "value",
            "total",
            "discount_amount"
        ]

        for col in important_cols:

            if col not in clean_df.columns:
                continue

            Q1 = clean_df[col].quantile(0.25)
            Q3 = clean_df[col].quantile(0.75)

            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            clean_df = clean_df[
                (clean_df[col] >= lower_bound)
                & (clean_df[col] <= upper_bound)
            ]

        return clean_df

    def summary(self):
        """Thông tin tổng quan dữ liệu"""

        self.check_data_loaded()

        print("\n===== DATA SUMMARY =====")
        print(f"Số dòng: {self.df.shape[0]}")
        print(f"Số cột: {self.df.shape[1]}")

        print("\nDanh sách cột:")
        for col in self.df.columns:
            print(f"- {col}")


def detect_outliers(df):
    """
    Hàm dùng cho cleaner.py:
    Trả về các dòng chứa outlier.
    """

    detector = OutlierDetector(df)

    report = detector.detect_outliers()

    print("\n===== BÁO CÁO OUTLIER =====")

    for col, info in report.items():

        print(f"\nCột: {col}")
        print(
            f"Lower Bound: "
            f"{info['lower_bound']:.2f}"
        )
        print(
            f"Upper Bound: "
            f"{info['upper_bound']:.2f}"
        )
        print(
            f"Số Outlier: "
            f"{info['outlier_count']}"
        )

    outlier_df = detector.get_outlier_rows()

    print("\n===== THỐNG KÊ OUTLIER =====")
    print(
        f"Số dòng chứa outlier: "
        f"{len(outlier_df)}"
    )

    return outlier_df


def flag_outliers(df):
    """
    Hàm dùng cho cleaner.py:
    Tạo cột is_outlier để đánh dấu dòng bất thường.
    """

    detector = OutlierDetector(df)

    df_flagged = detector.flag_outliers()

    print("Đã tạo cột is_outlier.")

    return df_flagged