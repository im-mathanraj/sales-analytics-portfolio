-- SQLite analysis. analyze.py imports the CSV and executes these queries.
-- 1. Overall performance
SELECT COUNT(DISTINCT order_id) AS orders, SUM(revenue) AS revenue,
 SUM(profit) AS gross_profit,
 ROUND(100.0*SUM(profit)/NULLIF(SUM(revenue),0),2) AS gross_margin_pct
FROM sales;

-- 2. Category contribution: margin is a weighted ratio, not average row margin.
SELECT category, SUM(revenue) AS revenue, SUM(profit) AS gross_profit,
 ROUND(100.0*SUM(profit)/NULLIF(SUM(revenue),0),2) AS margin_pct
FROM sales GROUP BY category ORDER BY gross_profit DESC;

-- 3. Region comparison
SELECT region, COUNT(*) AS orders, SUM(revenue) AS revenue,
 SUM(profit) AS gross_profit
FROM sales GROUP BY region ORDER BY revenue DESC;

-- 4. Month-over-month revenue. First month has no previous comparison.
WITH monthly AS (
 SELECT SUBSTR(order_date,1,7) AS month,SUM(revenue) AS revenue
 FROM sales GROUP BY SUBSTR(order_date,1,7)
), comparison AS (
 SELECT month,revenue,LAG(revenue) OVER(ORDER BY month) AS previous_revenue
 FROM monthly
)
SELECT month,revenue,
 ROUND(100.0*(revenue-previous_revenue)/NULLIF(previous_revenue,0),2) AS growth_pct
FROM comparison ORDER BY month;
