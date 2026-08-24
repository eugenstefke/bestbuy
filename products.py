class Product:

    def __init__(self, product_name, product_price, quantity_of_product):
        self.product_name = product_name
        self.product_price = product_price
        self.quantity_of_product = quantity_of_product
        self.product_status = True

    def get_quantity(self):
        return self.quantity_of_product

    def set_quantity(self, quantity):

        if quantity > 0:
            if not self.product_status:
                self.activate()
                self.quantity_of_product += quantity

            self.quantity_of_product += quantity
        else:
            print("You cannot add a negative quantity")

    def is_active(self):
         return self.product_status

    def activate(self):
        self.product_status = True
        return self.product_status

    def deactivate(self):
        self.product_status = False
        return self.product_status

    def show(self):
        print(f"{self.product_name}, Price: {self.product_price}, Quantity: {self.quantity_of_product}")

    def buy(self, quantity):

        if quantity > 0:
            if not self.product_status:
                return "The product is sold out"

            if self.get_quantity() >= quantity:
                self.quantity_of_product -= quantity
                if self.get_quantity() == 0:
                    self.deactivate()
                return (f"The total price for the product is {self.product_price * quantity}")
            else:
                return(f"I don´t have that many.  I’ve got {self.quantity_of_product} of them")
        else: return "You cannot buy a negative quantity"



bose = Product("Bose QuietComfort Earbuds", 250, 500)
mac = Product("MacBook Air M2", 1450, 100)

print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())

bose.show()
# mac.show()
print(bose.buy(50))
bose.set_quantity(-1)

bose.show()
print(bose.buy(-1))
bose.show()

