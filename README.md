# 🛒 Supermarket Data Engineering Project

> **End-to-End Data Engineering Solution using Microsoft Fabric**

![Microsoft Fabric](https://img.shields.io/badge/Microsoft%20Fabric-Data%20Engineering-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)
![SQL](https://img.shields.io/badge/SQL-Data%20Warehouse-lightgrey)
![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-yellow)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black)

---

## 📌 Project Overview

The **Supermarket Data Engineering Project** is an end-to-end data engineering solution built using **Microsoft Fabric**.

The project demonstrates how raw transactional data can be ingested from an on-premises SQL Server database, stored in a Lakehouse, transformed through Bronze → Silver → Gold layers, loaded into a Data Warehouse, and finally consumed by a Power BI semantic model and interactive business dashboard.

The solution follows a modern **Medallion Architecture** to improve data quality, maintainability, scalability, and analytical performance.

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   SQL Server         │
                    │  On-Premises Source  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Pipeline       │
                    │  Copy Activity        │
                    └──────────┬───────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │        BRONZE LAYER             │
              │      Microsoft Fabric          │
              │          Lakehouse              │
              │                                │
              │ Customers.csv                  │
              │ Orders.csv                     │
              │ OrderDetails.csv               │
              │ Products.csv                   │
              │ Stores.csv                     │
              └───────────────┬────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │        SILVER LAYER             │
              │       Data Cleaning & ETL       │
              │                                │
              │ • Remove duplicates            │
              │ • Trim whitespace              │
              │ • Handle null values           │
              │ • Correct data types            │
              │ • Validate foreign keys        │
              │ • Remove invalid records       │
              └───────────────┬────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │          GOLD LAYER             │
              │       Business Modeling         │
              │                                │
              │ Gold_Sales                     │
              │ Gold_Category_Sales            │
              └───────────────┬────────────────┘
                              │
                 ┌────────────┴─────────────┐
                 ▼                          ▼
      ┌────────────────────┐     ┌────────────────────┐
      │ Fabric Warehouse   │     │ Power BI Semantic  │
      │                    │     │ Model              │
      └────────────────────┘     └──────────┬─────────┘
                                            │
                                            ▼
                                  ┌────────────────────┐
                                  │ Power BI Dashboard │
                                  │                    │
                                  │ • Sales KPIs       │
                                  │ • Sales Trends     │
                                  │ • Category Sales   │
                                  │ • Top Products     │
                                  │ • Store Analysis   │
                                  └────────────────────┘

🎯 Business Problem

Supermarket businesses generate large amounts of transactional data from customers, stores, products, and orders.

However, raw transactional data is not immediately suitable for analytics because it may contain:

Duplicate records
Missing values
Invalid foreign keys
Inconsistent text formatting
Incorrect data types
Raw transactional structures

This project builds a complete data pipeline that transforms raw supermarket data into a trusted analytical data platform.

The final solution enables business users to answer questions such as:

What are the total sales?
Which products generate the highest revenue?
Which categories perform best?
Which stores generate the most sales?
How are sales changing over time?
What is the average order value?
How much discount is being given?
Which products have the highest sales volume?
🗂️ Source Data

The project uses five major source datasets:

Dataset	Description
Customers	Customer information
Orders	Order-level transaction information
OrderDetails	Product-level order details
Products	Product and category information
Stores	Store information
Source System

SQL Server

The source data is initially stored in an on-premises SQL Server environment and ingested into Microsoft Fabric.

🥉 Bronze Layer

The Bronze layer stores the raw source data with minimal transformation.

Technologies
Microsoft Fabric Lakehouse
Fabric Data Pipeline
SQL Server
OneLake
Bronze datasets
Bronze_Supermarket_data/
│
├── Customers.csv
├── Orders.csv
├── OrderDetails.csv
├── Products.csv
└── Stores.csv

The purpose of this layer is to maintain a reliable copy of the source data before transformation.

🥈 Silver Layer

The Silver layer contains cleaned and validated data.

ETL transformations were implemented using PySpark and Dataflow Gen2.

Data Quality Transformations
1. Duplicate Removal

Duplicate records were identified and removed using business keys such as:

CustomerID
OrderID
OrderDetailID
ProductID
StoreID
2. Whitespace Cleaning

Leading and trailing spaces were removed from text fields.

Example:

from pyspark.sql.functions import trim

df = df.withColumn(
    "CustomerName",
    trim(col("CustomerName"))
)
3. Null Handling

Rows containing null values in critical fields were removed.

Example:

df = df.dropna(
    subset=[
        "CustomerID",
        "FirstName",
        "LastName"
    ]
)
4. Data Type Correction

Columns were converted into appropriate data types such as:

CustomerID → Integer
Quantity   → Integer
Price      → Decimal
Discount   → Decimal
OrderDate  → Date
5. Foreign Key Validation

Invalid relationships were removed by joining transactional tables with valid customer records.

Example:

df_orders = df_orders.join(
    df_customers.select("CustomerID"),
    "CustomerID",
    "inner"
)

This ensures that transactional records reference valid customers.

🥈 Silver Data Storage

Cleaned data is stored in the Lakehouse as Parquet files.

Silver_ETL_performed/
│
├── Customers/
├── Orders/
├── OrderDetails/
├── Products/
└── Stores/

Parquet provides a columnar storage format suitable for analytical workloads.

🥇 Gold Layer

The Gold layer contains business-ready datasets designed for analytics and reporting.

Gold_Sales

A denormalized analytical dataset combining information from:

Customers
Orders
Order Details
Products
Stores

Example attributes include:

OrderID
OrderDate
CustomerID
CustomerName
ProductID
ProductName
Category
StoreID
StoreName
StoreCity
Quantity
Price
Discount
GrossAmount
DiscountAmount
NetAmount
PaymentMethod

This structure simplifies Power BI reporting and reduces the complexity of analytical queries.

Gold_Category_Sales

An aggregated dataset used for category-level analysis.

Example metrics:

Category
GrossSales
NetSales
TotalDiscount
TotalQuantity
NumberOfOrders

This table supports category performance analysis.

🏢 Data Warehouse

The cleaned/processed data is also integrated with a Microsoft Fabric Data Warehouse.

The warehouse provides a SQL-based analytical environment for downstream reporting and business intelligence workloads.

Warehouse tables
Customers
Orders
OrderDetails
Products
Stores

The Warehouse acts as the structured analytical layer for relational querying.

📊 Power BI Analytics

The Gold layer is connected to a Power BI semantic model.

The report provides an executive-level view of supermarket performance.

Executive Overview

The dashboard contains KPIs including:

💰 Total Sales

Measures total revenue generated.

📦 Total Quantity

Shows the total number of products sold.

🏷️ Total Discount

Measures the total discount amount provided.

🧾 Total Orders

Shows the number of orders processed.

💵 Average Order Value
Average Order Value =
DIVIDE(
    [Total Sales],
    [Total Orders],
    0
)
📉 Discount Rate
Discount Rate =
DIVIDE(
    [Total Discount],
    [Gross Sales],
    0
)
📈 Dashboard Visualizations

The Power BI report includes business-focused visualizations such as:

Sales Trend Over Time

Tracks how sales change across different dates.

Sales by Category

Identifies high-performing product categories.

Top Products by Sales

Highlights products generating the most revenue.

Sales by Store

Compares sales performance across stores.

KPI Cards

Provides an executive summary of:

Total Sales
Total Quantity
Total Discount
Total Orders
Average Order Value
🔄 End-to-End Data Flow
SQL Server
    │
    ▼
Fabric Data Pipeline
    │
    ▼
Bronze Lakehouse
    │
    │ Raw CSV
    ▼
PySpark / Dataflow Gen2
    │
    ├── Remove duplicates
    ├── Trim whitespace
    ├── Handle nulls
    ├── Correct data types
    └── Validate foreign keys
    │
    ▼
Silver Lakehouse
    │
    │ Parquet
    ▼
Gold Transformation
    │
    ├── Gold_Sales
    └── Gold_Category_Sales
    │
    ├───────────────┐
    ▼               ▼
Warehouse       Power BI
    │               │
    │               ▼
    │         Semantic Model
    │               │
    └───────────────┤
                    ▼
             Business Dashboard
🛠️ Technologies Used
Technology	Purpose
Microsoft Fabric	End-to-end data platform
OneLake	Unified data storage
Lakehouse	Bronze/Silver data storage
PySpark	Data transformation
Dataflow Gen2	Low-code ETL
Data Pipeline	Data ingestion
Fabric Warehouse	SQL analytical storage
T-SQL	Warehouse querying
Power BI	Visualization and reporting
DAX	Analytical measures
GitHub	Version control
Git Integration	Fabric project source control
🔐 Data Quality & Governance

The pipeline implements basic data quality practices:

Duplicate detection
Null validation
Data type validation
Referential integrity checks
Whitespace normalization
Invalid record removal
Layered data architecture
Version control using Git
📁 Project Structure
supermarket-data-engineering-fabric/
│
├── DF_LH_TO_WH.Dataflow/
│
├── New_Warehouse.Warehouse/
│
├── PowerBi_Supermarket_Gold.Report/
│
├── PowerBi_Supermarket_Gold.SemanticModel/
│
├── SuperMarket_BrToSi_ETL.Notebook/
│
├── SupM_SilverTOGold.Notebook/
│
├── Supermarket_Raw_Data.Lakehouse/
│
├── Wh_ETL_SupermarketData.Warehouse/
│
├── copyonpremsqldatolakehouse.DataPipeline/
│
├── StagingLakehouseForDataflows/
│
├── StagingWarehouseForDataflows/
│
└── README.md
🚀 Key Learning Outcomes

This project demonstrates practical experience with:

End-to-end ETL pipeline development
Microsoft Fabric Lakehouse architecture
Medallion architecture
PySpark data engineering
Dataflow Gen2
Data Pipeline development
Data quality and validation
Parquet-based data storage
SQL Data Warehousing
Dimensional/analytical data modeling
Power BI semantic modeling
DAX measures
Business intelligence reporting
Git-based version control
Microsoft Fabric Git integration
💡 Business Value

The solution converts raw supermarket transactions into reliable analytical datasets that can support:

Sales performance monitoring
Product performance analysis
Store performance comparison
Category-level analysis
Discount analysis
Revenue trend analysis
Executive reporting
Data-driven business decisions
📌 Future Improvements

Possible future enhancements include:

Incremental data loading
Slowly Changing Dimensions (SCD)
Automated pipeline scheduling
Data quality monitoring
Error logging and retry mechanisms
Star schema implementation
Customer segmentation
Sales forecasting
Inventory analytics
Row-level security in Power BI
CI/CD using Fabric Deployment Pipelines
Automated testing
Metadata-driven pipelines
👨‍💻 Author

K Sai Snehan

🎓 B.Tech – Computer Science & Engineering

Technologies & Interests

Python • SQL • PySpark • Microsoft Fabric • Data Engineering • Power BI • Azure • ETL

⭐ Project Highlights

Built an end-to-end Microsoft Fabric data engineering platform that ingests raw SQL Server data, processes it through Bronze → Silver → Gold layers, loads analytical data into a Fabric Warehouse, and delivers business insights through Power BI.

📜 License

This project is intended for educational and portfolio purposes.


### One thing I'd change before you paste it

Your current README is very basic:

> `Microsoft Fabric end-to-end data engineering project.`

Replace it with the README above. **But don't claim anything you haven't actually implemented.** For example, the "Future Improvements" section is explicitly future work, while the main architecture describes what you've actually built.

Also, because your GitHub repository now contains the actual Fabric artifacts, this README gives a recruiter a much clearer story:

**Source → Ingestion → Bronze → ETL → Silver → Gold → Warehouse → Semantic Model → Power BI → GitHub**

That's exactly the story you want to communicate for a **Data Engineering portfolio project**.
