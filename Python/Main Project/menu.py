#--------------------------------------------------------


# Setting global variables.
Total = 0
totalPrice = 0
drinkPriceTotal = 0

dinner_orders = []
drink_orders = []

# --------------------------------------------------------
# DINNER SECTION

dinner_menu = {
    "Dinner": {
        1: {"name": "Tikka Masala", "price": 8},
        2: {"name": "Lasagna Carbonara", "price": 11},
        3: {"name": "Steak and Chilli Garlic Noodles", "price": 11},
        4: {"name": "Falafel and Hummus", "price": 10},
        5: {"name": "Beef Burritos", "price": 9},
        6: {"name": "Katsu Curry", "price": 8}
    },

    "Children": {
        7: {"name": "Fish and Chips", "price": 6},
        8: {"name": "Beef Burger", "price": 6},
        9: {"name": "Peri Peri Chips", "price": 4}
    }
}


def DinnerMenu():

    column_width = 55

    print("\nDinner Menu".ljust(column_width) + "Children's Menu")
    print("-" * 50 + "     " + "-" * 30)

    dinner_items = list(dinner_menu["Dinner"].items())
    children_items = list(dinner_menu["Children"].items())

    for i in range(len(dinner_items)):

        dinner_number, dinner = dinner_items[i]

        dinner_text = (
            f"{dinner_number}. {dinner['name']} - €{dinner['price']:.2f}"
        )

        if i < len(children_items):

            children_number, child = children_items[i]

            children_text = (
                f"{children_number}. {child['name']} - €{child['price']:.2f}"
            )

        else:
            children_text = ""

        print(dinner_text.ljust(column_width) + children_text)


def GetOrder():

    global Total
    global dinner_orders

    ordering = True

    while ordering:

        Choice = int(input(
            "\nEnter the number of the item you want to order (1-9) or 0 to finish: "
        ))

        if Choice == 0:
            ordering = False

        elif Choice in dinner_menu["Dinner"]:
            item = dinner_menu["Dinner"][Choice]

            quantity = int(input(
                f"Enter quantity for {item['name']}: "
            ))

            item_total = quantity * item["price"]

            Total += item_total

            dinner_orders.append({
                "name": item["name"],
                "quantity": quantity,
                "total": item_total
            })

        elif Choice in dinner_menu["Children"]:
            item = dinner_menu["Children"][Choice]

            quantity = int(input(
                f"Enter quantity for {item['name']}: "
            ))

            item_total = quantity * item["price"]

            Total += item_total

            dinner_orders.append({
                "name": item["name"],
                "quantity": quantity,
                "total": item_total
            })

        else:
            print("Invalid choice. Please enter a number between 1-9.")


# --------------------------------------------------------

# --------------------------------------------------------
# DESSERT SECTION

# Dessert menu dictionary
dessert_menu = {
    1: {
        "name": "Cheesecake",
        "price": 6.50,
        "quantity": 0,
        "total": 0
    },

    2: {
        "name": "Tiramisu",
        "price": 5.50,
        "quantity": 0,
        "total": 0
    },

    3: {
        "name": "Brownie",
        "price": 5.50,
        "quantity": 0,
        "total": 0
    },

    4: {
        "name": "Banana Pudding",
        "price": 8.90,
        "quantity": 0,
        "total": 0
    },

    5: {
        "name": "Carrot Cake",
        "price": 7.50,
        "quantity": 0,
        "total": 0
    }
}


ice_cream_cost = 2.50
totalPrice = 0


# Displays the dessert menu
def display_menu():

    print("\nDessert Menu:")
    print("-------------------")

    for number, dessert in dessert_menu.items():
        print(f"{number}. {dessert['name']} - €{dessert['price']:.2f}")


# Takes the customer's dessert order
def take_order():

    global totalPrice

    ordering = True

    while ordering:

        dessert_choice = int(input(
            "\nEnter the number of the dessert you want to order (1-5) or 0 to finish: "
        ))

        # Finish ordering
        if dessert_choice == 0:
            ordering = False

        # Check if choice exists in dictionary
        elif dessert_choice in dessert_menu:

            dessert = dessert_menu[dessert_choice]

            dessert_quantity = int(input(
                f"Enter the number of {dessert['name']}s you want to order: "
            ))

            # Ask about ice cream
            additional_ice_cream = input(
                f"Would you like an extra scoop of ice cream for €{ice_cream_cost:.2f}? (yes/no): "
            )

            if additional_ice_cream.lower() == "yes":
                ice_cream_total = ice_cream_cost

            else:
                ice_cream_total = 0

            # Calculate dessert price
            dessert_total = dessert["price"] * dessert_quantity

            # Add ice cream
            dessert_total += ice_cream_total

            # Update quantity ordered
            dessert["quantity"] += dessert_quantity

            # Update total for this dessert
            dessert["total"] += dessert_total

            # Update overall dessert total
            totalPrice += dessert_total

            print(
                f"Your total price for {dessert['name']} "
                f"(including ice cream if selected) is €{dessert_total:.2f}"
            )

        else:
            print("Invalid choice, please enter a number between 1-5.")


# Displays dessert order summary
def display_total():

    print("\nOrder Summary:")
    print(f"{'Dessert Name':<20}{'Quantity':<10}{'Total Price':<15}")

    for dessert in dessert_menu.values():

        if dessert["quantity"] > 0:

            print(
                f"{dessert['name']:<20}"
                f"{dessert['quantity']:<10}"
                f"€{dessert['total']:.2f}"
            )

    print(f"\nTotal Price of all desserts: €{totalPrice:.2f}")


#-------------------------------------------------------------------

# ------------------------------------------------------------------
# DRINKS SECTION

