class Product:
    def __init__(self ,product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
    def display_product_info(self):
        print(f"Product Name: {self.product_name}.")
        print(f"Price: shs.{self.price}.")
        print(f"Quantity in Stock: {self.quantity_in_stock}.")
        
class ShoppingCart:
    
    total_carts = 0
    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1
        
    def add_to_cart(self ,product , quantity):
        self.items.append((product ,quantity))
        
    def remove_from_cart(self, product):
        for item in self.items:
            if item == product:
                self.items.remove(item)
                break
            
    def display_cart(self):
       # Displays the items in the cart.
        if not self.items:
            print("Cart is empty.")
        else:
            print("Items in cart:")
            for item in self.items:
                product, quantity = item
                print(f"Product Name: {product.product_name}, Quantity: {quantity}")
    
            
    def calculate_total(self):
        
        # Calculates the total cost of the items in the cart.
        
        total = 0
        for item in self.items:
            product, quantity = item
            total += product.price * quantity
        return total
    
# Create three Product objects
product1 = Product("Apple", 1500, 10)
product2 = Product("Banana", 500, 20)
product3 = Product("Orange", 300, 15)

# Displaying products 
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

# Create two separate ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Perform operations on cart1
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 3)
cart1.display_cart()
print(f"Total: shs.{cart1.calculate_total()}")

# Perform operations on cart2
cart2.add_to_cart(product2, 4)
cart2.add_to_cart(product3, 1)
cart2.display_cart()
print(f"Total: shs.{cart2.calculate_total()}")

# Remove an item from cart1
cart1.remove_from_cart(product1)
cart1.display_cart()
print(f"Total: shs.{cart1.calculate_total()}")