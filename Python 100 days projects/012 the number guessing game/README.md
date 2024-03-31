# Number Guessing Game

The Number Guessing Game is a simple Python program designed to entertain users by challenging them to guess a randomly generated number within a specified range. This README provides an overview of the project, its features, and how to use it effectively.

## Project Overview

The project consists of a single Python file:
- `main.py`: Contains the main code for running the Number Guessing Game.

## Features

### 1. Random Number Generation
- A random number between 1 and 100 is generated using the `randint()` function from the `random` module.

### 2. Difficulty Levels
- Users can choose between two difficulty levels: easy and hard.
- In the easy mode, users have 10 attempts to guess the number.
- In the hard mode, users have 5 attempts to guess the number.

### 3. User Interaction
- Users input their guesses, and the program provides feedback on whether the guess is too low, too high, or correct.
- The program also keeps track of the number of attempts remaining.

### 4. Game Logic
- The game ends when the user correctly guesses the number or exhausts all attempts.
- Upon winning or losing, appropriate messages are displayed to the user.

## How to Use

1. Run the `main.py` file.
2. Choose a difficulty level by typing 'easy' or 'hard'.
3. Guess the number within the specified number of attempts.
4. Receive feedback on each guess and continue guessing until you either win or lose the game.