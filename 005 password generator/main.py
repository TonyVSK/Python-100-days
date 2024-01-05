from passwordlists import alphabet,  symbollist, numberlist
from random import randint, shuffle

print('Welcome to the PyPassword Generator!')
letters = int(input('How many letters would you like in your password? \n'))
symbols = int(input('How many symbols would you like? \n'))
numbers = int(input('How many numbers would you like? \n'))


password = []

# Letters
for i in range(0, letters):
    letter = randint(0, 25)
    computer=randint(1, 2)
    if computer == 1:
        password.append(alphabet[letter].upper())
    else:
        password.append(alphabet[letter])

# Symbols
for i in range(0, symbols):
    symbol = randint(0, 6)
    password.append(symbollist[symbol])

# Numbers
for i in range(0, numbers):
    number = randint(0, 9)
    password.append(numberlist[number])

# Final password
shuffle(password)
password = ''.join(password)

print(f'Here is your password: {password}')