# For day 16 of 100 days of code, the task is to re-create the same coffee machine from day 15. Only this time using,
# object-oriented programming. Main.py is the only file I wrote my own code in, feel free to poke around and use this
# amazing coffee machine.

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

print(logo)

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:

    initial_selection = input(f"What would you like today? {menu.get_items()}:")

    if initial_selection == "report":
        coffee_maker.report()
        money_machine.report()

    elif initial_selection == "off":
        is_on = False

    else:
        drink_selection = menu.find_drink(initial_selection)
        if coffee_maker.is_resource_sufficient(drink_selection):
            if money_machine.make_payment(drink_selection.cost):
                coffee_maker.make_coffee(drink_selection)
