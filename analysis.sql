-- SUPERSTORE SALES ANALYSIS (SQL PORTFOLIO PROJECT)
-- ================================================

-- 1. Total Business Key Metrics (KPIs)
SELECT 
    COUNT(DISTINCT "Order ID") AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales;


-- 2. Performance by Product Category
SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS profit_margin_percent
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;


-- 3. Top 5 Sub-Categories by Sales
SELECT 
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY "Sub-Category"
ORDER BY total_sales DESC
LIMIT 5;


-- 4. Top 10 Most Profitable Customers
SELECT 
    "Customer Name",
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY "Customer Name"
ORDER BY total_profit DESC
LIMIT 10;


-- 5. Sales & Profit Performance by Region
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Region
ORDER BY total_profit DESC;