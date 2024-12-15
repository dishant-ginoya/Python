# # ------- Custom Exception Handling in a Shopping Cart -------
# #
# #   Create a shopping cart program where users can add items, specify quantities, and calculate the total cost.
# #   Implement error handling for various scenarios and create custom exceptions to manage specific errors.
# #
# # Instructions:
# # 1.) Item Catalog:
# #       Create a dictionary of items available in the store with their prices.
# #          catalog = {
# #                     "apple": 0.5,
# #                     "banana": 0.3,
# #                     "orange": 0.7,
# #                     "milk": 1.2,
# #                     "bread": 1.5
# #                     }
# #       Ensure the inputs are valid numbers.
# # 2.) Shopping Cart:
# #       Initialize an empty shopping cart.
# #
# # 3.) Custom Exceptions:
# #       Define custom exceptions for the following situations:
# #         ItemNotFoundException: Raised when the user tries to add an item that is not in the catalog.
# #         InvalidQuantityException: Raised when the user inputs a negative quantity.
# #
# # 4.) Error Handling:
# #      Use `try-except` blocks to handle:
# #         invalid item selection.
# #         invalid quantity input.
# #         General exceptions.
# #
# # 5.) Cart Operations:
# #       Allow the user to add items to the cart by specifying the item name and quantity.
# #       If an item is already in the cart, update the quantity.
# #       Display the cart contents and the total price.
# #
# # 6.) Exit Condition:
# #       Allow the user to exit the program and display the final cart and total price.
# #
# #  -------------------
# # TEST CASE :-
# #   Available items: apple, banana, orange, milk, bread
# #     Enter an item to add to your cart (or 'exit' to finish): apple
# #     Enter quantity for apple: 3
# #     -> Added 3 apple(s) to your cart.
# # -------------------
# #     Enter an item to add to your cart (or 'exit' to finish): orange
# #     Enter quantity for orange: 2
# #     -> Added 2 orange(s) to your cart.
# # -------------------
# #     Enter an item to add to your cart (or 'exit' to finish): chocolate
# #     -> Error: chocolate is not available in the catalog.
# # -------------------
# #     Enter an item to add to your cart (or 'exit' to finish): banana
# #     Enter quantity for banana: -1
# #     -> Error: Quantity cannot be negative.
# # -------------------
# #     Enter an item to add to your cart (or 'exit' to finish): exit
# #     Your cart:
# #         apple: 3 @ $0.5 each = $1.5
# #         orange: 2 @ $0.7 each = $1.4
# #         Total price: $2.9

# # ========================================================================================================== # #


catalog = {
    'apple': 0.5,
    'banana': 0.3,
    'orange': 0.7,
    'milk': 1.2,
    'bread': 1.5
}

cart = {}


def Is_view_catalog():
    global catalog
    print(f'''
+---------------------+
| {'items'.ljust(11).capitalize()}|{'price'.rjust(7).capitalize()} |
|---------------------|''')
    for item, price in catalog.items():
        print(f'''| {item.ljust(11).capitalize()}:{str(price).rjust(7)} |''')
    print(f'''{'+'}{''.center(21, '-')}{'+'}''')


def Is_view_cart():
    global cart
    print(f'''
+-----------------------------------+''')
    if cart:
        print(f'''| {'Items'.ljust(10)}|{'Price'.rjust(6)} |{'Qty'.rjust(4)} |{'Total'.rjust(8)} |
|-----------------------------------|''')
        grand_total = 0
        for item in cart:
            name = cart[item]
            total = float(name['qty'] * name['price'])
            print(
                f'''| {item.ljust(10)}|{str(catalog[name]).rjust(6)} |{str(name['qty']).rjust(4)} |{str(total).rjust(8)} |''')
            grand_total += total
        print(f'''|                                   |
|                         ----------|
| {'Grand Total'.center(24)}|{str(float(grand_total)).rjust(8)} |''')
    else:
        print(f''' * * *  Your Cart Is Empty !  * * *''')
    print(f'''+-----------------------------------+''')


def Is_add_cart():
    global catalog
    global cart
    while True:
        item = str(input('\n  Enter an item to add to your cart (or q to exit):- ')).lower().strip()
        if item in catalog:
            while True:
                try:
                    quantity = int(input(f'  Enter quantity for {item}: ').strip())
                    if quantity > 0:
                        if item not in cart:
                            cart[item] = {'price': catalog[item], 'qty': 0}
                        cart[item]['qty'] = quantity + cart[item]['qty']
                        break
                    else:
                        print('\n  --> Error: Quantity cannot be negative.')
                except ValueError:
                    print('\n  --> Error: Please Enter Digits')
        elif item == 'q':
            break
        else:
            print(f'\n  --> Error: {item} is not available in the catalog.')


def Is_its_choice(option):
    if option == 'v':
        Is_view_catalog()
    elif option == 'a':
        Is_add_cart()
    elif option == 's':
        Is_view_cart()
    else:
        print('\n ---- Please Enter Valid Option ----')


while True:
    print("""
1. V For View Available Items
2. A For Add to Cart
3. S For View Cart
4. Q For Exit""")
    option = input('\n Which Command Perform To You ? :- ').lower().strip()
    if option == 'q':
        Is_view_cart()
        break
    else:
        Is_its_choice(option)
