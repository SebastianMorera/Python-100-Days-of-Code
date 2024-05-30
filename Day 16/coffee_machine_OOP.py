from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    is_on = True
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    coffee_menu = Menu()

    while is_on:
        choice = input(f"What would you like? ({coffee_menu.get_items()}): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = coffee_menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    coffee_machine()
