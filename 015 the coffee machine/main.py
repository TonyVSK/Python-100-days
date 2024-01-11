# Espresso 50 ml water 18 g coffee
# Latte 200 ml water 24 g coffee 150 ml milk 
# Cappuccino 250 ml water 24 g coffee 100 ml milk


# resources machine: 300 ml water 100 g coffee 200 ml milk


# Penny = 1 cent
# Nickel = 5 cents
# Dime = 10 cents
# Quarter = 25 cents
from extras import MENU, profit, resources

status = 'on'

while status =='on':
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user = input("What would you like? (espresso/latte/cappuccino: ").lower()

    # 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user == 'off':
        status='off'
    
    # 3. Print report.
    #   a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values
    if user == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")