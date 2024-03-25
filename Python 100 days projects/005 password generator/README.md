# PyPassword Generator

The PyPassword Generator is a Python project that generates secure passwords with customizable lengths of letters, symbols, and numbers. This project is more elaborate than previous examples and demonstrates the practical usage of modules and file imports in Python.

## Getting Started

Follow these instructions to run the PyPassword Generator on your local machine.

### Prerequisites

Ensure you have Python installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).

### Project Structure

The project consists of two files:
- `main.py`: Contains the main code for generating passwords.
- `passwordlists.py`: Contains lists of alphabets, numbers, and symbols used for password generation.

### Running the Script

1. Clone this repository to your local machine or download the `main.py` and `passwordlists.py` files directly.
2. Open your terminal or command prompt.
3. Navigate to the directory where the `main.py` file is located.
4. Run the script by typing the following command and pressing Enter:
    ```
    python main.py
    ```

## Usage

Follow the prompts to customize the length and composition of your password:
- Enter the number of letters, symbols, and numbers you want in your password.
- The script will generate a random password based on your inputs.

## New Concepts

This project introduces the following concepts:
- **Module Import**: The `passwordlists.py` file is imported as a module in `main.py` to access lists of alphabets, numbers, and symbols.
- **File Imports**: The `passwordlists.py` file is imported into `main.py` to utilize the lists defined in it.