# Maze Escaper with Functions

This Python script is a simple maze escape program that utilizes functions to navigate through a mini maze. It aims to teach the basics of maze navigation and function usage in Python.

## Getting Started

You can find the original code and additional resources for learning about maze escape on the [CodeHS website](https://codehs.com/).

## Understanding Functions in Python

Functions in Python are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable, and reducing repetition. Here's a breakdown of key concepts related to functions:

- **Definition**: Functions are defined using the `def` keyword, followed by the function name and parentheses containing any parameters. For example:
  ```python
  def turn_right():
      turn_left()
      turn_left()
      turn_left()

**Calling Functions**: To execute a function, you simply write its name followed by parentheses. For example:
```
turn_right()
```
**Parameters**: Functions can accept input parameters, which are variables passed to the function when it is called. These parameters can be used inside the function. For example:
```
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
```
**Return Values**: Functions can also return values using the return keyword. This allows the function to provide output that can be used elsewhere in the code. For example:
```
def add(x, y):
    return x + y

result = add(3, 4)
print(result)  # Output: 7
```

## Project Structure
The script consists of two main parts:

Function Definitions: Includes the definition of two functions (turn_right() and what_to_do()).
Main Execution: Invokes the what_to_do() function to navigate through the maze.

## Usage
The script uses a simple algorithm to escape the maze:

1. Define the behavior for different scenarios using the what_to_do() function.
2. Continuously call the what_to_do() function until the goal is reached.
## Example
Here's an example of how the script navigates through the maze using the defined functions:
```
what_to_do()
while not at_goal():
    what_to_do()
```