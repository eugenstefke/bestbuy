from products import Product
from store import Store
from functools import partial

def menu():
    """Prints the store's main menu to the console."""
    print("\n   Store Menu\n"
          "   ----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit")

def start(best_buy):
    """
    Starts the interactive store user interface.
    Repeatedly displays the menu and dispatches the user's input to
    the matching function until "Quit" is chosen.

    Args: best_buy (Store): The store to interact with.
    """

    functions = {
            1: partial(list_all_products, best_buy),
            2: partial(show_total_amount, best_buy),
            3: partial(make_an_order, best_buy),
            4: quit_app
        }
    quit = True
    while quit:
        menu()
        try:
            user_input = int(input("Please choose a number: "))
            if 1 <= user_input <= 4:
                quit = functions[int(user_input)]()
            else:
                print("\nUnknown command, please enter a number between 1 and 4")
        except ValueError:
            print("\nUnknown command, please enter a number between 1 and 4")

def quit_app():
    """
    Ends the main loop of the user interface.
    Returns: Always False, to terminate the while loop in start().
    """
    return False

def list_all_products(best_buy):
    """
    Displays all active products in the store, numbered, on the console.
    Args: (Store): The store whose products should be displayed.
    Returns: Always True, so the menu loop keeps running.
    """

    products = best_buy.get_all_products()
    print("------")
    for i, product in enumerate(products, start=1):
        print(f"{i}. ", end="")
        product.show()
    print("------")

    return True

def make_an_order(best_buy):
    """
    Guides the user interactively through placing an order.
    Displays all available products and repeatedly lets the user enter
    a product number and quantity, until they cancel with an empty
    input. The collected order is then processed via Store.order().
    Args: best_buy (Store): The store to order from.

    Returns:
    True, so the menu loop keeps running;
    None, if the order was cancelled without any selection.
    """

    products = best_buy.get_all_products()
    list_all_products(best_buy)
    print("When you want to finish order, enter empty text.")

    shopping_list = []
    while True:
        product_input = input("Which product # do you want? ")
        if product_input == "":
            break

        amount_input = input("What amount do you want? ")
        if amount_input == "":
            break

        try:
            product_index = int(product_input) - 1
            amount = int(amount_input)
            if product_index < 0 or product_index >= len(products):
                print("Invalid product number.\n")
                continue
            shopping_list.append((products[product_index], amount))
            print("Product added to list!\n")
        except ValueError:
            print("Please enter numbers only.\n")

    if not shopping_list:
        print("Order cancelled - nothing selected.\n")
        return

    try:
        total_price = best_buy.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total_price}")
    except Exception as e:
        print(f"Error while making order! {e}")

    return True

def show_total_amount(best_buy):
    """
    Displays the total quantity of all active products in the store.
    Args: best_buy (Store): The store whose total quantity should be displayed.

    Returns: Always True, so the menu loop keeps running.
    """

    print(f"Total of {best_buy.get_total_quantity()} items in store")
    return True

def main():
    """Initializes the default inventory and starts the user interface."""
    product_list = [Product("MacBook Air M2", 1450, 100),
             Product("Bose QuietComfort Earbuds", 250, 500),
             Product("Google Pixel 7", 500, 250)]

    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()