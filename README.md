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

The project demonstrates how raw supermarket transactional data can be ingested into a Microsoft Fabric Lakehouse, transformed through **Bronze → Silver → Gold layers**, loaded into a **Fabric Data Warehouse**, and finally consumed through a **Power BI Semantic Model and interactive business dashboard**.

The solution follows a modern **Medallion Architecture** to improve data quality, maintainability, scalability, and analytical performance.

---
# 🎯 Business Problem

Supermarket businesses generate large amounts of transactional data from customers, stores, products, and orders.

However, raw transactional data is not immediately suitable for analytics because it may contain:

- Duplicate records
- Missing values
- Invalid foreign keys
- Inconsistent text formatting
- Incorrect data types
- Raw transactional structures

This project builds a complete data engineering pipeline that transforms raw supermarket data into a **trusted analytical data platform**.

The final solution enables business users to answer questions such as:

- 💰 What are the total sales?
- 🛍️ Which products generate the highest revenue?
- 📊 Which categories perform best?
- 🏪 Which stores generate the most sales?
- 📈 How are sales changing over time?
- 💵 What is the average order value?
- 🏷️ How much discount is being given?
- 📦 Which products have the highest sales volume?

---
# 🗂️ Source Data

The project uses five major source datasets:

| Dataset | Description |
|---|---|
| `Customers` | Customer information |
| `Orders` | Order-level transaction information |
| `OrderDetails` | Product-level order details |
| `Products` | Product and category information |
| `Stores` | Store information |

### Source Data Format

The raw source data is provided as **CSV files** and stored in the Bronze layer of the Microsoft Fabric Lakehouse.

### Source Files

```text
Bronze_Supermarket_data/
│
├── Customers.csv
├── Orders.csv
├── OrderDetails.csv
├── Products.csv
└── Stores.csv

---

# PART 5 — 🏗️ Architecture

This is the section corresponding to the **Architecture** heading and large diagram shown in your screenshot.

```markdown
# 🏗️ Architecture

```text
                    ┌──────────────────────────┐
                    │      Source Data         │
                    │                          │
                    │      CSV Files            │
                    │                          │
                    │ Customers.csv             │
                    │ Orders.csv                │
                    │ OrderDetails.csv          │
                    │ Products.csv              │
                    │ Stores.csv                │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │       BRONZE LAYER       │
                    │                          │
                    │   Fabric Lakehouse       │
                    │                          │
                    │   Raw Source Data        │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │       SILVER LAYER       │
                    │                          │
                    │   PySpark / Dataflow     │
                    │                          │
                    │ • Remove duplicates      │
                    │ • Trim whitespace        │
                    │ • Handle null values     │
                    │ • Correct data types     │
                    │ • Validate foreign keys  │
                    │ • Remove invalid rows    │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │        GOLD LAYER        │
                    │                          │
                    │   Business-Ready Data   │
                    │                          │
                    │   Gold_Sales              │
                    │   Gold_Category_Sales     │
                    └─────────────┬────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
          ┌───────────────────┐       ┌────────────────────┐
          │ Fabric Warehouse  │       │ Power BI Semantic  │
          │                   │       │ Model              │
          │ SQL Analytics     │       │                    │
          └───────────────────┘       └──────────┬─────────┘
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

     
---

## PART 7 — 🥈 Silver Layer

```markdown
# 🥈 Silver Layer

The Silver layer contains cleaned and validated data.

ETL transformations were implemented using **PySpark** and **Dataflow Gen2**.

## 🔄 Data Quality Transformations

### 1. Duplicate Removal

Duplicate records were identified and removed using business keys such as:

```text
CustomerID
OrderID
OrderDetailID
ProductID
StoreID         


---

## PART 8 — 🥈 Silver Data Storage

```markdown
# 🥈 Silver Data Storage

After transformation, the cleaned datasets are stored in the Lakehouse as **Parquet** files.

```text
Silver_ETL_performed/
│
├── Customers/
├── Orders/
├── OrderDetails/
├── Products/
└── Stores/


---

## PART 9 — 🥇 Gold Layer

```markdown
# 🥇 Gold Layer

The Gold layer contains business-ready datasets designed for analytics and reporting.

## 📊 Gold_Sales

`Gold_Sales` is a denormalized analytical dataset combining information from:

- Customers
- Orders
- OrderDetails
- Products
- Stores

### Example Attributes

