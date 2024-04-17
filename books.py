class Book:
    def __init__ (self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getprice(self):
        if hasattr(self, "discount"):
            return self.price * self.discount
        else:
            return self.price

    def setdiscount(self, amount):
        self.discount = amount
        return self.discount

    def __str__(self):
        price = str(self.price)
        return f"Available: {self.title} by {self.author} for {self.price} | {self.pages} Pages"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 336, 24.99)
book2 = Book("Harry Potter", "J.K. Rowling", 223, 19.99)
book3 = Book("Mein Kampf", "Adolf Hitler", 720, 34.99)

book2.setdiscount(.75)
book2.price = book2.getprice()
print(book1)
print(book2, "| 25% Off!")
print(book3)
