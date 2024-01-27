print("""
         __________
        /\____;;___|
       | /         /
       `. ())oo() .
        |\(%()*^^()^|
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
""")
print('Welcome to Treasure island.')
print('Your mission is to find the treasure.')

way = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
if way != 'left':
    print('You fall into a hole. Game Over')
else:
    lake = input("You came to a lake. There is an island  in the middle of the lake. Type 'wait' to wait for a boat. Type 'swin' to swin across: \n").lower()
    if lake != 'wait':
        print("You were attacked by trout. Game over")
    else:
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
        if door == 'blue':
            print('You enter a room of beasts. Game Over.')
        elif door == 'red':
            print('A fireball was thrown at you. Game over!')
        elif door == 'yellow':
            print('You found the treasure, congrats!')
        else:
            print('A fireball was thrown at you. Game over!')