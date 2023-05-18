"""CODE BY EZECHUKWU EMMAUEL"""


"""
Extra Creativity: the user can choose multiple of a particular item and the price will be multiplied by the number of items && 

The User can use either number based or word based to perform actions on the cart
"""

shopping_cart = []  # List to store the items in the cart


# Display the available options to the user
print("Welcome to Nuel-Green Suppermarket!\nBelow Is your Automated shopping cart and instructions on how to manage your Cart\n")
options = print(
    "Choose from the Options below: \n 1 - ADD item \n 2 - REMOVE item \n 3 - VIEW cart \n 4 - COMPUTE total price \n 0 - EXIT \n")

action = ''

while action != '0' or action != 'exit':
    action = input("Enter your action: ").lower()

    # Add item to the cart
    if action == '1' or action == 'add':
        item_name = input("Enter the name of the item: ")
        quantity = int(input("Enter the Quantity of the item: "))
        item_price = float(input("Enter the price of the item: "))
        shopping_cart.append((item_name, item_price, quantity))
        print("Item added to the cart.")

    # Remove item from the cart
    elif action == '2' or action == 'remove'.lower():
        item_index = int(input("Enter the index of the item to remove: ")) - 1
        if item_index < 0 or item_index >= len(shopping_cart):
            print("Invalid item index.")
        else:
            item = shopping_cart.pop(item_index)
            print(f"Item '{item[0]}' removed from the cart.")

    # View the items in the cart
    elif action == '3' or action == 'view':
        print("You already have the following items in the cart:")
        #The user is shown 1-based indexes and the program translates these to 0-based indexes for the lists.
        for index, item in enumerate(shopping_cart):
            print(f"{index + 1}. Item: {item[0]} - Price = N{item[1]} - Quantity: {item[2]}")

    # Calculate the total price of the cart
    elif action == '4' or action == 'compute':
        total_price = 0
        for item in shopping_cart:
            item_price = item[1] * item[2]  # Multiply price by quantity
            total_price += item_price
        print("Total price of the cart: N{:.2f}".format(total_price))

    # Exit the program
    elif action == '0' or action == 'exit':
        print("Exiting the program...")
        break

    else:
        print("Invalid action. Please try again.")
