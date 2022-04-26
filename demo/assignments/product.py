class Product:
    tax = 0.1    # static attribute

    @staticmethod
    def getTax():
        return Product.tax

    @staticmethod
    def setTax(value):
        Product.tax = value

    def __init__(self, name, price):
        self.pname = name
        self.price = price

    @property
    def name(self):
        return self.pname.upper()

    @property
    def netprice(self):
        return self.price * (1 + Product.tax)


Product.setTax(.12)
p1 = Product("Product 1", 10000)
p2 = Product("Product 2", 15000)

for p in (p1, p2):
    print(f"{p.name:20}  {p.netprice:8.2f}")



