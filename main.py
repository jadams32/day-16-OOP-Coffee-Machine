# For day 16 of 100 days of code, the task is to re-create the same coffee machine from day 15. Only this time using,
# object-oriented programming. Main.py is the only file I wrote my own code in, feel free to poke around and use this
# amazing coffee machine.

# Import all the modules needed.
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

# Show the logo to the user.
print(logo)

# Initialize all the objects.
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# Setting a while loop variable.
is_on = True

while is_on:

    # Ask the user for their input today.
    initial_selection = input(f"What would you like today? {menu.get_items()}:")

    # If the user enters the secret word "report", show the resources left and money captured.
    if initial_selection == "report":
        coffee_maker.report()
        money_machine.report()

    # If the user enters "off" turn the machine off and exit the program.
    elif initial_selection == "off":
        is_on = False

    # If the user makes a drink selection check if there's enough resources and that the user paid the correct amount.
    # Then issue the drink deduct the resources and add to the profit.
    else:
        drink_selection = menu.find_drink(initial_selection)
        if coffee_maker.is_resource_sufficient(drink_selection):
            if money_machine.make_payment(drink_selection.cost):
                coffee_maker.make_coffee(drink_selection)
