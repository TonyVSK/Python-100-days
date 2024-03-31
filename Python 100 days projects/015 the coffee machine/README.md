# Project: Coffee Machine
The Coffee Machine project is a simple implementation of a coffee machine in Python, which simulates the basic functionalities of a real coffee machine. This project is a great way to introduce fundamental object-oriented programming concepts in Python, as well as common development practices such as control flow, data manipulation, and modularity.

## Object Orientation in Python
In Python, object-oriented programming is an essential approach to organizing and structuring code efficiently. Objects are instances of classes that contain data (attributes) and behaviors (methods). In this project, each type of coffee (espresso, latte, cappuccino) is represented as an object, with attributes for the required ingredients and the cost.

## Main Features
1. Drink Selection
The user can choose between three types of coffee: espresso, latte and cappuccino. Each selection is treated as a separate object, with specific ingredients and associated cost.

2. Feature Check
Before preparing the chosen drink, the program checks whether there are sufficient resources available in the machine, such as water, milk and coffee. If any resource is exhausted, the program informs the user that it is not possible to make the selected drink.

3. Currency Processing
After selecting the drink and checking the features, the user is asked to enter coins to pay for the drink. The program calculates the total value of the coins inserted and checks whether the value is enough to pay for the drink.

4. Drink Delivery and Change
If the value of the coins inserted is enough to pay for the drink, the program prepares the drink and delivers it to the user. If there is change to be returned, the program informs the user and provides change if there is enough money in the machine.


## Getting Started with Object Orientation
This project is an excellent way to start learning about object-oriented programming in Python. By implementing each type of coffee as a separate object, developers can practice creating classes, defining attributes and methods, encapsulating, and reusing code.

This README provides an overview of the Coffee Machine project's features and serves as a useful guide for Python beginners interested in learning about object orientation and software development.

## Project Files
* main.py: Contains the main code for running the coffee machine.
* extras.py: Separate file containing menu, profit and coffee machine resource definitions.

## How to use
1. Run the main.py file.
2. Choose a drink by typing 'espresso', 'latte' or 'cappuccino'.
3. Insert coins as prompted.
4. Wait for the drink to be prepared and receive change, if applicable.