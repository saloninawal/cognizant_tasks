
# Define a dictionary 
customer_data = {'Alice': 120, 'Bob': 75, 'Charlie': 90}

# Function to update the purchase amount for a given customer
def update_purchase(customer_data, name, amount):
    if name in customer_data:
        customer_data[name] = amount
    else:
        print(f"Customer {name} not found!")

# Update the amt foe bob
update_purchase(customer_data, 'Bob', 100)

# Print 
print("Updated customer data:")
for name, amount in customer_data.items():
    print(f"{name}: ${amount}")
