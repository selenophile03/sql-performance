# generate_data.py
import psycopg2
import random
from datetime import datetime, timedelta

# Database configuration - Update these details with your local PostgreSQL credentials
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "yourpassword",
    "host": "localhost",
    "port": "5432"
}

def seed_database():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    print("Connected to database. Seeding data...")

    # 1. Insert 10,000 Users
    regions = ['North America', 'Europe', 'Asia', 'South America', 'Australia']
    user_data = []
    for i in range(1, 10001):
        username = f"user_{i}"
        email = f"user_{i}@example.com"
        region = random.choice(regions)
        user_data.append((username, email, region))
    
    cur.executemany("INSERT INTO users (username, user_email, user_region) VALUES (%s, %s, %s);", user_data)
    print("Successfully inserted 10,000 users.")

    # 2. Insert 1,000,000 Sales Records in Batches
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Beauty']
    payments = ['Credit Card', 'PayPal', 'Crypto', 'Bank Transfer']
    start_date = datetime(2024, 1, 1)
    
    batch_size = 50000
    total_rows = 1000000
    
    for batch in range(0, total_rows, batch_size):
        sales_batch = []
        for _ in range(batch_size):
            user_id = random.randint(1, 10000)
            # Random date spanning 2024 to early 2026
            random_days = random.randint(0, 800)
            sale_date = start_date + timedelta(days=random_days, hours=random.randint(0, 23))
            revenue = round(random.uniform(5.00, 1500.00), 2)
            category = random.choice(categories)
            payment = random.choice(payments)
            
            sales_batch.append((user_id, sale_date, revenue, category, payment))
            
        cur.executemany(
            "INSERT INTO sales_history (user_id, sale_date, revenue, product_category, payment_method) VALUES (%s, %s, %s, %s, %s);", 
            sales_batch
        )
        print(f"Inserted rows {batch + batch_size}/{total_rows}")

    conn.commit()
    cur.close()
    conn.close()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
