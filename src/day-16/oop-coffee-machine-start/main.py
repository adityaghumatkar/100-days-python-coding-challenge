from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
machine_status = True

while machine_status:
    order = input(f"What would you like to order? ({menu.get_items()})").lower()
    if order == "report":
        coffee_maker.report()
        money.report()
    elif order == "off":
        machine_status = False
    else:
        menu_item = menu.find_drink(order)
        if menu_item != "None":
            is_resource_sufficient = coffee_maker.is_resource_sufficient(menu_item)
            if is_resource_sufficient:
                payment_status = money.make_payment(menu_item.cost)
                if payment_status:
                    coffee_maker.make_coffee(menu_item)
                else:
                    print("Insufficient funds. Please add more money to buy this drink")
# print(menu_item.ingredients)
