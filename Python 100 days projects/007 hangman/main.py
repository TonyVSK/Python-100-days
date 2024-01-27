from ascii import opening, hangman, skull, trophy
from words import words
from time import sleep
from random import randint

sleep(0.5)
print(opening)
sleep(0.5)


counter = 0
lives = 7
errors = 0
verify = 0

computer = words[randint(0, len(words)-1)]
secret_word = []
while counter<len(computer):
    secret_word.append('-')
    counter+=1



# while user still has some life
while lives != 0:
    print(secret_word)
    letter = input('Insert a letter: ')
    newcounting=0

    #verify the letter of user in word of computer
    for i in range(0, len(computer)):
        if letter == computer[i]:
            secret_word[i]=letter
            newcounting=1
            verify += 1
    # if all words are complete, finish the loop
    if verify == len(computer):
        break

    # if the user's letter isn't in the computer word, loose one life
    if newcounting == 0:
        print('sorry, you lost one life')
        sleep(0.5)
        lives-=1
        errors+=1
        print(hangman[errors-1])

# if user's lives == 0, game over
if lives == 0:
    print('sorry...')
    sleep(0.5)
    print('You lost the game...')
    sleep(0.5)
    print(skull)

else:
    print(computer)
    sleep(0.5)
    print('Congratulations!')
    sleep(0.5)
    print('You won the game!')
    sleep(0.5)
    print(trophy)