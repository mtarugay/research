class Product:
    name : None
    price : None
    quantity : None

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("--PRODUCT DETAILS--")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print(" ")
        

class Electronic(Product):
    brand: None

    def __init__(self, name, brand, price, quantity):
        super().__init__(name, price, quantity)
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print("--PRODUCT DETAILS--")
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print(" ")

class Clothing(Product):
    size: None

    def __init__(self, name, size, price, quantity):
        super().__init__(name, price, quantity)
        self.name = name
        self.size = size
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print("--PRODUCT DETAILS--")
        print("Name:", self.name)
        print("Size:", self.size)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print(" ")

class Book(Product):
    author: None

    def __init__(self, name, author, price, quantity):
        super().__init__(name, price, quantity)
        self.name = name
        self.author = author
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print("--PRODUCT DETAILS--")
        print("Name:", self.name)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print(" ")

electronic1 = Electronic("Mouse", "Logitech", "99.99", "20")
electronic2 = Electronic("Keyboard", "HyperX", "79.99", "15")
clothing1 = Clothing("Red Polo Shirt", "Lacoste", "49.99", "5")
clothing2 = Clothing("White T-Shirt", "Penguin", "39.99", "5")
book1 = Book("Harry Potter", "J.K. Rowling", "19.99", "10")
book2 = Book("Mein Kampf", "Adolf Hitler", "24.99", "5")

electronic1.display()
electronic2.display()
clothing1.display()
clothing2.display()
book1.display()
book2.display()