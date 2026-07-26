from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    get_items = menu.get_items()
    user_drink = input(f"What would you like? {get_items} ").lower()

    if user_drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_drink == "off":
        break
    else:
        drink = menu.find_drink(user_drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)