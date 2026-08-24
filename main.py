import products
import store
from functools import partial

def menu():
    print("\n   Store Menu\n"
          "   ----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit")

def start(best_buy):
    functions = {
            1: partial(store.Store.get_all_products, best_buy),
            2: partial(store.Store.get_total_quantity, best_buy),
            3: partial(store.Store.order, best_buy),
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
                print("\nUnknown command, please enter a number between 0 and 4")
        except ValueError:
            print("\nUnknown command, please enter a number between 0 and 4")

def quit_app():
    return False

def main():

    product_list = [ products.Product("MacBook Air M2", 1450, 100),
             products.Product("Bose QuietComfort Earbuds", 250, 500),
             products.Product("Google Pixel 7", 500, 250)
           ]

    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()