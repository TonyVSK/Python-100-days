# Caesar Cipher

The Caesar Cipher is a classic encryption technique that shifts the letters of a message by a fixed number of positions down the alphabet. This Python project implements the Caesar Cipher encryption and decryption functionalities. It showcases the use of functions, conditional statements, loops, and modular programming.

## Project Overview

The project consists of a single Python file:
- `caesar_cipher.py`: Contains functions for encoding and decoding messages using the Caesar Cipher, as well as the main program logic.

## Features

### 1. Encryption and Decryption Functions
- The `encode()` function encodes a message using the Caesar Cipher technique.
- The `decode()` function decodes an encoded message back to its original form.

### 2. Main Program Logic
- The main program prompts the user to choose between encoding or decoding a message.
- It accepts user input for the message and the shift number.
- Based on the user's choice, it either encodes or decodes the message using the specified shift number.

### 3. Modular Programming
- The functions for encoding and decoding are modularized for reusability and clarity of code.

### 4. User Interaction
- The program interacts with the user through command-line prompts, allowing them to input messages and shift numbers.

## How to Use

1. Run the `caesar_cipher.py` file.
2. Choose whether you want to encode or decode a message.
3. Enter the message you want to encrypt or decrypt.
4. Specify the shift number.
5. View the encoded/decoded message.

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3
The encode message is khoor
Type 'yes' if you want again. Otherwise type 'no':
no
End of program
```