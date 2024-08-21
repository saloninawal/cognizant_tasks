# enhanced_inventory_management.py

import threading
import time
import json
import os

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Added {quantity} of {item_name}. Total: {self.items[item_name]}")

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                print(f"Removed {quantity} of {item_name}. Total: {self.items[item_name]}")
            else:
                print(f"Not enough {item_name} to remove. Available: {self.items[item_name]}")
        else:
            print(f"{item_name} not found in inventory.")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.items, file)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as file:
                    self.items = json.load(file)
                print(f"Inventory loaded from {filename}.")
            except IOError as e:
                print(f"Error loading inventory from file: {e}")
        else:
            print(f"{filename} does not exist. Starting with an empty inventory.")

    def restock_alert(self):
        while True:
            for item_name, quantity in self.items.items():
                if quantity < 5:
                    print(f"Restock Alert: {item_name} is low in stock (Only {quantity} left).")
            time.sleep(10)  # Check every 10 seconds

# Create inventory instance
inventory = Inventory()

# Load existing inventory from file
inventory.load_from_file("inventory_data.json")

# Perform some operations
inventory.add_item("Apples", 10)
inventory.add_item("Bananas", 2)
inventory.remove_item("Apples", 3)

# Save inventory state to file
inventory.save_to_file("inventory_data.json")

# Start a thread to check for restocking alerts
restock_thread = threading.Thread(target=inventory.restock_alert, daemon=True)
restock_thread.start()

# Print current inventory state
print("Current inventory:")
print(inventory.items)

# Keep the program running to allow restocking alerts to be printed
while True:
    time.sleep(1)
