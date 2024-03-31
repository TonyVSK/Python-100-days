# NATO Phonetic Alphabet Converter

This repository contains a Python script that converts words into their corresponding NATO phonetic alphabet code words. It also demonstrates looping through dictionaries and data frames using the Pandas library.

## Structure

The repository includes the following files:

- **`main.py`**: The main Python script for converting words to NATO phonetic alphabet code words.
- **`nato_phonetic_alphabet.csv`**: A CSV file containing the NATO phonetic alphabet with letters and their corresponding code words.

## How It Works

1. The script reads the NATO phonetic alphabet data from the CSV file using the Pandas library and creates a dictionary in the format `{letter: code}`.
2. It prompts the user to input a word.
3. The script converts each letter of the word into its corresponding NATO phonetic code word using the dictionary.
4. It then prints the NATO phonetic code words for each letter of the input word.

## Running the Converter

To run the NATO Phonetic Alphabet Converter:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Ensure the CSV file `nato_phonetic_alphabet.csv` is in the same directory as the `main.py` script.
4. Open a terminal and navigate to the directory where the repository is cloned.
5. Run the `main.py` script using Python: `python main.py`.
6. Follow the on-screen instructions to input a word.
7. The script will print the NATO phonetic code words for each letter of the input word.

## Dependencies

This project requires the following dependencies:

- Python 3.11
- Pandas library

## Notes

- The NATO Phonetic Alphabet Converter provides a useful tool for converting words into their corresponding NATO phonetic code words, commonly used in communications to spell out words clearly.
- Users can customize or extend the code according to their needs, such as adding error handling or integrating it into larger projects.

Feel free to explore the code and experiment with different words to see their NATO phonetic equivalents.
