# True or False Quiz Game

The True or False Quiz Game is a simple yet engaging Python project that tests the player's knowledge by presenting true or false statements and requiring them to respond accordingly. The game is structured with several classes to manage questions, the quiz itself, and the quiz brain.

## Key Features and Enhancements

### 1. Structured Code with Classes
- The project is structured using three main classes: `Question`, `QuizBrain`, and the main script `main.py`.
- Each class is responsible for specific aspects of the game, such as representing individual questions, managing the quiz logic, and executing the game flow.

### 2. Dynamic Question Loading
- Questions are loaded from an external data file (`data.py`) into the quiz game dynamically.
- This allows for easy addition or modification of questions without needing to change the main code, enhancing scalability and maintainability.

### 3. Interactive Gameplay
- Players are presented with true or false statements and prompted to input their response.
- Feedback is provided immediately after each answer, informing the player if they were correct or incorrect.

### 4. Game Over Handling
- The game continues until all questions are answered, providing a dynamic and engaging experience for the player.
- If the player answers incorrectly, the game ends, and their score is displayed.

## Comparison with Previous Version

Compared to a previous version of the game, this version offers several enhancements:

- Use of classes for better code organization and modularity.
- Dynamic loading of questions from an external file, allowing for easier maintenance and expansion of the question bank.
- Improved feedback and game over handling, providing a more interactive and enjoyable gameplay experience.

## Project Files

- `main.py`: Contains the main code for running the quiz game, including question loading, game logic, and user interaction.
- `question_model.py`: Defines the `Question` class, representing individual quiz questions with text and answers.
- `quiz_brain.py`: Defines the `QuizBrain` class, responsible for managing the quiz logic, question progression, and user interaction.
- `data.py`: Contains the question data in a list format, which is loaded dynamically into the quiz game.

## How to Play

1. Run the `main.py` script.
2. Answer each true or false question presented by typing 'true' or 'false'.
3. Receive immediate feedback after each answer.
4. Continue until all questions are answered or the game ends.