# inventory_management.py

# 1. Lists: Manage product names
product_names = ["Apples", "Bananas", "Cherries"]

def add_product(product_list, product_name):
    product_list.append(product_name)
    print(f"Added {product_name} to the product list.")

def remove_product(product_list, product_name):
    if product_name in product_list:
        product_list.remove(product_name)
        print(f"Removed {product_name} from the product list.")
    else:
        print(f"{product_name} not found in the product list.")

def update_product(product_list, old_name, new_name):
    if old_name in product_list:
        index = product_list.index(old_name)
        product_list[index] = new_name
        print(f"Updated {old_name} to {new_name} in the product list.")
    else:
        print(f"{old_name} not found in the product list.")

# 2. Dictionaries: Store product details
product_details = {
    "Apples": {"quantity": 50, "price": 0.5},
    "Bananas": {"quantity": 30, "price": 0.3},
    "Cherries": {"quantity": 20, "price": 1.5},
}

def add_product_detail(details_dict, product_name, quantity, price):
    details_dict[product_name] = {"quantity": quantity, "price": price}
    print(f"Added {product_name} with quantity {quantity} and price ${price} to the product details.")

def update_product_detail(details_dict, product_name, quantity=None, price=None):
    if product_name in details_dict:
        if quantity is not None:
            details_dict[product_name]["quantity"] = quantity
        if price is not None:
            details_dict[product_name]["price"] = price
        print(f"Updated {product_name} details in the product details.")
    else:
        print(f"{product_name} not found in the product details.")

def delete_product_detail(details_dict, product_name):
    if product_name in details_dict:
        del details_dict[product_name]
        print(f"Deleted {product_name} from the product details.")
    else:
        print(f"{product_name} not found in the product details.")

# 3. Tuples: Represent immutable product data
product_catalog = (
    ("Apples", 50, 0.5),
    ("Bananas", 30, 0.3),
    ("Cherries", 20, 1.5),
)

def display_catalog(catalog):
    print("\nProduct Catalog:")
    for product in catalog:
        print(f"Name: {product[0]}, Quantity: {product[1]}, Price: ${product[2]}")

# 4. Sets: Track unique product categories
product_categories = {"Fruits", "Vegetables"}

def add_category(categories_set, category):
    categories_set.add(category)
    print(f"Added {category} to the product categories.")

def remove_category(categories_set, category):
    if category in categories_set:
        categories_set.remove(category)
        print(f"Removed {category} from the product categories.")
    else:
        print(f"{category} not found in the product categories.")

# 5. Combining Collections: Generate reports
def generate_price_report(details_dict):
    sorted_products = sorted(details_dict.items(), key=lambda item: item[1]["price"])
    print("\nProduct Report Sorted by Price:")
    for product, details in sorted_products:
        print(f"Name: {product}, Quantity: {details['quantity']}, Price: ${details['price']}")

def find_products_in_price_range(details_dict, min_price, max_price):
    filtered_products = {product for product, details in details_dict.items() if min_price <= details["price"] <= max_price}
    print(f"\nProducts in the price range ${min_price} - ${max_price}: {filtered_products}")

# Running the functions to demonstrate usage

# List operations
add_product(product_names, "Oranges")
remove_product(product_names, "Bananas")
update_product(product_names, "Cherries", "Grapes")

# Dictionary operations
add_product_detail(product_details, "Oranges", 40, 0.7)
update_product_detail(product_details, "Apples", quantity=60)
delete_product_detail(product_details, "Bananas")

# Tuple operation
display_catalog(product_catalog)

# Set operations
add_category(product_categories, "Dairy")
remove_category(product_categories, "Vegetables")

# Combined operations
generate_price_report(product_details)
find_products_in_price_range(product_details, 0.4, 1.0)
