-- slow_query.sql
-- Goal: Calculate total Q4 2025 revenue from users located in Europe.

EXPLAIN ANALYZE
SELECT SUM(s.revenue) AS total_revenue
FROM sales_history s
JOIN users u ON s.user_id = u.user_id
WHERE EXTRACT(YEAR FROM s.sale_date) = 2025 
  AND EXTRACT(MONTH FROM s.sale_date) IN (10, 11, 12)
  AND LOWER(u.user_region) LIKE '%europe%';
