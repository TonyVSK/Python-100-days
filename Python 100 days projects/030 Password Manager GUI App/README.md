# Password Manager Application

This repository contains a Python script for a Password Manager application built using the Tkinter library. The application enables users to generate strong passwords and store them securely. It also provides functionality to search for and retrieve stored passwords.

## Introduction to Password Manager

A Password Manager is a software application that helps users store, generate, and manage their passwords securely. It enhances security by generating strong and unique passwords for each account and encrypting and storing them in a centralized database. Users can access their passwords using a master password or biometric authentication.

## Understanding the Script

The `main.py` script implements a Password Manager with the following features:

- **Password Generator**: The application generates strong passwords comprising letters, numbers, and symbols based on user-defined criteria.
- **Save Password**: Users can save their website credentials (website URL, username/email, and password) securely in a JSON file. Before saving, the application prompts users to confirm the details entered.
- **Search Functionality**: The application allows users to search for stored website credentials by entering the website URL. Upon searching, it displays the corresponding username/email and password.
- **Error Handling**: The script handles various types of errors, including JSON decoding errors and file not found errors, ensuring smooth execution and user experience.

## Password Generation

The password generation function creates passwords with a random combination of letters, numbers, and symbols, ensuring strength and uniqueness. Users can customize the length and complexity of the generated passwords.

## Data Storage

Website credentials are stored securely in a JSON file named `data.json`. Each entry in the JSON file contains the website URL as the key and the corresponding username/email and password as values.

## Error Handling

The script incorporates error handling mechanisms to address potential issues, such as JSON decoding errors and file not found errors. This ensures robustness and reliability in managing passwords.

## How to Use

To use the Password Manager application:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the `main.py` script.
4. Run the script using Python: `python main.py`.
5. The Password Manager application will launch, allowing you to generate, save, and search for passwords.

## Customization

You can customize the Password Manager application by modifying the password generation criteria, such as the length and complexity of generated passwords. Additionally, you can enhance the user interface by adjusting the layout and styling elements.

## Dependencies

This project requires the following dependencies:

- Python 3.11
- Tkinter library (included in standard Python distribution)

## Conclusion

The Password Manager application provides a convenient and secure solution for managing passwords, offering password generation, storage, and retrieval functionalities. By leveraging Python and Tkinter, users can enhance their password security and streamline their digital identity management.