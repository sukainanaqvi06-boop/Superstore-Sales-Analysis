CREATE DATABASE IF NOT EXISTS superstore_project;
USE superstore_project;

USE superstore_project;
SELECT COUNT(*) FROM superstore_data;

--- 1. which region has the highest sales
SELECT region, SUM(sales) AS Total_Sales
FROM superstore_data
GROUP BY region 
ORDER BY Total_Sales DESC;

-- --- 2. which category has sells the most 
SELECT category, SUM(sales) AS Total_Sales
FROM superstore_data
GROUP BY category 
ORDER BY Total_Sales DESC;

-- --- 3. which product sells the most
SELECT `Product Name` , SUM(sales) AS Total_Sales
FROM superstore_data
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 5;

-- --- 4. which month has the highest order
SELECT MONTH(`Order Date`)AS months,
count(`Order Id`) AS Total_order
FROM superstore_data
GROUP BY MONTH(`Order Date`)
ORDER BY Total_Order DESC;
