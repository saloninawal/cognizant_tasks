
# Define a variable for the order amount
order_amount = 150

# Function to apply discount
def apply_discount(order_amount):
    if order_amount > 100:
        return order_amount * 0.9 
    else:
        return order_amount  


final_price = apply_discount(order_amount)

# Print the price
print(f"Final price after discount: ${final_price:.2f}")
