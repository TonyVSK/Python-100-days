print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
percentage = int(input('What percentage tip would you like to five? 10, 12 or 15? '))

# updating the total value including percentage
bill = bill + (bill/100)*percentage

people = int(input('How many people to split the bill? '))

person  = bill/people

print(f'Each person should pay: ${person}')