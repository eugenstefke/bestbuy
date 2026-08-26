class Product:

    def __init__(self, product_name, product_price, quantity_of_product):
        if not product_name:
            raise ValueError("Product name cannot be empty")
        if product_price < 0:
            raise ValueError("Price cannot be negative")
        if quantity_of_product < 0:
            raise ValueError("Quantity cannot be negative")

        self.product_name = product_name
        self.product_price = product_price
        self.quantity_of_product = quantity_of_product
        self.product_status = True

    def get_quantity(self):
        return self.quantity_of_product

    def set_quantity(self, quantity):

        if quantity < 0:
            print("Quantity must not be negative")
            return
        self.quantity_of_product = quantity
        if self.quantity_of_product == 0:
            self.deactivate()
        elif not self.product_status:
            self.activate()

    def is_active(self):
         return self.product_status

    def activate(self):
        self.product_status = True
        return self.product_status

    def deactivate(self):
        self.product_status = False
        return self.product_status

    def show(self):
        print(f"{self.product_name}, Price: ${self.product_price}, Quantity: {self.quantity_of_product}")


    def buy(self, quantity):

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("You cannot buy a negative or zero quantity")
        if not self.product_status:
            raise Exception(f"{self.product_name} is sold out")
        if self.get_quantity() < quantity:
            raise ValueError(f"I don't have that many. I've got {self.quantity_of_product} of them")

        self.quantity_of_product -= quantity
        if self.get_quantity() == 0:
            self.deactivate()
        return self.product_price * quantity

# bose = Product("Bose QuietComfort Earbuds", 250, 500)
# mac = Product("MacBook Air M2", 1450, 100)
#
# print(bose.buy("h"))
# print(mac.buy(100))
# print(mac.is_active())

# bose.show()
# mac.show()
# print(bose.buy())
# bose.set_quantity(1)
#
# bose.show()
# print(bose.buy(-1))
# bose.show()

