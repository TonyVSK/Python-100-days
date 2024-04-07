# Morse Code Converter - First Project

This is a simple text-based Python program that converts strings into Morse Code.

## How it Works

The program uses a dictionary `morse` to map each letter of the alphabet (both uppercase and lowercase) and digits to their corresponding Morse Code representation. Additionally, it includes a mapping for space characters.

To convert a string into Morse Code, the program takes user input and converts each character of the input string to its Morse Code equivalent using the `morse` dictionary. The input string is converted to uppercase to ensure consistent mapping.

## Usage

1. Clone the repository or download the Python script.
2. Run the script using a Python interpreter.
3. Enter the text you want to convert into Morse Code when prompted.

## Example

```python
python morse_code_converter.py
```

```
    Write something: Hello, World!
    ....
    .
    .-..
    .-..
    ---
    .
    .-- 
    ---
    .-.
    .-.. 
    -..-
```
In the above example, the input "Hello, World!" is converted into Morse Code and printed character by character.