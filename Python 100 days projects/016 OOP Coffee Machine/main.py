# Espresso 50 ml water 18 g coffee
# Latte 200 ml water 24 g coffee 150 ml milk 
# Cappuccino 250 ml water 24 g coffee 100 ml milk


# resources machine: 300 ml water 100 g coffee 200 ml milk


# Penny = 1 cent
# Nickel = 5 cents
# Dime = 10 cents
# Quarter = 25 cents
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

status = 'on'

while status =='on':
    
    options = menu.get_items()
    user = input(f"What would you like? {options}: ").lower()
    if user == 'off' or user == 'iff':
        status = 'off'
    elif user == 'report':
        print(money_machine.report(), coffee_maker.report())
    else:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)