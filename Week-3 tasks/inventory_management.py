# Define a list of items with their quantities
inventory = [('item1', 10), ('item2', 0), ('item3', 5)]

# Function to check inventory
def check_inventory(inventory):
    for item, quantity in inventory:
        if quantity == 0:
            print(f"{item} is out of stock!")
        else:
            print(f"{item} has {quantity} items in stock.")

 
check_inventory(inventory)
