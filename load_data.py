import mysql.connector
import os
from dotenv import load_dotenv
import logging

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

cursor = db.cursor(dictionary=True)

# Load customer data
def load_customer_data():
    query = """
    SELECT CustomerID, Email
    FROM Customer
    """
    cursor.execute(query)
    customers = cursor.fetchall()
    return customers

# Load event data without joins
def load_event_data():
    query = """
    SELECT EventID, CustomerID, ContentID, Quantity, EventDate
    FROM CustomerEventData
    WHERE EventTypeID = 6 AND EventDate >= '2020-04-01'
    """
    cursor.execute(query)
    events = cursor.fetchall()

    # Load content prices separately
    content_prices = {}
    cursor.execute("SELECT ContentID, Price FROM ContentPrice")
    for row in cursor.fetchall():
        content_prices[row['ContentID']] = row['Price']

    # Add prices to events
    for event in events:
        event['Price'] = content_prices.get(event['ContentID'], 0)

    return events

customers = load_customer_data()
events = load_event_data()

logging.info(f"Loaded {len(customers)} customers")
logging.info(f"Loaded {len(events)} events")

cursor.close()
db.close()