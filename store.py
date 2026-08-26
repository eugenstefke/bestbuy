from products import Product


class Store:

    def __init__(self, products):
        self.product_list = products

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self):
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list):
        total = 0
        for product, quantity in shopping_list:
            result = product.buy(quantity)
            total += result
        return total

# product_list = [products.Product("MacBook Air M2", 1450, 100),
#                 products.Product("Bose QuietComfort Earbuds", 250, 500),
#                 products.Product("Google Pixel 7", 500, 250),
#                     ]
#
# best_buy = Store(product_list)
# products = best_buy.get_all_products()
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))