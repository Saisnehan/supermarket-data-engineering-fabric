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
