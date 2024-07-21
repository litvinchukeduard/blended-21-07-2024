'''

class Product:
    name: str
    price: float
    quantity: int

    calculate_total_price()
    calculate_price(n)
'''

class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        if quantity < 0:
            raise ValueError
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def calculate_price(self, n: int):
        return self.price * n
    
class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date) -> None:
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

'''
class Store

    products: list[Product]
'''
class Store:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def calculate_total_product_price(self):
        total_price = 0.0
        for product in self.products:
            # total_price += product.calculate_total_price()
            total_price += product.price * product.quantity
        return total_price
    
    def find_product(self, name: str):
        for product in self.products:
            if product.name == name:
                return product
        raise ValueError('No such product')
    

# pen = Product("Pen", 5, 100)
# # print(pen)
# # print(pen.calculate_total_price())
# print(pen.calculate_price(25))
# try:
#     cheese = FoodProduct('Cheese', 50, -1, '2024-08-01')
# except ValueError:
#     print('Error while creating a class')

store = Store()

pen = Product("Pen", 5, 100)
cheese = FoodProduct('Cheese', 50, 10, '2024-08-01')
store.add_product(pen)
store.add_product(cheese)
store.add_product(Product('Paper', 1, 1000))
# store.products.append(Product("Pen", 5, 100))
print(store.products)
# print(store.calculate_total_product_price())

# print(store.find_product("Pen").name)
try:
    print(store.find_product("Pencil").name)
except ValueError:
    print("No such product")