-- schema.sql

-- Drop tables if they already exist to ensure a clean slate
DROP TABLE IF EXISTS sales_history;
DROP TABLE IF EXISTS users;

-- 1. Create Users Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    user_email VARCHAR(100),
    user_region VARCHAR(50)  -- e.g., 'North America', 'Europe', 'Asia'
);

-- 2. Create Sales History Table (Deliberately unindexed on search columns)
CREATE TABLE sales_history (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT,
    sale_date TIMESTAMP,
    revenue NUMERIC(10, 2),
    product_category VARCHAR(50),
    payment_method VARCHAR(30)
);
