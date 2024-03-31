# Project: Coffee Machine (Advanced Version)

The Coffee Machine project is now in an advanced version, with significant improvements in the code structure and functionality. This version utilizes more advanced concepts of object-oriented programming in Python, as well as modularity and encapsulation.

## Key Enhancements

### 1. Increased Modularity
- The code has been divided into several separate Python files (`main.py`, `coffee_maker.py`, `menu.py`, `money_machine.py`), each containing classes and functions related to specific aspects of the project.
- This promotes better code organization, making it more readable, scalable, and easy to maintain.

### 2. Use of Classes and Objects
- The project now employs classes and objects to model the different components of the coffee machine, such as the coffee maker, menu, and payment processor.
- Each class has specific attributes and methods that help represent and manage its behavior within the system.

### 3. Enhanced Resource Reporting and Control
- The `CoffeeMaker` class now provides methods for reporting the current status of the machine's resources, such as water, milk, and coffee.
- Additionally, checking for sufficient resources to make a drink has been improved, ensuring a more accurate response to the user when resources are insufficient.

### 4. Improved Payment Processing
- The `MoneyMachine` class now handles coin processing and payments more efficiently.
- Methods have been refined to calculate the total value of inserted coins and check if the payment is sufficient for the selected drink.
- Machine profit control has also been enhanced, accurately recording the profit generated from coffee sales.

## Comparison with Previous Version

This version of the Coffee Machine project offers several improvements over the previous version:

- Enhanced modularity, with the code divided into separate files for better organization and maintenance.
- Use of classes and objects to represent specific components of the coffee machine, providing a more object-oriented structure.
- More detailed resource reporting and control, ensuring more efficient management of the machine's resources.
- More robust payment processing, with refined methods to calculate change and accurately record machine profit.

## Project Files

- `main.py`: Contains the main code for running the coffee machine, interacting with the `CoffeeMaker`, `Menu`, and `MoneyMachine` classes.
- `coffee_maker.py`: Contains the `CoffeeMaker` class, responsible for managing resources and brewing coffee.
- `menu.py`: Contains the `MenuItem` and `Menu` classes, which represent the menu of available drinks in the machine.
- `money_machine.py`: Contains the `MoneyMachine` class, responsible for payment processing and financial control of the machine.

## How to Use

1. Run the `main.py` file.
2. Choose a drink by typing 'espresso', 'latte', or 'cappuccino'.
3. Insert coins as requested.
4. Wait for the drink to be prepared and receive change, if applicable.