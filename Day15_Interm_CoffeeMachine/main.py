from Menu_and_Rss import MENU, resources

choice = None


def buy_pay_coffee(_choice, _water, _coffee, _milk):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    coins_paid = float((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))

    if coins_paid >= float(MENU[f"{_choice}"]["cost"]):
        resources["water"] = _water
        resources["coffee"] = _coffee
        if _milk is not None:
            resources["milk"] = _milk

        if coins_paid > float(MENU[f"{_choice}"]["cost"]):
            change = round(coins_paid - MENU[f"{_choice}"]["cost"], 2)
            print(f"Here is $ {change} in change.\n")

        print(f"Here is your {_choice}! Enjoy!")

    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(_choice):
    able_to_make = True
    temp_water = None
    temp_coffee = None
    temp_milk = None

    if MENU[f"{_choice}"]["ingredients"]["water"] <= resources["water"]:
        temp_water = resources["water"] - MENU[f"{_choice}"]["ingredients"]["water"]
    else:
        print(f"Sorry there is not enough {list(resources.keys())[0]}.")
        able_to_make = False

    if MENU[f"{_choice}"]["ingredients"]["coffee"] <= resources["coffee"]:
        temp_coffee = resources["coffee"] - MENU[f"{_choice}"]["ingredients"]["coffee"]
    else:
        print(f"Sorry there is not enough {list(resources.keys())[2]}.")
        able_to_make = False

    if _choice != "espresso":
        if MENU[f"{_choice}"]["ingredients"]["milk"] <= resources["milk"]:
            temp_milk = resources["milk"] - MENU[f"{_choice}"]["ingredients"]["milk"]
        else:
            print(f"Sorry there is not enough {list(resources.keys())[1]}.")
            able_to_make = False

    if able_to_make:
        buy_pay_coffee(_choice, temp_water, temp_coffee, temp_milk)


# CoffeeMachine:

while choice != "q":

    print("\nHi! Nice to see You! We have: espresso - $ 1.50 | latte - $ 2.50 | cappuccino - $ 3.00")
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")

    elif choice == "espresso":
        make_coffee("espresso")

    elif choice == "latte":
        make_coffee("latte")

    elif choice == "cappuccino":
        make_coffee("cappuccino")

    else:
        print("Something went wrong! Bye! See you again later!\n")


