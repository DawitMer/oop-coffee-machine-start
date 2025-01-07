from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_shop_menu = Menu()
coffee_machine = CoffeeMaker()
casher = MoneyMachine()



def coffee_shop():
    is_on = True
    while is_on:
        order = input(f"What would you like? {coffee_shop_menu.get_items()}: ").lower()
        if order == "off":
            is_on = False
        elif order == "report":
            coffee_machine.report()
            casher.report()
        else:
            drink = coffee_shop_menu.find_drink(order)
            if drink:
                if coffee_machine.is_resource_sufficient(drink):
                    price_of_drink = drink.cost
                    if casher.make_payment(price_of_drink):
                        coffee_machine.make_coffee(drink)


coffee_shop()
