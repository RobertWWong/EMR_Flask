# cart_service.py
class CartService:
    def __init__(self):
        self.cart_items = []

    def add_item(self, item_name, price):
        self.cart_items.append({"item": item_name, "price": price})

    def remove_item(self, index):
        if index < 0 or index >= len(self.cart_items):
            raise IndexError("Invalid index")
        del self.cart_items[index]

    def reset_cart(self):
        self.cart_items.clear()

    def calculate_total(self):
        return sum(item["price"] for item in self.cart_items)