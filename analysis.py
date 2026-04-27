import pandas as pd

df = pd.read_csv("train.csv")

#1. missing values 
print("Missing Values:")
print(df.isnull().sum())

#2. duplicates
print("\nDuplicates:")
print(df.duplicated().sum())

# 3.data types
print("\nData Types:")
print(df.dtypes)

#4. data columns fix
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

#5. missing value drop
df = df.dropna(subset=["Postal Code"])

print("Cleaaning Done!")
print(df.dtypes)

#6. which region has the highest sale
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("Region wise sale:")
print(region_sales)

#7. Which category sells the most
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nCetagory wise sales:")
print(category_sales)

#8. which month has the highest order
df["Month"] = df['Order Date'].dt.month
monthly_orders = df.groupby('Month')['Order ID'].count().sort_values(ascending=False)
print("\nMonth wise sales:")
print(monthly_orders)

df.to_csv("clean_train.csv", index=False, encoding='utf-8-sig')
print("clean csv")

import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:mysql1332@localhost/superstore_project')

df.to_sql("superstore_data", engine, if_exists="replace", index=False)
print("9800 rows MySQL")