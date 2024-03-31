# Quizzler App with API Integration

This version of the Quizzler App is an enhanced version (project 017) that incorporates API requests to fetch quiz questions from an online source. It provides users with a more robust and dynamic quiz-taking experience by fetching real-time questions from an API instead of using pre-defined question sets.

## Project Overview

The Quizzler App with API Integration consists of several Python scripts, each serving a specific purpose:

1. **main.py**: This script orchestrates the flow of the application. It imports question data from an external API, creates question objects, initializes the quiz, and launches the user interface for quiz interaction.

2. **data.py**: This module retrieves question data from an external API using API requests. It fetches a set number of questions (10 in this case) with a boolean type.

3. **question_model.py**: Defines the `Question` class, representing individual quiz questions. Each question object contains the question text and the correct answer.

4. **quiz_brain.py**: Implements the `QuizBrain` class, which manages the quiz logic. It tracks the current question number, the user's score, and provides methods for fetching the next question and checking the user's answer.

5. **ui.py**: Constructs the graphical user interface (GUI) using the Tkinter library. It displays quiz questions and provides buttons for users to select true or false answers. Additionally, it dynamically updates the user's score as they progress through the quiz.

## Key Features

- **API Integration**: Utilizes API requests to fetch quiz questions from an online source, enhancing the quiz-taking experience with fresh and diverse question sets.
- **Dynamic UI**: Presents questions and options in a user-friendly graphical interface, allowing users to interact with the quiz seamlessly.
- **Real-time Score Tracking**: Updates the user's score dynamically as they answer questions, providing immediate feedback on their performance.

## Educational Value

This version of the Quizzler App offers valuable learning opportunities for Python developers, including:

- **API Integration**: Demonstrates the process of fetching data from external APIs and incorporating it into Python applications.
- **Dynamic GUI Creation**: Shows how to build interactive GUIs using Tkinter, a popular Python library for creating desktop applications.
- **Quiz Logic Implementation**: Illustrates how to implement quiz logic, including question handling and answer evaluation, in Python.

## Usage Instructions

1. Ensure that Python and the necessary libraries (`requests`, `tkinter`) are installed on your system.
2. Run the `main.py` script to launch the Quizzler App.
3. Interact with the graphical interface to answer quiz questions by selecting true or false options.
4. View your score at the end of the quiz and enjoy the dynamic quiz-taking experience.

## Conclusion

The Quizzler App with API Integration offers an engaging and educational way to explore API requests, GUI development, and quiz logic implementation in Python. By working on this project, developers can enhance their skills and create interactive applications with real-time data integration.
