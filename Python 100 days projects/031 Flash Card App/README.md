# Flash Card App

This repository contains a Python script for a Flash Card application built using the Tkinter library. The application helps users learn and memorize vocabulary using a digital flash card interface. It reads vocabulary data from a CSV file, displays a random flash card with French words, and allows users to test their knowledge by flipping the card and indicating whether they know the English translation.

## Introduction to Flash Card App

A Flash Card App is a software tool that enables users to study and memorize information using digital flash cards. It is commonly used for language learning, vocabulary building, and reviewing key concepts in various subjects. Flash card apps offer an interactive and engaging learning experience, allowing users to test their knowledge and track their progress.

## Understanding the Script

The `main.py` script implements a Flash Card application with the following features:

- **CSV Data Handling**: The application reads vocabulary data from a CSV file containing French words and their English translations. If the specified CSV file (`words_to_learn.csv`) is not found, it defaults to using a pre-defined CSV file (`french_words.csv`).
- **Flash Card Display**: The application displays a random flash card with a French word on the front side and its English translation on the back side.
- **Flip Card Functionality**: Users can flip the flash card to reveal the English translation of the displayed French word.
- **Knowledge Assessment**: Users can indicate whether they know the English translation of the displayed French word by clicking on buttons representing "Wrong" or "Right" answers.
- **Data Persistence**: Upon selecting the "Right" answer, the flash card is removed from the list of words to learn, and the updated vocabulary data is saved back to the CSV file (`words_to_learn.csv`).

## Flash Card Interaction

- **Next Card**: Clicking the "Wrong" button displays the next random flash card.
- **Known Word**: Clicking the "Right" button removes the current flash card from the list of words to learn and displays the next random flash card.

## User Interface

The Flash Card application features a simple and intuitive user interface with the following elements:

- **Canvas Display**: The flash card is displayed on a canvas widget, showing the French word on the front side and the English translation on the back side.
- **Navigation Buttons**: Two buttons labeled "Wrong" and "Right" allow users to indicate their knowledge of the displayed word.

## Dependencies

This project requires the following dependencies:

- Python 3.11
- Tkinter library (included in standard Python distribution)
- Pandas library

## Conclusion

The Flash Card application provides an effective and efficient method for learning and memorizing vocabulary. By leveraging Python and Tkinter, users can enhance their language skills in a fun and interactive way. The application's intuitive interface and functionality make it suitable for learners of all levels, from beginners to advanced users.
