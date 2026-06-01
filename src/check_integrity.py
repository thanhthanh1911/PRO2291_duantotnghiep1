import pandas as pd

fact = pd.read_csv("data/dim_fact/fact_sales.csv")
customer = pd.read_csv("data/dim_fact/dim_customer.csv")
product = pd.read_csv("data/dim_fact/dim_product.csv")
location = pd.read_csv("data/dim_fact/dim_location.csv")
time = pd.read_csv("data/dim_fact/dim_time.csv")

print("Null values in fact_sales:")
print(fact.isnull().sum())

print("Duplicate rows in fact_sales:")
print(fact.duplicated().sum())

print("Customer key check:")
print(fact["customer_id"].isin(customer["customer_id"]).all())

print("Product key check:")
print(fact["product_id"].isin(product["product_id"]).all())

print("Location key check:")
print(fact["location_id"].isin(location["location_id"]).all())

print("Date key check:")
print(fact["date_id"].isin(time["date_id"]).all())