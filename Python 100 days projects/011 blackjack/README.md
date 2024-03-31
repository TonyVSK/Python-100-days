# Blackjack Game

The Blackjack Game project is an interactive Python program that simulates a simplified version of the popular casino card game Blackjack. It emphasizes the use of conditional statements, loops, functions, and randomization to create a dynamic and engaging gaming experience. This README highlights the importance of mastering control structures and introduces a more complex project suitable for intermediate-level programming learners.

## Project Overview

The project consists of a single Python file:
- `main.py`: Contains the main code for running the Blackjack game.

## Features

### 1. Card Handling Functions
- The `add_card()` function adds a random card to a player's hand.
- The `verify_counting()` function calculates the total value of a player's hand.

### 2. Game Logic
- Players are dealt two cards each, and one of the dealer's cards is revealed.
- Players have the option to request additional cards (hit) or pass (stand).
- The game determines the winner based on the player's and dealer's hands.

### 3. Interactive Interface
- Users interact with the game through command-line prompts, making decisions on whether to hit or stand.

### 4. Looping
- The game loop allows players to continue playing multiple rounds until they choose to quit.

## How to Use

1. Run the `main.py` file.
2. Follow the prompts to play the game.
3. Decide whether to hit (get another card) or stand (pass).
4. View the result of each round and the overall winner.

## Example
```
                            _____   
                    _____  |K  WW|         
            _____  |Q  ww| | ^ {)|  
     _____ |J  ww| | ^ {(| |(.)  | _____
    |10 ^ || ^ {)| |(.)  | | |  %||A .  |
    |^ ^ ^||(.)% | | |  %| |_  %>|| /.\ |
    |^ ^ ^|| | % | |_  %O|        |(_._)|
    |^ ^ ^||____[|                |  |  |
    |___0I|                       |____V|

Your cards: ['J', 10]
Computer's first card: K
Type 'y' to get another card, type 'n' to pass: y
Your cards: ['J', 10, 7]
Type 'y' to get another card, type 'n' to pass: n
Computer's 2 first cards: K J
You lost... computer got 20
Would you like to play again? 'yes' or 'no': no
```