drink_menu = {
    1: {
        "name": "Coke",
        "price": 4.50,
        "alcoholic": False
    },

    2: {
        "name": "Tea",
        "price": 5.00,
        "alcoholic": False
    },

    3: {
        "name": "Coffee",
        "price": 6.00,
        "alcoholic": False
    },

    4: {
        "name": "Tequila",
        "price": 12.00,
        "alcoholic": True
    },

    5: {
        "name": "Beer",
        "price": 10.50,
        "alcoholic": True
    }
}


def drinks():

    global drinkPriceTotal
    global drink_orders

    drinkPriceTotal = 0

    print("\nDrinks Menu:")
    print("-------------------")

    # Display numbered drinks
    for number, drink in drink_menu.items():
        print(f"{number}. {drink['name']} - €{drink['price']:.2f}")

    ordering = True

    while ordering:

        chosenDrink = int(input(
            "\nEnter the number of the drink you want (1-5) or 0 to finish: "
        ))

        # Finish drinks order
        if chosenDrink == 0:
            ordering = False

        # Check if number exists in drink menu
        elif chosenDrink in drink_menu:

            drink = drink_menu[chosenDrink]

            # Check age if alcoholic
            if drink["alcoholic"]:

                over18 = input(
                    "Are you over 18? (yes/no): "
                ).lower()

                if over18 != "yes":
                    print("Sorry, we cannot serve you alcohol.")
                    continue

            # Ask for quantity
            drinkAmount = int(input(
                f"How many {drink['name']}s would you like?: "
            ))

            # Calculate cost
            drinkTotal = drink["price"] * drinkAmount

            # Add to overall drinks total
            drinkPriceTotal += drinkTotal

            # Store order information
            drink_orders.append({
                "name": drink["name"],
                "quantity": drinkAmount,
                "total": drinkTotal
            })

            print(
                f"{drink['name']} x{drinkAmount} - €{drinkTotal:.2f}"
            )

        else:
            print("Invalid choice. Please enter a number between 1-5.")


    # Display drinks order summary
    print("\nOrder Summary:")
    print(f"{'Drink Name':<15}{'Quantity':<10}{'Total Price':<15}")

    for order in drink_orders:
        print(
            f"{order['name']:<15}"
            f"{order['quantity']:<10}"
            f"€{order['total']:.2f}"
        )

    print(f"\nTotal Price of all drinks: €{drinkPriceTotal:.2f}")


# ------------------------------------------------------------------

# ------------------------------------------------------------------
# INITIAL MENU / MAIN PROGRAM


main_menu = {
    1: "Dinner",
    2: "Dessert",
    3: "Drinks"
}


def initial_menu():

    print("\nInitial Menu:")
    print("-------------------")

    for number, menu_name in main_menu.items():
        print(f"{number}. {menu_name}")


def menu_order():

    menu_ordering = True

    while menu_ordering:

        initial_menu()
        
        user_order = int(input(
            "\nChoose Your Menu (1-3) or 0 to finish: "
        ))

        if user_order == 0:
            menu_ordering = False

        elif user_order == 1:
            DinnerMenu()
            GetOrder()

        elif user_order == 2:
            display_menu()
            take_order()
            display_total()

        elif user_order == 3:
            drinks()

        else:
            print("Invalid choice. Please enter a number between 1-3.")


def ReviewOrder():

    print("\n========================================")
    print("           FINAL ORDER REVIEW")
    print("========================================")

    # Dinner
    print("\nDinner / Children's Orders:")

    if len(dinner_orders) == 0:
        print("No dinner items ordered.")

    else:
        for order in dinner_orders:
            print(
                f"{order['name']} x{order['quantity']} "
                f"- €{order['total']:.2f}"
            )

    # Desserts
    print("\nDessert Orders:")

    dessert_ordered = False

    for dessert in dessert_menu.values():

        if dessert["quantity"] > 0:
            dessert_ordered = True

            print(
                f"{dessert['name']} x{dessert['quantity']} "
                f"- €{dessert['total']:.2f}"
            )

    if not dessert_ordered:
        print("No desserts ordered.")

    # Drinks
    print("\nDrink Orders:")

    if len(drink_orders) == 0:
        print("No drinks ordered.")

    else:
        for order in drink_orders:
            print(
                f"{order['name']} x{order['quantity']} "
                f"- €{order['total']:.2f}"
            )

    # Final total
    finalOrderPrice = Total + totalPrice + drinkPriceTotal

    print("\n----------------------------------------")
    print(f"Final Order Total: €{finalOrderPrice:.2f}")
    print("----------------------------------------")


def CancelOrder():

    global Total
    global totalPrice
    global drinkPriceTotal
    global dinner_orders
    global drink_orders

    Total = 0
    totalPrice = 0
    drinkPriceTotal = 0

    dinner_orders.clear()
    drink_orders.clear()

    # Reset dessert quantities and totals
    for dessert in dessert_menu.values():
        dessert["quantity"] = 0
        dessert["total"] = 0

    print("\nYour order has been cancelled.")


def ConfirmOrder():

    ReviewOrder()

    confirmation = input(
        "\nWould you like to confirm or cancel your order? "
        "(confirm/cancel): "
    ).lower()

    if confirmation == "confirm":
        OverallTotal()

    elif confirmation == "cancel":
        CancelOrder()

    else:
        print("Invalid choice.")
        ConfirmOrder()


def OverallTotal():

    finalOrderPrice = drinkPriceTotal + totalPrice + Total

    print(
        f"\nThank you for ordering, "
        f"your total price will come to: €{finalOrderPrice:.2f}"
    )


def Main():

    menu_order()
    ConfirmOrder()

Main()