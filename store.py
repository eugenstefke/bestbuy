class Store:

    product_list = []

    def __init__(self, products):
        self.product_list = products

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        quantity_counter = 0
        for product in self.product_list:
            quantity_counter += product.get_quantity()
        print(f"Total of {quantity_counter} items in store")
        return quantity_counter

    def get_all_products(self):
        for product in self.product_list:
            product.show()
        return self.product_list

    def order(self, shopping_list):
        total = 0
        for product, quantity in shopping_list:
            result = product.buy(quantity)
            total += result
        return f"Order cost: {total} dollars."

# product_list = [products.Product("MacBook Air M2", 1450, 100),
#                 products.Product("Bose QuietComfort Earbuds", 250, 500),
#                 products.Product("Google Pixel 7", 500, 250),
#                     ]
#
# best_buy = Store(product_list)
# products = best_buy.get_all_products()
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))