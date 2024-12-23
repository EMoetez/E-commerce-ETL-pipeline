import mysql.connector
import random
from faker import Faker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

# Create a connection to the database
db = mysql.connector.connect(
    host=host,        # MySQL host name
    user=user,        # MySQL username
    password=password,  # MySQL password
    database=database   # database name
)

cursor = db.cursor()
faker = Faker()

# Predefined channel types and event types
channel_types = {
    1: 'Email',
    2: 'PhoneNumber',
    3: 'Postal',
    4: 'MobileID',
    5: 'Cookie'
}

event_types = {
    1: 'sent',
    2: 'view',
    3: 'click',
    4: 'visit',
    5: 'cart',
    6: 'purchase'
}

# # Insert predefined channel types
# for channel_type_id, channel_name in channel_types.items():
#     sql_channel_type = """
#     INSERT INTO ChannelType (ChannelTypeID, Name)
#     VALUES (%s, %s)
#     ON DUPLICATE KEY UPDATE Name = VALUES(Name);
#     """
#     cursor.execute(sql_channel_type, (channel_type_id, channel_name))

# # Insert predefined event types
# for event_type_id, event_name in event_types.items():
#     sql_event_type = """
#     INSERT INTO EventType (EventTypeID, Name)
#     VALUES (%s, %s)
#     ON DUPLICATE KEY UPDATE Name = VALUES(Name);
#     """
#     cursor.execute(sql_event_type, (event_type_id, event_name))

# Insert random content data
content_ids = []
for _ in range(100):  # Insert 100 sample rows
    sql_content = """
    INSERT INTO Content (ClientContentID, InsertDate)
    VALUES (%s, NOW());
    """
    client_content_id = random.randint(1000, 9999)
    cursor.execute(sql_content, (client_content_id,))
    content_id = cursor.lastrowid
    content_ids.append(content_id)

    sql_content_price = """
    INSERT INTO ContentPrice (ContentID, Price, Currency, InsertDate)
    VALUES (%s, %s, %s, NOW());
    """
    price = round(random.uniform(10.0, 100.0), 2)
    currency = 'USD'
    cursor.execute(sql_content_price, (content_id, price, currency))

# Insert random customer data
for _ in range(1000):  # Insert 1000 sample rows
    sql_customer = """
    INSERT INTO Customer (ClientCustomerID, Email, InsertDate)
    VALUES (%s, %s, NOW());
    """
    client_customer_id = random.randint(1000, 9999)
    email = faker.email()
    cursor.execute(sql_customer, (client_customer_id, email))
    customer_id = cursor.lastrowid

    channel_type_id = random.choice(list(channel_types.keys()))
    if channel_type_id == 1:
        channel_value = email
    elif channel_type_id == 2:
        channel_value = faker.phone_number()
    elif channel_type_id == 3:
        channel_value = faker.address()
    elif channel_type_id == 4:
        channel_value = faker.uuid4()
    elif channel_type_id == 5:
        channel_value = faker.md5()

    sql_customer_data = """
    INSERT INTO CustomerData (CustomerID, ChannelTypeID, ChannelValue, InsertDate)
    VALUES (%s, %s, %s, NOW());
    """
    cursor.execute(sql_customer_data, (customer_id, channel_type_id, channel_value))

    sql_customer_event = """
    INSERT INTO CustomerEvent (ClientEventID, InsertDate)
    VALUES (%s, NOW());
    """
    client_event_id = random.randint(1000, 9999)
    cursor.execute(sql_customer_event, (client_event_id,))
    event_id = cursor.lastrowid

    event_type_id = random.choice(list(event_types.keys()))
    content_id = random.choice(content_ids)  # Use existing content IDs
    quantity = random.randint(1, 10)

    sql_customer_event_data = """
    INSERT INTO CustomerEventData (EventID, ContentID, CustomerID, EventTypeID, EventDate, Quantity, InsertDate)
    VALUES (%s, %s, %s, %s, NOW(), %s, NOW());
    """
    cursor.execute(sql_customer_event_data, (event_id, content_id, customer_id, event_type_id, quantity))

db.commit()
cursor.close()
db.close()

print("Data inserted successfully!")