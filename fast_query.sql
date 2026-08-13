-- fast_query.sql

-- 1. Apply Performance Optimizations
-- Index for foreign key join acceleration
CREATE INDEX idx_sales_user_id ON sales_history(user_id); 

-- Composite index for the target date boundaries
CREATE INDEX idx_sales_date ON sales_history(sale_date);

-- Index on user filtering criteria
CREATE INDEX idx_users_region ON users(user_region);

-- 2. Execute the Refactored Query
EXPLAIN ANALYZE
SELECT SUM(s.revenue) AS total_revenue
FROM sales_history s
JOIN users u ON s.user_id = u.user_id
WHERE s.sale_date >= '2025-10-01 00:00:00' 
  AND s.sale_date < '2026-01-01 00:00:00'
  AND u.user_region = 'Europe';
