import pandas as pd


class FeatureEngineering:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Đọc dữ liệu thành công!")

    def create_revenue(self):
        if self.df is None:
            raise ValueError("Vui lòng load dữ liệu trước.")

        self.df["revenue"] = (
            self.df["quantity"] * self.df["unit_price"]
        )

    def create_profit(self):
        if self.df is None:
            raise ValueError("Vui lòng load dữ liệu trước.")

        self.df["profit"] = (
            self.df["revenue"]
            - (self.df["quantity"] * self.df["unit_cost"])
        )

    def create_time_features(self, date_col):
        if self.df is None:
            raise ValueError("Vui lòng load dữ liệu trước.")

        self.df[date_col] = pd.to_datetime(self.df[date_col])

        self.df["month"] = self.df[date_col].dt.month
        self.df["quarter"] = self.df[date_col].dt.quarter
        self.df["year_month"] = self.df[date_col].dt.strftime("%Y-%m")

    def get_data(self):
        """Trả về DataFrame sau khi xử lý"""
        return self.df
    

