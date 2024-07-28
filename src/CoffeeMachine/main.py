# day 15

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0


def get_report():
    print(
        f"Water: {resources['water']}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}ml\nMoney: ${money} ")


def check_resources(drink):
    ingredients = drink["ingredients"]

    if resources["water"] < ingredients["water"]:
        return "water"
    elif "milk" in ingredients and resources["milk"] < ingredients["milk"]:
        return "milk"
    elif resources["coffee"] < ingredients["coffee"]:
        return "coffee"
    else:
        return "ok"


def check_money(drink, money_received):
    drink_price = drink["cost"]
    return drink_price > money_received


def insert_coins():
    quarters = int(input("how many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("how many pennies?"))

    return (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)


def update_resources(drink):
    resources["water"] -= drink["ingredients"]["water"]
    if "milk" in drink["ingredients"]:
        resources["milk"] -= drink["ingredients"]["milk"]
    resources["coffee"] -= drink["ingredients"]["coffee"]


def refill_resources():
    milk = int(input("Milk in ml"))
    water = int(input('Water in ml'))
    coffee = int(input("coffee in gm"))

    resources["water"] += water
    resources["milk"] += milk
    resources['coffee'] += coffee


def update_money(money_received, drink_cost):
    global money
    money += drink_cost


def return_change(money_received, drink_cost):
    return round(money_received - drink_cost, 2)


def process_drink(drink, money_received):
    update_resources(drink)
    cost = drink["cost"]
    update_money(money_received, cost)
    change = 0.0
    if cost < money_received:
        change = return_change(money_received, cost)
        print(f"Here is your ${change} in change.")


def start_machine():
    status = True
    while status:
        user_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
        if user_choice == "off":
            status = False
        else:
            if user_choice == "report":
                get_report()
            elif user_choice == 'refill':
                refill_resources()
            else:
                drink = MENU[user_choice]
                ingredient = check_resources(drink)
                if ingredient != "ok":
                    print(f"Sorry there is not enough {ingredient}")
                else:
                    print("Please insert coins.")
                    money_received = insert_coins()
                    if check_money(drink, money_received):
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        process_drink(drink, money_received)
                        print(f"Here is your {user_choice}. Enjoy!")


start_machine()
