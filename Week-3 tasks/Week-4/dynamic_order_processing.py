# dynamic_order_processing.py

from abc import ABC, abstractmethod

# Define the DiscountStrategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass

# Implement different discount strategies
class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount  # No discount for regular customers

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.9  # 10% discount for premium customers

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.8  # 20% discount for VIP customers

# Define the Order class
class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount
        self.discount_strategy = self.get_discount_strategy()

    def get_discount_strategy(self):
        if self.customer_type == "regular":
            return RegularDiscount()
        elif self.customer_type == "premium":
            return PremiumDiscount()
        elif self.customer_type == "VIP":
            return VIPDiscount()

    def final_price(self):
        return self.discount_strategy.apply_discount(self.order_amount)

# Create instances of Order for different customer types
order1 = Order("regular", 100)
order2 = Order("premium", 200)
order3 = Order("VIP", 300)

# Calculate and print the final prices after applying discounts
print(f"Regular customer final price: ${order1.final_price():.2f}")
print(f"Premium customer final price: ${order2.final_price():.2f}")
print(f"VIP customer final price: ${order3.final_price():.2f}")
