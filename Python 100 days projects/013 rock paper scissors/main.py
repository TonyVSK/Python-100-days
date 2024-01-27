from ascii import rock, paper, scissors
from random import randint

options = [rock, paper, scissors]

user = int(input('What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors: '))
computer = randint(0, 2)
print(computer)

print('You chose: ')
print(options[user])

print('I chose: ')
print(options[computer])

# Tied game
if computer == user:
    print('The game tied :0')
# Computer won the game
if (computer==2 and user==1) or (computer == 1 and user == 0) or (computer == 0 and user == 2):
    print('You lost the game')
# Player won the game
if (user==2 and computer==1) or (user == 1 and computer == 0) or (user == 0 and computer == 2):
    print('Congrats, you won the game')