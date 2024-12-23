import logging
from load_data import customers, events
from tqdm import tqdm
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Calculate total revenue for each customer
customer_revenue = {}
for event in tqdm(events, desc="Processing events"):
    customer_id = event['CustomerID']
    revenue = event['Quantity'] * event['Price']
    if customer_id in customer_revenue:
        customer_revenue[customer_id] += revenue
    else:
        customer_revenue[customer_id] = revenue

# Print 10 random entries from the customer_revenue map
import random
sample_entries = random.sample(list(customer_revenue.items()), 10)
for entry in sample_entries:
    logging.info(f"CustomerID: {entry[0]}, Revenue: {entry[1]}")

# Determine top customers based on quantile
quantile = 0.025
sorted_revenue = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)
top_customers_count = int(len(sorted_revenue) * quantile)
top_customers = sorted_revenue[:top_customers_count]

logging.info(f"Number of top customers: {len(top_customers)}")

# Analyze distribution of customers by revenue
quantile_distribution = {}
quantile_size = int(len(sorted_revenue) * quantile)
for i in range(0, len(sorted_revenue), quantile_size):
    quantile_range = sorted_revenue[i:i + quantile_size]
    if quantile_range:
        max_revenue = quantile_range[0][1]
        min_revenue = quantile_range[-1][1]
        quantile_distribution[i // quantile_size] = {
            'count': len(quantile_range),
            'max_revenue': max_revenue,
            'min_revenue': min_revenue
        }

for quantile, data in quantile_distribution.items():
    logging.info(f"Quantile: {quantile}, Count: {data['count']}, Max Revenue: {data['max_revenue']}, Min Revenue: {data['min_revenue']}")