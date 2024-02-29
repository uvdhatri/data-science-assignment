python code for 9 questions.
# Sample data for reference
# You should replace these with your actual data
# customer_id, product_count
customer_products_purchased = {
    1: 5,
    2: 3,
    # Add more customer data here
}

# Sample data for reference
# You should replace these with your actual data
# customer_id, total_purchase_value
customer_total_purchase = {
    1: 120.50,
    2: 75.20,
    # Add more customer data here
}

# Sample data for reference
# You should replace these with your actual data
# customer_id, country
customer_country = {
    1: 'USA',
    2: 'Canada',
    # Add more customer data here
}

# Sample data for reference
# You should replace these with your actual data
# employee_id, total_products_sold
employee_products_sold = {
    1: 50,
    2: 45,
    # Add more employee data here
}

# Sample data for reference
# You should replace these with your actual data
# shipper_id, total_orders_shipped
shipper_orders_shipped = {
    1: 80,
    2: 70,
    # Add more shipper data here
}

# Sample data for reference
# You should replace these with your actual data
# product_id, supplier_id
product_supplier = {
    1: 101,
    2: 102,
    # Add more product-supplier data here
}

# Question 1: How many distinct customers are there?
distinct_customers = len(customer_products_purchased)
print(f"There are {distinct_customers} distinct customers.")

# Question 2: How many products each customer has purchased?
for customer_id, product_count in customer_products_purchased.items():
    print(f"Customer ID {customer_id} has purchased {product_count} products.")

# Question 3: How many customers have purchased at least 3 products?
customers_3_or_more_products = len([customer_id for customer_id, product_count in customer_products_purchased.items() if product_count >= 3])
print(f"{customers_3_or_more_products} customers have purchased at least 3 products.")

# Question 4: What is the total value each customer has purchased?
for customer_id, total_purchase in customer_total_purchase.items():
    print(f"Customer ID {customer_id} has purchased a total value of {total_purchase}.")

# Question 5: How many customers have purchased more than a total price of 30?
customers_over_30 = len([customer_id for customer_id, total_purchase in customer_total_purchase.items() if total_purchase > 30])
print(f"{customers_over_30} customers have purchased more than a total price of 30.")

# Question 6: How many customers are there by each country?
from collections import Counter
customer_count_by_country = Counter(customer_country.values())
print("Number of customers by each country:")
for country, count in customer_count_by_country.items():
    print(f"{country}: {count}")

# Question 7: How many products each employee has sold, and which employee has sold the maximum?
max_products_sold = max(employee_products_sold.values())
top_employees = [employee_id for employee_id, products_sold in employee_products_sold.items() if products_sold == max_products_sold]
print(f"The employee(s) who sold the maximum number of products ({max_products_sold}): {', '.join(map(str, top_employees))}")

# Question 8: Which shipping unit is used most frequently?
max_orders_shipped = max(shipper_orders_shipped.values())
top_shippers = [shipper_id for shipper_id, orders_shipped in shipper_orders_shipped.items() if orders_shipped == max_orders_shipped]
print(f"The shipping unit used most frequently is {', '.join(map(str, top_shippers))} with {max_orders_shipped} orders shipped.")

# Question 9: Which product and respective unit details the most frequent supplier is providing?
most_frequent_supplier = max(product_supplier, key=product_supplier.get)
print(f"The most frequent supplier is Supplier ID {product_supplier[most_frequent_supplier]}. They provide Product ID {most_frequent_supplier}.")