from products import Product


class Store:
    """Manages a collection of Product instances.

    Allows adding/removing products and placing orders that span
    multiple products.
    """
    def __init__(self, products):
        """
        Creates a new store with an initial list of products.
        Args: products (list[Product]): List of products initially available in the store.
        """
        self.product_list = products

    def add_product(self, product):
        """
        Adds a product to the store.
        Args: product (Product): The product to add.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.
        Args: product (Product): The product to remove.
        Raises: ValueError: If the product is not contained in the list.
        """
        self.product_list.remove(product)

    def get_total_quantity(self):
        """
        Calculates the total quantity of all active products in the store.
        Returns: Sum of the stock quantities of all active products.
        """
        return sum(product.get_quantity() for product in self.product_list if product.is_active())

    def get_all_products(self):
        """Returns all active products in the store.
        Returns: List of active products (inactive ones are excluded).
        """
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list):
        """
        Places an order spanning multiple products.
        Args: shopping_list (list[tuple[Product, int]]): List of (product, quantity) tuples.
        Returns: The total price of the entire order.

        Raises:
        TypeError: If a quantity is not an integer.
        ValueError: If there is not enough stock for one of the products.
        Exception: If one of the products is inactive.
        """
        
        total = 0
        for product, quantity in shopping_list:
            result = product.buy(quantity)
            total += result
        return total
