# SQL Query Performance Optimization Sandbox

An educational project showcasing database performance engineering on a dataset of 1 million transaction logs using PostgreSQL.

# Performance Metrics Summary
* **Unoptimized Execution Time:** ~450ms - 1,200ms (Varies by hardware)
* **Optimized Execution Time:** ~12ms - 18ms
* **Performance Improvement:** **~97% decrease in query latency**

# Why the Slow Query Failed
1. **Sequential Table Scans:** Without indexes on `user_id` and `user_region`, the query planner was forced to scan every row sequentially from disk.
2. **Non-Sargable Functions:** Using `EXTRACT(YEAR FROM sale_date)` prevents the database engine from executing simple boundary lookups, rendering standard chronological data sorting useless.
3. **Expensive Text Search:** Utilizing `LOWER(region) LIKE '%europe%'` triggers full text scans instead of strict categorical pointer matches.

# Applied Solutions
1. **Data Range Filtering:** Swapped the mathematical row extractions for precise logical range evaluations (`>= '2025-10-01'`).
2. **Composite Indexing Strategy:** Implemented highly targeted B-Tree indexes on database foreign keys and filter fields.
