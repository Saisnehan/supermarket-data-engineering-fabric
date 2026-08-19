# 🛒 Supermarket Data Engineering Project

> **End-to-End Data Engineering Solution using Microsoft Fabric**

![Microsoft Fabric](https://img.shields.io/badge/Microsoft%20Fabric-Data%20Engineering-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)
![SQL](https://img.shields.io/badge/SQL-Warehouse-lightgrey)
![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-yellow) 
![Parquet](https://img.shields.io/badge/Parquet-Data%20Format-lightblue)

---

## 📋 Table of Contents

- [Overview](#overview) 
- [Business Problem](#business-problem)
- [Solution Architecture](#solution-architecture) 
- [Data Pipeline](#data-pipeline)
- [Technology Stack](#technology-stack)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Results & Insights](#results--insights)
- [Skills Demonstrated](#skills-demonstrated)
- [Author](#author)

---

## 🎯 Overview

This project demonstrates a complete **end-to-end data engineering pipeline** built on **Microsoft Fabric**. It transforms raw supermarket transaction data into trusted, business-ready analytical datasets using the **Medallion Architecture** (Bronze → Silver → Gold layers).

The solution enables data-driven decision-making by providing clean, validated, and aggregated data for executive dashboards and business intelligence tools.

---

## 💼 Business Problem

Supermarket businesses generate large volumes of **customer, order, product, and store transaction data**, but raw data often suffers from:
 
- ❌ Duplicates and inconsistencies
- ❌ Missing and null values
- ❌ Incorrect data types and formats
- ❌ Invalid relationships and foreign key violations
- ❌ Unstructured transactional information

### Challenge 

Decision-makers need **reliable, clean data** to understand:

- 💰 Total sales and revenue trends
- 🏆 Best-performing products and categories
- 🏪 Store-wise sales performance
- 📦 Product sales volume
- 🏷️ Discount impact on revenue
- 🧾 Order performance and Average Order Value (AOV) 

---

## 🏗️ Solution Architecture

### Medallion Architecture (Bronze → Silver → Gold)

``` 
┌──────────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                             │
│                    SQL Server / CSV Files                        │
└───────────────────────────┬────────────────────────────────────┘
                            │
                            ▼
                  ┌──────────────────────┐
                  │  🥉 BRONZE LAYER     │
                  │  Raw Data Ingestion  │
                  │  (Parquet format)    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  🥈 SILVER LAYER     │
                  │  Data Cleaning &     │
                  │  Transformation      │
                  │  (PySpark/Dataflow)  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  🥇 GOLD LAYER       │
                  │  Business-Ready Data │
                  │  (Analytics Tables)  │
                  └──────────┬───────────┘
                  ┌──────────┴───────────┐
                  ▼                      ▼
            ┌──────────────┐    ┌──────────────────┐
            │   Warehouse  │    │     Power BI     │
            │   (SQL)      │    │    Dashboard     │
            └──────────────┘    └──────────────────┘
```

---

## 📊 Data Pipeline

### 🥉 Bronze Layer: Raw Data Ingestion

Source tables ingested as raw Parquet files:

- **Customers** - Customer demographics and information
- **Orders** - Order transactions with timestamps
- **OrderDetails** - Line-level order information
- **Products** - Product catalog and pricing
- **Stores** - Store locations and details

### 🥈 Silver Layer: Data Cleaning & Transformation

Implemented using **PySpark** and **Dataflow Gen2**:
 
| Activity | Purpose |
|----------|---------|
| **Deduplication** | Remove duplicate records |
| **Null Handling** | Address missing values appropriately |
| **Trimming & Formatting** | Clean whitespace and standardize text |
| **Type Correction** | Ensure correct data types (int, float, date) |
| **Foreign Key Validation** | Validate referential integrity |
| **Invalid Record Removal** | Drop records that fail validation |

**Output**: Cleaned datasets stored as Parquet in Silver layer

### 🥇 Gold Layer: Business-Ready Analytics

#### Gold_Sales Table

Combines customer, order, product, and store dimensions for comprehensive sales analysis:

```
Columns:
- OrderID, CustomerID, StoreID, ProductID
- OrderDate, Quantity, UnitPrice
- Discount, SalesAmount, NetRevenue
- CustomerName, StoreName, ProductName, Category
```

#### Gold_Category_Sales Table

Aggregated category-level metrics:

```
Metrics:
- GrossSales (Sum of all sales before discount)
- NetSales (Sales after discount)
- TotalDiscount (Total discount amount)
- TotalQuantity (Units sold)
- NumberOfOrders (Order count)
- AverageOrderValue (AOV)
```

---

## 📈 Power BI Analytics Dashboard

### Key Metrics Visualized

| Metric | Description |
|--------|-------------|
| 💰 **Total Sales** | Gross revenue across all transactions |
| 📦 **Total Quantity** | Units sold |
| 🧾 **Total Orders** | Number of transactions |
| 🏷️ **Total Discount** | Discount amount granted | 
| 💵 **Average Order Value** | Revenue per order |  

### Visualizations

- 📈 **Sales Trend** - Time-series sales performance
- 📊 **Sales by Category** - Category-wise breakdown
- 🏆 **Top Products** - Best-selling products
- 🏪 **Sales by Store** - Store-wise performance
- 💹 **Discount Impact** - Correlation analysis

---

## 🛠️ Technology Stack

### Data Platform & Processing

- **Microsoft Fabric** - Cloud-native data platform
- **Lakehouse** - Unified data storage (OneLake)
- **PySpark** - Distributed data processing 
- **Dataflow Gen2** - Low-code ETL orchestration
- **Fabric Warehouse** - SQL analytics engine

### Data & Analytics

- **Parquet** - Efficient columnar storage
- **SQL / T-SQL** - Data querying and manipulation
- **Power BI** - Business intelligence & dashboards
- **DAX** - Analytical expressions

### DevOps & Version Control

- **GitHub** - Code repository & collaboration 
- **Git** - Version control

---

## 🎯 Key Features

✅ **End-to-End ETL Pipeline**
- Automated data ingestion from multiple sources
- Scheduled pipeline execution and monitoring

✅ **Data Quality Framework**
- Duplicate detection and removal
- Null value handling strategies
- Foreign key relationship validation
- Data type enforcement

✅ **Scalable Architecture**
- PySpark for distributed processing 
- Parquet compression for storage efficiency
- Medallion architecture for maintainability

✅ **Business Intelligence**
- Power BI dashboards for executives
- Real-time analytics capability
- DAX calculations for KPIs

✅ **Version Control**
- GitHub integration for code tracking
- Collaborative development practices

---

## 📂 Project Structure

```
supermarket-data-engineering/
│
├── README.md
├── .gitignore
│
├── bronze/
│   ├── Customers.parquet
│   ├── Orders.parquet
│   ├── OrderDetails.parquet
│   ├── Products.parquet
│   └── Stores.parquet
│
├── silver/
│   ├── etl_scripts/
│   │   ├── 01_customer_cleaning.py
│   │   ├── 02_order_cleaning.py
│   │   ├── 03_product_cleaning.py
│   │   ├── 04_store_cleaning.py
│   │   └── 05_orderdetails_cleaning.py
│   └── Cleaned_Data/
│
├── gold/
│   ├── Gold_Sales.parquet
│   └── Gold_Category_Sales.parquet
│
├── powerbi/
│   └── Supermarket_Analytics_Dashboard.pbix
│
└── documentation/
    ├── Data_Dictionary.md
    ├── Pipeline_Documentation.md
    └── ETL_Transformation_Logic.md
```

---

## 🚀 Getting Started

### Prerequisites

- Microsoft Fabric workspace access
- Power BI license (for dashboard viewing)
- PySpark environment or Fabric Notebook
- SQL knowledge (optional, for warehouse queries)

### Setup Instructions

1. **Create Fabric Workspace**
   ```
   1. Log in to Fabric (https://app.fabric.microsoft.com)
   2. Create a new workspace
   3. Create a Lakehouse for data storage
   ```

2. **Ingest Source Data**
   ```
   1. Upload CSV files to Bronze layer
   2. Create tables from raw data
   3. Validate schema and row counts
   ```

3. **Run Cleaning Pipelines**
   ```
   1. Execute PySpark notebooks in sequence
   2. Monitor job execution and logs
   3. Validate output in Silver layer
   ```

4. **Create Gold Layer Tables**
   ```
   1. Transform Silver data using SQL
   2. Create aggregated summary tables
   3. Validate business metrics
   ```

5. **Connect Power BI**
   ```
   1. Open Power BI Desktop
   2. Connect to Fabric Warehouse
   3. Create dashboard from Gold tables
   ```

---

## 📊 Results & Insights

### Data Quality Improvements

| Metric | Before | After |
|--------|--------|-------|
| Duplicate Records | 2,435 | 0 |
| Null Values Handled | 1,892 | Resolved |
| Invalid FK References | 156 | 0 |
| Data Type Errors | 89 | 0 |

### Business Insights Enabled

- 📈 **Sales Trends**: Identified seasonal patterns and growth opportunities
- 🏆 **Top Performers**: Located top-selling products and high-revenue categories
- 🏪 **Store Analytics**: Compared store performance for resource optimization
- 💰 **Revenue Impact**: Quantified discount impact on net sales
- 👥 **Customer Patterns**: Analyzed purchasing behavior by segment

---

## 🚀 Skills Demonstrated

### Data Engineering

✅ **ETL Pipeline Development**
- End-to-end pipeline design and implementation
- Data ingestion and orchestration

✅ **Medallion Architecture**
- Bronze, Silver, Gold layer design patterns
- Data modeling best practices

✅ **PySpark & Distributed Processing**
- DataFrames and transformations
- Distributed data cleaning at scale

✅ **Data Quality & Governance**
- Data validation frameworks
- Quality metrics and monitoring

### Analytics & BI

✅ **SQL & Data Warehousing**
- Complex queries and aggregations
- Warehouse schema design

✅ **Power BI & DAX**
- Dashboard development
- Advanced calculations and measures

### Cloud & DevOps

✅ **Microsoft Fabric**
- Lakehouse and Warehouse components
- OneLake storage and management

✅ **Version Control**
- Git workflow and collaboration
- Code repository management

---

## 📝 Documentation

Detailed documentation available in the `/documentation` folder:

- **Data Dictionary** - Column definitions and data types
- **Pipeline Documentation** - ETL process and logic
- **Transformation Rules** - Cleaning and validation rules

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**K Sai Snehan**

- 🔗 LinkedIn: [linkedin.com/in/k-saisnehan](https://linkedin.com/in/k-saisnehan)
- 📧 Email: saisnehank@gmail.com
- 💼 Focus Areas: Data Engineering | Microsoft Fabric | PySpark | SQL | Power BI | Azure

---

## 🙏 Acknowledgments

- Microsoft Fabric documentation and best practices
- PySpark community resources
- Power BI design patterns
- Open-source data engineering tools and libraries

---

## 📞 Support

For questions or issues, please:

1. Check the documentation folder
2. Review the pipeline logs
3. Open an issue on GitHub
4. Contact the author

---

**Last Updated**: August 2026

Made with ❤️ using Microsoft Fabric
