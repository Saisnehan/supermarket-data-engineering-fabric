# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "820fef14-d0a3-4589-90bf-9c140a159cac",
# META       "default_lakehouse_name": "Supermarket_Raw_Data",
# META       "default_lakehouse_workspace_id": "759aa60a-f2cd-4b13-af28-a56c44ed485a",
# META       "known_lakehouses": [
# META         {
# META           "id": "820fef14-d0a3-4589-90bf-9c140a159cac"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet("Files/Silver_ETL_performed/Customers/part-00000-60931bed-6c37-4517-889f-c1fe37e1429b-c000.snappy.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/Silver_ETL_performed/Customers/part-00000-60931bed-6c37-4517-889f-c1fe37e1429b-c000.snappy.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet("Files/Silver_ETL_performed/OrderDetails/part-00000-570a6926-da7c-412a-a5d8-4789b0de648f-c000.snappy.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/Silver_ETL_performed/OrderDetails/part-00000-570a6926-da7c-412a-a5d8-4789b0de648f-c000.snappy.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet("Files/Silver_ETL_performed/Orders/part-00000-a2f4c1f2-ff83-4538-b43e-0d1f54700ec4-c000.snappy.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/Silver_ETL_performed/Orders/part-00000-a2f4c1f2-ff83-4538-b43e-0d1f54700ec4-c000.snappy.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet("Files/Silver_ETL_performed/Products/part-00000-86c699a0-13a5-49ae-87ea-cbbcf8d9d822-c000.snappy.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/Silver_ETL_performed/Products/part-00000-86c699a0-13a5-49ae-87ea-cbbcf8d9d822-c000.snappy.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet("Files/Silver_ETL_performed/Stores/part-00000-b5500c69-9de4-48fb-962a-950abf122853-c000.snappy.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/Silver_ETL_performed/Stores/part-00000-b5500c69-9de4-48fb-962a-950abf122853-c000.snappy.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 12: LOAD SILVER DATA
# ============================================================

silver_path = "Files/Silver_ETL_performed"

df_customers = spark.read.parquet(
    f"{silver_path}/Customers"
)

df_orderdetails = spark.read.parquet(
    f"{silver_path}/OrderDetails"
)

df_orders = spark.read.parquet(
    f"{silver_path}/Orders"
)

df_products = spark.read.parquet(
    f"{silver_path}/Products"
)

df_stores = spark.read.parquet(
    f"{silver_path}/Stores"
)

print("======================================")
print("SILVER DATA LOADED")
print("======================================")

print("Customers   :", df_customers.count())
print("OrderDetails:", df_orderdetails.count())
print("Orders      :", df_orders.count())
print("Products    :", df_products.count())
print("Stores      :", df_stores.count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 12: LOAD SILVER DATA
# ============================================================

silver_path = "Files/Silver_ETL_performed"

df_customers = spark.read.parquet(
    f"{silver_path}/Customers"
)

df_orderdetails = spark.read.parquet(
    f"{silver_path}/OrderDetails"
)

df_orders = spark.read.parquet(
    f"{silver_path}/Orders"
)

df_products = spark.read.parquet(
    f"{silver_path}/Products"
)

df_stores = spark.read.parquet(
    f"{silver_path}/Stores"
)

print("======================================")
print("SILVER DATA LOADED")
print("======================================")

print("Customers   :", df_customers.count())
print("OrderDetails:", df_orderdetails.count())
print("Orders      :", df_orders.count())
print("Products    :", df_products.count())
print("Stores      :", df_stores.count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print("Customers:", df_customers.count())
print("Stores:", df_stores.count())
print("Products:", df_products.count())
print("Orders:", df_orders.count())
print("OrderDetails:", df_orderdetails.count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col, concat_ws, round

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 13: CREATE GOLD SALES DATASET
# ============================================================

df_sales = (
    df_orderdetails.alias("od")

    # OrderDetails → Orders
    .join(
        df_orders.alias("o"),
        col("od.OrderID") == col("o.OrderID"),
        "inner"
    )

    # Orders → Customers
    .join(
        df_customers.alias("c"),
        col("o.CustomerID") == col("c.CustomerID"),
        "inner"
    )

    # OrderDetails → Products
    .join(
        df_products.alias("p"),
        col("od.ProductID") == col("p.ProductID"),
        "inner"
    )

    # Orders → Stores
    .join(
        df_stores.alias("s"),
        col("o.StoreID") == col("s.StoreID"),
        "inner"
    )

    .select(
        col("od.OrderDetailID"),
        col("o.OrderID"),
        col("o.OrderDate"),

        col("c.CustomerID"),

        concat_ws(
            " ",
            col("c.FirstName"),
            col("c.LastName")
        ).alias("CustomerName"),

        col("s.StoreID"),
        col("s.StoreName"),
        col("s.City").alias("StoreCity"),

        col("p.ProductID"),
        col("p.ProductName"),
        col("p.Category"),

        col("od.Quantity"),
        col("p.Price"),
        col("od.Discount"),

        col("o.PaymentMethod")
    )
)

display(df_sales)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 14: CALCULATE SALES AMOUNTS
# ============================================================

df_sales = (
    df_sales

    .withColumn(
        "GrossAmount",
        round(
            col("Quantity") * col("Price"),
            2
        )
    )

    .withColumn(
        "DiscountAmount",
        round(
            col("GrossAmount") *
            col("Discount") / 100,
            2
        )
    )

    .withColumn(
        "NetAmount",
        round(
            col("GrossAmount") -
            col("DiscountAmount"),
            2
        )
    )
)

display(df_sales)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 15: SAVE GOLD SALES
# ============================================================

df_sales.write \
    .format("delta") \
    .mode("overwrite") \
    .save("Tables/Gold_Sales")

print("Gold_Sales created successfully.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import sum, count

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 16: CATEGORY SALES SUMMARY
# ============================================================

df_category_sales = (
    df_sales
    .groupBy("Category")
    .agg(
        sum("Quantity").alias("TotalQuantity"),
        round(sum("GrossAmount"), 2).alias("GrossSales"),
        round(sum("DiscountAmount"), 2).alias("TotalDiscount"),
        round(sum("NetAmount"), 2).alias("NetSales"),
        count("OrderID").alias("NumberOfOrders")
    )
)

display(df_category_sales)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 17: SAVE CATEGORY SALES
# ============================================================

df_category_sales.write \
    .format("delta") \
    .mode("overwrite") \
    .save("Tables/Gold_Category_Sales")

print("Gold_Category_Sales created successfully.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet("Tables/Gold_Category_Sales/part-00000-09278984-1d19-46ad-a790-3f4d4384b354-c000.snappy.parquet")
# df now is a Spark DataFrame containing parquet data from "Tables/Gold_Category_Sales/part-00000-09278984-1d19-46ad-a790-3f4d4384b354-c000.snappy.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet("Tables/Gold_Sales/part-00000-13c23cd6-3350-4560-a09f-ab2e1c3cb18b-c000.snappy.parquet")
# df now is a Spark DataFrame containing parquet data from "Tables/Gold_Sales/part-00000-13c23cd6-3350-4560-a09f-ab2e1c3cb18b-c000.snappy.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
