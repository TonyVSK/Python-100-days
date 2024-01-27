from random import randint
from replit import clear
from time import sleep



def add_card(user, cards):
    new_card = cards[randint(0, 12)]
    user.append(new_card)
    return user


def verify_counting(user):
    counter = 0
    for each_card in user:
        if each_card == 'A':
            counter +=1
        elif each_card == 'J' or each_card =='Q' or each_card == 'K':
            counter += 10
        else:
            counter += each_card
    return counter


def who_won(decision, dealer, counter):
    if decision == 'n':
        print(f"Computer's 2 first cards: {dealer[0]} {dealer[1]}")
        computer_counter = verify_counting(dealer)
        if computer_counter > counter and computer_counter != counter:
            print(f"Sorry, you lost, computer got {computer_counter}")
        elif computer_counter <= counter:
            while computer_counter <21 and computer_counter <= counter:
                dealer = add_card(dealer, cards)
                sleep(1)
                print(dealer)
                computer_counter = verify_counting(dealer)
            if computer_counter > 21 or computer_counter<counter:
                sleep(1)
                print(dealer)
                print(f"You won! computer got {computer_counter}")
            if computer_counter>counter and computer_counter<=21:
                sleep(1)
                print(dealer)
                print(f"You lost... computer got {computer_counter}")



cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

game = """
                            _____   
                    _____  |K  WW|         
            _____  |Q  ww| | ^ {)|  
     _____ |J  ww| | ^ {(| |(.)  | _____
    |10 ^ || ^ {)| |(.)  | | |  %||A .  |
    |^ ^ ^||(.)% | | |  %| |_  %>|| /.\ |
    |^ ^ ^|| | % | |_  %O|        |(_._)|
    |^ ^ ^||____[|                |  |  |
    |___0I|                       |____V|
                              
"""
answer = 'yes'

while answer == 'yes':
    clear()
    print(game)
    user = [cards[randint(0, 12)], cards[randint(0, 12)]]
    dealer = [cards[randint(0, 12)], cards[randint(0, 12)]]
    print(f'your cards: {user}')
    print(f"Computer's first card: {dealer[0]}")
    decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while decision == 'y':
        user = add_card(user, cards)
        print(f'Your cards: {user}')

        counter = verify_counting(user)
        if counter > 21:
            print(f'Sorry... you lost the game, you got {counter}')
            break
        elif counter == 21:
            print('blackjack! you got 21')
            break
        else:
            decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        who_won(decision, dealer, counter)

    counter = verify_counting(user)
    who_won(decision, dealer, counter)
            


    answer = input("Would you like to play again? 'yes' or 'no': ").lower()