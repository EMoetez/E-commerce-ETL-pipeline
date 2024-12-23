import mysql.connector
import os
from dotenv import load_dotenv
from compute import top_customers, customers
import logging
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a connection to the database
db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = db.cursor()

# Create export table
date_str = datetime.now().strftime('%Y%m%d')
table_name = f"test_export_{date_str}_mass_insert"
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    CustomerID BIGINT NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Revenue DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (CustomerID)
)
"""
cursor.execute(create_table_query)

# Prepare data for mass insert
data_to_insert = []
for customer_id, revenue in top_customers:
    email = next(customer['Email'] for customer in customers if customer['CustomerID'] == customer_id)
    data_to_insert.append((customer_id, email, revenue))

# Insert top customers into export table using mass insert
insert_query = f"""
INSERT INTO {table_name} (CustomerID, Email, Revenue)
VALUES (%s, %s, %s)
ON DUPLICATE KEY UPDATE Revenue = VALUES(Revenue)
"""
cursor.executemany(insert_query, data_to_insert)

db.commit()
cursor.close()
db.close()

logging.info("Top customers exported successfully!")