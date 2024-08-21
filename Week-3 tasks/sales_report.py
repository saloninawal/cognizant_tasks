
# Define a list
sales = [200, 600, 150, 800, 300]

# Function to generate 
def generate_report(sales):
    total_sales = 0
    print("Sales Report:")
    for sale in sales:
        if sale > 500:
            print(f"Sale amount: ${sale} - **Over $500!**")
        else:
            print(f"Sale amount: ${sale}")
        total_sales += sale
