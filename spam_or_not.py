class Product:
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock

  def __str__(self):
    return f"{self.name} - ${self.price} (Stock: {self.stock})"

class FlipkartClone:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def list_products(self):
    for product in self.products:
      print(product)

  def buy_product(self, product_name, quantity):
    for product in self.products:
      if product.name == product_name:
        if product.stock >= quantity:
          product.stock -= quantity
          print(f"Purchased {quantity} of {product.name}")
        else:
          print(f"Not enough stock for {product.name}")
        return
    print(f"Product {product_name} not found")

# Example usage
if __name__ == "__main__":
  flipkart_clone = FlipkartClone()
  flipkart_clone.add_product(Product("Laptop", 1000, 10))
  flipkart_clone.add_product(Product("Phone", 500, 20))

  print("Available products:")
  flipkart_clone.list_products()

  print("\nBuying 2 Laptops:")
  flipkart_clone.buy_product("Laptop", 2)

  print("\nAvailable products after purchase:")
  flipkart_clone.list_products()