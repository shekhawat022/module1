import numpy as np
import pandas as pd


DATA_FOLDER =  r"C:\Users\ankit\OneDrive\Documents\module1\task5"

orders      = pd.read_csv(f"{DATA_FOLDER}\\olist_orders_dataset.csv")
customers   = pd.read_csv(f"{DATA_FOLDER}\\olist_customers_dataset.csv")
products    = pd.read_csv(f"{DATA_FOLDER}\\olist_products_dataset.csv")
order_items = pd.read_csv(f"{DATA_FOLDER}\\olist_order_items_dataset.csv")


master = pd.merge(orders,      customers,   on="customer_id")
master = pd.merge(master,      order_items, on="order_id")
master = pd.merge(master,      products,    on="product_id")


customer_spend = (
    master.groupby("customer_id")["price"]
    .sum()
    .sort_values(ascending=False)
)
print("=== Top 10 customers by total spend ===")
print(customer_spend.head(10))


order_count  = master.groupby("customer_id")["order_id"].nunique()
single_order = order_count[order_count == 1]
print(f"\nNumber of customers with only one order: {len(single_order)}")

master["order_purchase_timestamp"] = pd.to_datetime(master["order_purchase_timestamp"])
master["Year"]  = master["order_purchase_timestamp"].dt.year
master["Month"] = master["order_purchase_timestamp"].dt.month
print("\n=== Sample: timestamp, Year, Month ===")
print(master[["order_purchase_timestamp", "Year", "Month"]].head())

master["MonthPeriod"] = master["order_purchase_timestamp"].dt.to_period("M").astype(str)

monthly_product_sales = (
    master.groupby(["product_id", "MonthPeriod"], as_index=False)["price"]
    .sum()
    .rename(columns={"price": "Sales"})
)
print("\n=== Monthly product sales (first 5 rows) ===")
print(monthly_product_sales.head())

master["customer_city"] = master["customer_city"].str.upper()

master["delivered"] = pd.to_datetime(master["order_delivered_customer_date"])
master["purchase"]  = master["order_purchase_timestamp"]
master["delivery_days"] = (master["delivered"] - master["purchase"]).dt.days

avg_delivery = master["delivery_days"].mean()
print(f"\nOverall average delivery time: {avg_delivery:.1f} days")

city_delivery = (
    master.groupby("customer_city")["delivery_days"]
    .mean()
    .sort_values(ascending=False)
)
print("\n=== Top 10 cities by average delivery time ===")
print(city_delivery.head(10))
