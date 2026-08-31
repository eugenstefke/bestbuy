class Product:
    """
    Represents a product type available in the store (e.g. MacBook Air M2).
    Encapsulates a product's name, price, stock quantity, and active status,
    and provides methods for purchasing and managing quantity.
    """

    def __init__(self, product_name, product_price, quantity_of_product):
        """
        Creates a new product instance.
        Args:
        product_name (str): Name of the product. Must not be empty.
        product_price (float): Price of the product. Must not be negative.
        quantity_of_product (int): Initial stock quantity. Must not be negative.

        Raises: ValueError: If the name is empty or price/quantity is negative.
        """

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
        """
        Returns the current stock quantity of the product.
        Returns: int: The currently available quantity.
        """
        return self.quantity_of_product

    def set_quantity(self, quantity):
        """
        Sets the product's stock quantity to a new value.

        Automatically deactivates the product if the new quantity is 0,
        and reactivates it if it was previously inactive and the new
        quantity is greater than 0.

        Args: quantity (int): The new quantity. Must be >= 0.
        Raises: ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity_of_product = quantity
        if self.quantity_of_product == 0:
            self.deactivate()
        elif not self.product_status:
            self.activate()

    def is_active(self):
        """
        Checks whether the product is active (purchasable).
        Returns: True if the product is active, False otherwise.
        """
        return self.product_status

    def activate(self):
        """Activates the product so it can be purchased again."""
        self.product_status = True

    def deactivate(self):
        """Deactivates the product so it can no longer be purchased."""
        self.product_status = False

    def show(self):
        """
        Prints a human-readable representation of the product to the console.
        Format: "<name>, Price: $<price>, Quantity: <quantity>"
        """

        print(f"{self.product_name}, Price: ${self.product_price}, Quantity: {self.quantity_of_product}")


    def buy(self, quantity):
        """
        Buys a given quantity of this product.
        Reduces the stock quantity accordingly and deactivates the
        product if the quantity drops to 0.
        Args: quantity (int): The quantity to buy. Must be a positive integer.

        Returns: The total price of the purchase (price * quantity).

        Raises:
        TypeError: If quantity is not an integer.
        ValueError: If quantity <= 0 or there is not enough stock available.
        Exception: If the product is inactive (sold out).
        """

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

