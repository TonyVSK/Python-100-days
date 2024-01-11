# Espresso 50 ml water 18 g coffee
# Latte 200 ml water 24 g coffee 150 ml milk 
# Cappuccino 250 ml water 24 g coffee 100 ml milk


# resources machine: 300 ml water 100 g coffee 200 ml milk


# Penny = 1 cent
# Nickel = 5 cents
# Dime = 10 cents
# Quarter = 25 cents
from extras import MENU, profit, resource
espresso = MENU['espresso']['ingredients']
latte = MENU['latte']['ingredients']
cappuccino = MENU['cappuccino']['ingredients']
resources = resource

# print(espresso)
# print(latte)
# print(cappuccino)






# 4.b. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#   not continue to make the drink but print: “Sorry there is not enough water.”
#   c. The same should happen if another resource is depleted, e.g. milk or coffee.
def verifier(drink, resources):
    if 'water' in drink and resources['water'] < drink['water']:
        print("Sorry there is not enough water")
        return False
    if 'milk' in drink and resources['milk'] < drink['milk']:
        print("Sorry there is not enough milk")
        return False
    if 'coffee' in drink and resources['coffee'] < drink['coffee']:
        print("Sorry there is not enough coffee")
        return False
        
#    resources['water'] = resources['water'] - drink['water']
#    if len(drink) != 2:
#        resources['milk'] = resources['milk'] - drink['milk']
#    resources['coffee'] = resources['coffee'] - drink['coffee']
    return True


def coins_total(pennies, nickels, dimes, quarters):
    total = pennies/100 + nickels/20 + dimes/10 + quarters/4
    return total


def verifyMachineCoins(totalCoins, drink, resources, user, profit):
    if user == 'espresso':
        cost = 0.5
    if user == 'latte':
        cost = 1
    if user == 'cappuccino':
        cost = 1.5
    
    if totalCoins - cost < 0:
        print('Sorry, no enought cash')
        machineMoney = 0
    if totalCoins - cost == 0:
        print(f'there is your {user}')
        machineMoney = cost
    if totalCoins - cost > 0:
        if profit >= (totalCoins-cost):
            print(f'There is your {user}, take ${totalCoins - cost} back')
            machineMoney = cost
        else:
            print('Sorry, the machine has no enought cash to return, take your money back')
            machineMoney = 0            
    
    return machineMoney


def ingredientsMachine(drink, resources):
    resources['water'] = resources['water'] - drink['water']
    if len(drink) != 2:
        resources['milk'] = resources['milk'] - drink['milk']
    resources['coffee'] = resources['coffee'] - drink['coffee']

status = 'on'

while status =='on':
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user = input("What would you like? (espresso/latte/cappuccino: ").lower()

    # 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user == 'off':
        status='off'
        continue
    
    # 3. Print report.
    #   a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values
    if user == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f'Machine money: {profit}')
        continue

    # 4. Check resources sufficient?
    #   a. When the user chooses a drink, the program should check if there are enough
    #   resources to make that drink.
    if user in MENU:
        drink = MENU[user]['ingredients']
        verifier(drink, resources)

    # 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should
    # prompt the user to insert coins.]
    if verifier(drink, resources):    
        pennies = int(input('How manny pennies do you want to insert: '))
        nickels = int(input ('How many nickels do you want to insert: '))
        dimes = int(input('How many dimes do you want to input: '))
        quarters = int(input('How many quarters do you want to input: '))
        totalCoins = coins_total(pennies, nickels, dimes, quarters)

        
        machineMoney = verifyMachineCoins(totalCoins, drink, resources, user, profit)
        if machineMoney != 0:
            profit += machineMoney
            ingredientsMachine(drink, resources)

