# Superstore Sales & Profit Performance Analysis

##  Project Overview
This project analyzes retail sales data from the **Superstore** dataset using **Python** and **SQL (SQLite)**. The goal is to uncover key business insights regarding overall revenue, category profitability, customer performance, and regional sales.

---

##  Tech Stack & Tools
* **Python**: Data loading and converting CSV data into a SQLite database (`pandas`, `sqlite3`).
* **SQL (SQLite)**: Data aggregation, filtering, and metric calculations.
* **VS Code**: Development environment.

---

##  Project Structure
  ''' text
├── Superstore.csv      # Raw dataset
├── convert.py          # Python script to convert CSV to SQLite DB
├── superstore.db       # SQLite Database
├── analysis.sql        # SQL queries for exploratory data analysis
└── README.md           # Project documentation

##  Key Business Insights & Recommendations

* **High-Margin Categories:** Technology products yield the highest profit margins. Marketing efforts should prioritize this category.
* **Furniture Margin Issue:** While Furniture generates high sales, its profit margin is low due to heavy discounting. Re-evaluating discount strategies is recommended.
* **Regional Optimization:** The Central region underperforms in total profit compared to West and East. Shipping costs and localized pricing should be audited.
* **Customer Retention:** A small segment of top customers drives a significant portion of profits. Introducing a VIP retention program is advised.
