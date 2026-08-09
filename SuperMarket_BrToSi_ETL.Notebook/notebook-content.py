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

df = spark.read.format("csv").option("header","true").load("Files/Bronze_Supermarket_data/Customers.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Bronze_Supermarket_data/Customers.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Bronze_Supermarket_data/OrderDetails.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Bronze_Supermarket_data/OrderDetails.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Bronze_Supermarket_data/Orders.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Bronze_Supermarket_data/Orders.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Bronze_Supermarket_data/Products.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Bronze_Supermarket_data/Products.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Bronze_Supermarket_data/Stores.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Bronze_Supermarket_data/Stores.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 1: READ BRONZE CSV FILES
# ============================================================

bronze_path = "Files/Bronze_Supermarket_data"

df_customers = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "false")
    .option("nullValue", "")
    .load(f"{bronze_path}/Customers.csv")
)

df_stores = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "false")
    .option("nullValue", "")
    .load(f"{bronze_path}/Stores.csv")
)

df_products = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "false")
    .option("nullValue", "")
    .load(f"{bronze_path}/Products.csv")
)

df_orders = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "false")
    .option("nullValue", "")
    .load(f"{bronze_path}/Orders.csv")
)

df_orderdetails = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "false")
    .option("nullValue", "")
    .load(f"{bronze_path}/OrderDetails.csv")
)

print("All Bronze CSV files loaded successfully.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 2: CHECK BRONZE DATA
# ============================================================

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

display(df_customers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_stores)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orderdetails)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 3: CLEAN CUSTOMERS
# ============================================================

from pyspark.sql.functions import (
    col,
    trim,
    upper,
    when,
    to_date
)

