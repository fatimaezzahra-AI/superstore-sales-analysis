# Superstore Business Intelligence & ML Dashboard

## Project Overview
This project is an end-to-end Data Analytics and Machine Learning web application built for the Superstore dataset. It integrates SQL, Python, interactive visual data exploration, and a Random Forest Machine Learning model into a unified Streamlit dashboard.

The application enables business stakeholders to evaluate profitability, track sales performance, examine discount-profit correlations, and predict estimated margins for upcoming deals in real time.

---

## Key Features

* **Interactive KPIs**: Dynamic tracking of Total Sales, Total Profit, Average Discount, and Total Order Volume.
* **Global Filters**: Real-time multi-attribute filtering across regions and product categories.
* **Statistical Analysis**:
  * **Correlation Matrix**: Quantifies mathematical relationships between core variables.
  * **OLS Trendline Regression**: Visualizes price elasticity and discount impact on margins.
* **Machine Learning Profit Simulator**:
  * Trained on a Random Forest Regressor algorithm with live performance metrics (R² score and Mean Absolute Error).
  * Interactive input panel allowing users to simulate deal scenarios and estimate profit or loss.
* **Categorical Segmentation**: Aggregated sales and profit distributions structured via Plotly chart components.
* **Custom UI Architecture**: Clean HTML/CSS integration designed for structured presentation and readability.

---

## Tech Stack & Dependencies

* **Dashboard Framework**: Streamlit, Custom HTML/CSS
* **Data Visualization**: Plotly Express
* **Machine Learning & Analytics**: Scikit-Learn, Statsmodels, NumPy
* **Data Processing**: Pandas
* **Database**: SQLite (sqlite3)
* **Development Environment**: VS Code, Git

---

## Repository Structure

```text
├── Superstore.csv       # Raw dataset
├── convert.py           # ETL script converting CSV records into SQLite DB
├── superstore.db        # Relational database storing sales data
├── analysis.sql         # SQL queries for exploratory data analysis
├── app.py               # Main application entry point and ML pipeline
└── README.md            # Technical documentation
