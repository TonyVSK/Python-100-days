# Files, derectories and paths

## Mail Merge Challenge

This repository contains a Python file manipulation challenge designed to teach you how to work with files, directories, and paths efficiently. The challenge is to create a mail merge system using letter templates and a list of recipient names.

### Repository Structure

The repository is organized as follows:

### Folder `Mail Merge Challenge`

- **Folder `Input`**: Contains input files necessary for the email merge process.
  - **Folder `Letters`**: Stores the letter template to be personalized with the names of the recipients.
    - File: `starting_letter.txt`
  - **Folder `Names`**: Contains the list of recipients' names.
    - File: `invited_names.txt`

- **Folder `Output`**: Stores the files generated after merging emails.
  - Files: `ReadyToSend_for_<name>.txt` (one file for each recipient)

- **`main.py`** file: Main code responsible for merging emails.

### How to use

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open the terminal and navigate to the cloned repository directory.
4. Run the `main.py` file to start the email merging process.

### Running the Code

The `main.py` file reads the list of recipient names and the letter template from the input files, personalizes the letter with their names, and generates ready-to-send files in the output folder.

```python
names = []

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        names.append(name.strip())

with open("Input/Letters/starting_letter.txt") as letter:
    text = letter.read()

for name in names:
    with open(f"Output/ReadyToSend_for_{name}.txt", "w") as newFile:
        newText = text.replace('[name]', f'{name}')
        newFile.write(newText)
```


## Snake Game with Highscore
This repository contains a version of the classic Snake Game implemented in Python using the Turtle library. In addition to the game itself, there is also a highscore system to challenge players to achieve the highest score possible.

### Repository Structure
The repository has the following structure:

### **Folder snake game with highscore**
**highscore.txt** file: Stores the maximum score achieved by players.

**food.py file**: Implements the class responsible for creating and managing food in the game.

**main.py** file: Main code that runs the Snake game.

**scoreboard.py** file: Implements the class that controls and displays the score during the game.

**snake.py** file: Implements the class that defines the behavior of the snake in the game.

### How to play
1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open the terminal and navigate to the cloned repository directory.
4. Run the main.py file to start the Snake game.
5. Use the arrow keys on the keyboard to control the snake's movement.
6. Avoid colliding with the edges of the screen and the snake's own body.
7. Capture the food (blue dots) to increase your score.
8. Try to achieve the highest score possible and beat the current record recorded in the highscore.txt file.

### Running the Code
The main.py file starts the Snake game and controls its execution, including detecting collisions, snake movement and updating the score.