df_customers = (
    df_customers

    # Data types
    .withColumn(
        "CustomerID",
        col("CustomerID").cast("int")
    )

    # Trim spaces
    .withColumn("FirstName", trim(col("FirstName")))
    .withColumn("LastName", trim(col("LastName")))
    .withColumn("City", trim(col("City")))
    .withColumn("Gender", trim(col("Gender")))

    # Replace NULL / blank FirstName
    .withColumn(
        "FirstName",
        when(
            col("FirstName").isNull() |
            (col("FirstName") == ""),
            "Unknown"
        ).otherwise(col("FirstName"))
    )

    # Replace NULL / blank LastName
    .withColumn(
        "LastName",
        when(
            col("LastName").isNull() |
            (col("LastName") == ""),
            "Unknown"
        ).otherwise(col("LastName"))
    )

    # Replace NULL / blank City
    .withColumn(
        "City",
        when(
            col("City").isNull() |
            (col("City") == ""),
            "Unknown"
        ).otherwise(col("City"))
    )

    # Replace NULL / blank Gender
    .withColumn(
        "Gender",
        when(
            col("Gender").isNull() |
            (col("Gender") == ""),
            "Unknown"
        ).otherwise(upper(col("Gender")))
    )

    # Remove duplicate CustomerID
    .dropDuplicates(["CustomerID"])

    # CustomerID is mandatory
    .dropna(subset=["CustomerID"])
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_customers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 4: CLEAN STORES
# ============================================================

df_stores = (
    df_stores

    # Data type
    .withColumn(
        "StoreID",
        col("StoreID").cast("int")
    )

    # Trim spaces
    .withColumn("StoreName", trim(col("StoreName")))
    .withColumn("City", trim(col("City")))
    .withColumn("StoreType", trim(col("StoreType")))

    # Missing StoreName
    .withColumn(
        "StoreName",
        when(
            col("StoreName").isNull() |
            (col("StoreName") == ""),
            "Unknown Store"
        ).otherwise(col("StoreName"))
    )

    # Missing City
    .withColumn(
        "City",
        when(
            col("City").isNull() |
            (col("City") == ""),
            "Unknown"
        ).otherwise(col("City"))
    )

    # Missing StoreType
    .withColumn(
        "StoreType",
        when(
            col("StoreType").isNull() |
            (col("StoreType") == ""),
            "Unknown"
        ).otherwise(col("StoreType"))
    )

    # Remove duplicate StoreID
    .dropDuplicates(["StoreID"])

    # StoreID is mandatory
    .dropna(subset=["StoreID"])
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_stores)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 5: CLEAN PRODUCTS
# ============================================================

df_products = (
    df_products

    # Correct data types
    .withColumn(
        "ProductID",
        col("ProductID").cast("int")
    )

    .withColumn(
        "Price",
        col("Price").cast("decimal(10,2)")
    )

    .withColumn(
        "StockQty",
        col("StockQty").cast("int")
    )

    # Trim text
    .withColumn(
        "ProductName",
        trim(col("ProductName"))
    )

    .withColumn(
        "Category",
        trim(col("Category"))
    )

    # Missing ProductName
    .withColumn(
        "ProductName",
        when(
            col("ProductName").isNull() |
            (col("ProductName") == ""),
            "Unknown Product"
        ).otherwise(col("ProductName"))
    )

    # Missing Category
    .withColumn(
        "Category",
        when(
            col("Category").isNull() |
            (col("Category") == ""),
            "Other"
        ).otherwise(col("Category"))
    )

    # Remove duplicate ProductID
    .dropDuplicates(["ProductID"])

    # ProductID required
    .dropna(subset=["ProductID"])

    # Price must be positive
    .filter(col("Price") > 0)

    # Stock cannot be negative
    .filter(col("StockQty") >= 0)
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 6: CLEAN ORDERS
# ============================================================

df_orders = (
    df_orders

    # Correct data types
    .withColumn(
        "OrderID",
        col("OrderID").cast("int")
    )

    .withColumn(
        "CustomerID",
        col("CustomerID").cast("int")
    )

    .withColumn(
        "StoreID",
        col("StoreID").cast("int")
    )

    .withColumn(
        "OrderDate",
        to_date(col("OrderDate"), "yyyy-MM-dd")
    )

    # Trim PaymentMethod
    .withColumn(
        "PaymentMethod",
        trim(col("PaymentMethod"))
    )

    # Standardize payment method
    .withColumn(
        "PaymentMethod",
        when(
            col("PaymentMethod").isNull() |
            (col("PaymentMethod") == ""),
            "Unknown"
        ).otherwise(upper(col("PaymentMethod")))
    )

    # Remove duplicate OrderID
    .dropDuplicates(["OrderID"])

    # Critical columns
    .dropna(
        subset=[
            "OrderID",
            "CustomerID",
            "StoreID",
            "OrderDate"
        ]
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 6: CLEAN ORDERS
# ============================================================

from pyspark.sql.functions import col, trim, upper, when, to_timestamp, to_date

df_orders = (
    df_orders

    # Correct numeric data types
    .withColumn(
        "OrderID",
        col("OrderID").cast("int")
    )

    .withColumn(
        "CustomerID",
        col("CustomerID").cast("int")
    )

    .withColumn(
        "StoreID",
        col("StoreID").cast("int")
    )

    # Convert timestamp to proper date
    .withColumn(
        "OrderDate",
        to_date(
            to_timestamp(
                col("OrderDate"),
                "yyyy-MM-dd HH:mm:ss.SSSSSSS"
            )
        )
    )

    # Trim PaymentMethod
    .withColumn(
        "PaymentMethod",
        trim(col("PaymentMethod"))
    )

    # Handle NULL / blank PaymentMethod
    .withColumn(
        "PaymentMethod",
        when(
            col("PaymentMethod").isNull() |
            (col("PaymentMethod") == ""),
            "Unknown"
        ).otherwise(
            upper(col("PaymentMethod"))
        )
    )

    # Remove duplicate OrderID
    .dropDuplicates(["OrderID"])

    # Remove rows with critical NULL values
    .dropna(
        subset=[
            "OrderID",
            "CustomerID",
            "StoreID",
            "OrderDate"
        ]
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# RELOAD ORDERS FROM BRONZE
# ============================================================

df_orders = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "false")
    .option("nullValue", "")
    .load("Files/Bronze_Supermarket_data/Orders.csv")
)

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# CLEAN ORDERS
# ============================================================

from pyspark.sql.functions import (
    col,
    trim,
    upper,
    when,
    substring
)

df_orders = (
    df_orders

    # -----------------------------
    # Correct numeric data types
    # -----------------------------
    .withColumn(
        "OrderID",
        col("OrderID").cast("int")
    )

    .withColumn(
        "CustomerID",
        col("CustomerID").cast("int")
    )

    .withColumn(
        "StoreID",
        col("StoreID").cast("int")
    )

    # -----------------------------
    # Convert OrderDate
    # -----------------------------
    # Example:
    # 2026-08-01 00:00:00.0000000
    #
    # becomes:
    # 2026-08-01
    #
    .withColumn(
        "OrderDate",
        substring(trim(col("OrderDate")), 1, 10)
    )

    # -----------------------------
    # Trim PaymentMethod
    # -----------------------------
    .withColumn(
        "PaymentMethod",
        trim(col("PaymentMethod"))
    )

    # -----------------------------
    # Handle NULL / blank PaymentMethod
    # -----------------------------
    .withColumn(
        "PaymentMethod",
        when(
            col("PaymentMethod").isNull() |
            (col("PaymentMethod") == ""),
            "Unknown"
        ).otherwise(
            upper(col("PaymentMethod"))
        )
    )

    # -----------------------------
    # Remove duplicate OrderID
    # -----------------------------
    .dropDuplicates(["OrderID"])

    # -----------------------------
    # Remove NULL critical fields
    # -----------------------------
    .dropna(
        subset=[
            "OrderID",
            "CustomerID",
            "StoreID",
            "OrderDate"
        ]
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import to_date

df_orders = df_orders.withColumn(
    "OrderDate",
    to_date(col("OrderDate"), "yyyy-MM-dd")
)

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

valid_customers = (
    df_customers
    .select("CustomerID")
    .distinct()
)

df_orders = (
    df_orders
    .join(
        valid_customers,
        on="CustomerID",
        how="inner"
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 7A: VALID CUSTOMER IDs
# ============================================================

valid_customers = (
    df_customers
    .select("CustomerID")
    .distinct()
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_orders = (
    df_orders
    .join(
        valid_customers,
        on="CustomerID",
        how="inner"
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 7B: VALID STORE IDs
# ============================================================

valid_stores = (
    df_stores
    .select("StoreID")
    .distinct()
)

df_orders = (
    df_orders
    .join(
        valid_stores,
        on="StoreID",
        how="inner"
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 8: CLEAN ORDER DETAILS
# ============================================================

df_orderdetails = (
    df_orderdetails

    # Correct data types
    .withColumn(
        "OrderDetailID",
        col("OrderDetailID").cast("int")
    )

    .withColumn(
        "OrderID",
        col("OrderID").cast("int")
    )

    .withColumn(
        "ProductID",
        col("ProductID").cast("int")
    )

    .withColumn(
        "Quantity",
        col("Quantity").cast("int")
    )

    .withColumn(
        "Discount",
        col("Discount").cast("decimal(5,2)")
    )

    # Remove duplicate OrderDetailID
    .dropDuplicates(["OrderDetailID"])

    # Critical fields
    .dropna(
        subset=[
            "OrderDetailID",
            "OrderID",
            "ProductID",
            "Quantity"
        ]
    )

    # Quantity must be > 0
    .filter(
        col("Quantity") > 0
    )

    # NULL discount = 0
    .withColumn(
        "Discount",
        when(
            col("Discount").isNull(),
            0
        ).otherwise(col("Discount"))
    )

    # Discount must be 0-100
    .filter(
        (col("Discount") >= 0) &
        (col("Discount") <= 100)
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orderdetails)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 9A: VALIDATE ORDER ID
# ============================================================

valid_orders = (
    df_orders
    .select("OrderID")
    .distinct()
)

df_orderdetails = (
    df_orderdetails
    .join(
        valid_orders,
        on="OrderID",
        how="inner"
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 9B: VALIDATE PRODUCT ID
# ============================================================

valid_products = (
    df_products
    .select("ProductID")
    .distinct()
)

df_orderdetails = (
    df_orderdetails
    .join(
        valid_products,
        on="ProductID",
        how="inner"
    )
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 10: SILVER DATA QUALITY CHECK
# ============================================================

print("======================================")
print("SILVER DATA QUALITY CHECK")
print("======================================")

print("Customers   :", df_customers.count())
print("Stores      :", df_stores.count())
print("Products    :", df_products.count())
print("Orders      :", df_orders.count())
print("OrderDetails:", df_orderdetails.count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_customers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_stores)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_orderdetails)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ============================================================
# STEP 11: SAVE SILVER DATA AS PARQUET
# ============================================================

silver_path = "Files/Silver_ETL_performed"

df_customers.write \
    .mode("overwrite") \
    .parquet(f"{silver_path}/Customers")

df_stores.write \
    .mode("overwrite") \
    .parquet(f"{silver_path}/Stores")

df_products.write \
    .mode("overwrite") \
    .parquet(f"{silver_path}/Products")

df_orders.write \
    .mode("overwrite") \
    .parquet(f"{silver_path}/Orders")

df_orderdetails.write \
    .mode("overwrite") \
    .parquet(f"{silver_path}/OrderDetails")

print("======================================")
print("BRONZE → SILVER ETL COMPLETED")
print("======================================")
print("Silver location:", silver_path)

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
