# Hangman Game

The Hangman Game is a Python project that implements the classic word-guessing game. It highlights the usage of modules created from separate Python files, functions, conditional statements, and loops.

## Project Overview

The project consists of three Python files:
- `main.py`: Contains the main code for running the Hangman game.
- `words.py`: Contains a list of words for the game to choose from.
- `ascii.py`: Contains ASCII art for the Hangman stages, opening message, skull (for game over), and trophy (for winning).

## Key Features

### 1. Modules and File Imports
The project showcases the use of separate Python files (`words.py` and `ascii.py`) as modules. These modules are imported into the `main.py` file to access word lists and ASCII art.

### 2. Functions
The game logic is encapsulated within functions, promoting code organization and reusability. Key functions include `turn_right()` and `what_to_do()`.

### 3. Conditional Statements
Conditional statements are used to control the flow of the game, such as determining if a guessed letter is correct and updating the player's lives accordingly.

### 4. Loops
The game loop (`while lives != 0`) ensures that the game continues until the player either wins or loses.

## How to Play

1. Run the `main.py` file to start the game.
2. Guess letters to uncover the secret word.
3. For each incorrect guess, a part of the Hangman is drawn.
4. Guess all letters correctly to win the game. Lose all lives to lose the game.

## Example Gameplay

```
Welcome to the Hangman Game!

['-', '-', '-', '-', '-', '-', '-', '-']
Insert a letter: e
['-', '-', 'e', '-', '-', '-', '-', '-']
Insert a letter: t
['t', '-', 'e', '-', '-', '-', '-', '-']
...
```


## Credits

The ASCII art used in this project was sourced from various online platforms.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
