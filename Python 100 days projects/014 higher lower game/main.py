from ascii import logo, gameOver, trophy, vs, listValues
from time import sleep
from random import randint


def complete():
    print('Congratulations! you won the game!')
    sleep(1)
    print(trophy)


def end_of_game():
    print('Sorry... you lost the game')
    sleep(1)
    print(gameOver)


user = 'ok'
counter = 0


people = listValues

    
a = people[randint(0, len(people)-1)]
b = people[randint(0, len(people)-1)]
while a == b:
    b = people[randint(0, len(people)-1)]
people.remove(a)
people.remove(b)



print(logo)


while user == 'ok':
    print(f'You got {counter} points')
    # verify if user choosed the right option
    user = input(f"Compare A: {a['Name']}, a {a['description']} \n{vs} \nAgaint B: {b['Name']}, a {b['description']}: \nWho has more followers? Type 'A' or 'B': ").lower()
    if (a['followers'] > b['followers'] and user == 'a'): 
        counter += 1
        user = 'ok'
        a = a
        b = people[randint(0, len(people)-1)]
        while a == b:
            b = people[randint(0, len(people)-1)]
        people.remove(b)
    elif (b['followers'] > a['followers'] and user == 'b'):
        counter += 1
        user = 'ok'
        a = b
        b = people[randint(0, len(people)-1)]
        while a == b:
            b = people[randint(0, len(people)-1)]
        people.remove(b)
    else:
        user = 'wrong'
    if len(people) == 0:
        complete()

if user == 'wrong':
    end_of_game()