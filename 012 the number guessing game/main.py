from random import randint


def game_function(difficulty, computer):
    attempt = difficulty
    for i in range(difficulty, 0, -1):
        print(f'You have {i} attempts remaining to guess the number')
        user = int(input('Make a guess: '))
        if user < computer:
            print('Too low, try again')
        if user > computer:
            print('Too high, try again')
        if user == computer:
            print(f'Congratulations, you got it, I was thinking in {computer}')
            break
        attempt -= 1
    if attempt == 0:
        print('Sorry... you lost the game')




print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

computer = randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    game_function(10, computer)
else:
    game_function(5, computer)