```text
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


---

## PART 10 — 🏢 Fabric Data Warehouse

```markdown
# 🏢 Fabric Data Warehouse

The cleaned and processed data is also integrated with a **Microsoft Fabric Data Warehouse**.

The Warehouse provides a structured SQL-based analytical environment for downstream reporting and business intelligence workloads.

### Warehouse Tables

```text
Customers
Orders
OrderDetails
Products
Stores


---

## PART 11 — 📊 Power BI Analytics

```markdown
# 📊 Power BI Analytics

The Gold layer is connected to a **Power BI Semantic Model**.

The Power BI report provides an executive-level view of supermarket performance.

## 📌 Executive Overview

The dashboard contains KPIs including:

### 💰 Total Sales

Measures the total net sales generated.

### 📦 Total Quantity

Shows the total number of products sold.

### 🏷️ Total Discount

Measures the total discount amount provided.

### 🧾 Total Orders

Shows the number of orders processed.

### 💵 Average Order Value

```DAX
Average Order Value =
DIVIDE(
    [Total Sales],
    [Total Orders],
    0
)


---

## PART 12 — 📈 Dashboard Visualizations

```markdown
# 📈 Dashboard Visualizations

The Power BI report includes business-focused visualizations such as:

### 📈 Sales Trend Over Time

Tracks how sales change across different dates.

### 📊 Sales by Category

Identifies high-performing product categories.

### 🏆 Top Products by Sales

Highlights products generating the most revenue.

### 🏪 Sales by Store

Compares sales performance across stores.

### 📌 KPI Cards

Provides an executive summary of:

```text
Total Sales
Total Quantity
Total Discount
Total Orders
Average Order Value



---

## PART 13 — 🔄 End-to-End Data Flow

```markdown
# 🔄 End-to-End Data Flow

```text
CSV Source Files
       │
       ▼
Fabric Data Pipeline
       │
       ▼
🥉 Bronze Lakehouse
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
🥈 Silver Lakehouse
       │
       │ Parquet
       ▼
Gold Transformation
       │
       ├── Gold_Sales
       └── Gold_Category_Sales
       │
       ├──────────────────┐
       ▼                  ▼
Fabric Warehouse      Power BI
                          │
                          ▼
                  Semantic Model
                          │
                          ▼
                  Business Dashboard


---

## PART 14 — 🛠️ Technologies Used

```markdown
# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Microsoft Fabric** | End-to-end data engineering platform |
| **OneLake** | Unified data storage |
| **Lakehouse** | Bronze and Silver data storage |
| **PySpark** | Data transformation and ETL |
| **Dataflow Gen2** | Low-code ETL |
| **Data Pipeline** | Data ingestion and orchestration |
| **Fabric Warehouse** | SQL analytical storage |
| **T-SQL** | Warehouse querying |
| **Power BI** | Visualization and reporting |
| **DAX** | Analytical measures |
| **Parquet** | Columnar data storage |
| **GitHub** | Version control |
| **Fabric Git Integration** | Source control for Fabric artifacts |

---

# 🔐 Data Quality & Governance

The pipeline implements several data quality practices:

- ✅ Duplicate detection and removal
- ✅ Null validation
- ✅ Data type validation
- ✅ Referential integrity checks
- ✅ Whitespace normalization
- ✅ Invalid record removal
- ✅ Layered data architecture
- ✅ Parquet-based storage
- ✅ Git-based version control

---
# 📁 Project Structure

```text
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


---

## PART 17 — 🚀 Key Learning Outcomes

```markdown
# 🚀 Key Learning Outcomes

This project demonstrates practical experience with:

- End-to-end ETL pipeline development
- Microsoft Fabric Lakehouse architecture
- Medallion Architecture
- PySpark data engineering
- Dataflow Gen2
- Data Pipeline development
- Data quality and validation
- Parquet-based data storage
- SQL Data Warehousing
- Analytical data modeling
- Power BI Semantic Modeling
- DAX measures
- Business intelligence reporting
- Git-based version control
- Microsoft Fabric Git Integration

---
# 💡 Business Value

The solution converts raw supermarket transactions into reliable analytical datasets that can support:

- 📈 Sales performance monitoring
- 🛍️ Product performance analysis
- 🏪 Store performance comparison
- 📊 Category-level analysis
- 🏷️ Discount analysis
- 📅 Revenue trend analysis
- 💰 Executive reporting
- 🎯 Data-driven business decisions

---
