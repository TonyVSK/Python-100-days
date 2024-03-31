# Pomodoro Timer App

This repository contains a Python script that implements a Pomodoro timer application using the Tkinter library. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Introduction to Pomodoro Technique

The Pomodoro Technique involves breaking work into intervals, usually 25 minutes in length, called "pomodoros," followed by short breaks. After completing a set number of pomodoros, a longer break is taken. This method aims to improve productivity and focus by providing structured breaks during work sessions.

## Understanding the Script

The `main.py` script creates a Pomodoro timer application with the following features:

- **Timer Mechanism**: The application alternates between work sessions and breaks based on predefined time intervals. It displays a countdown timer indicating the time remaining for each session.
- **Countdown Mechanism**: The countdown mechanism updates the timer display every second and triggers the start of the next session or break upon completion.
- **UI Setup**: The user interface (UI) is built using Tkinter, featuring a canvas for displaying the timer, buttons for starting and resetting the timer, and a label for showing completed work sessions.
- **Buttons**: The "Start" button initiates the timer, while the "Reset" button resets the timer and clears the session history.
- **Session Tracking**: The application keeps track of completed work sessions and displays checkmarks for each session completed.

## How to Use

To use the Pomodoro Timer App:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the `main.py` script.
4. Run the script using Python: `python main.py`.
5. The Pomodoro timer application will launch, allowing you to start and reset the timer as needed.

## Customization

You can customize the Pomodoro timer application by adjusting the following constants defined in the script:

- `WORK_MIN`: Duration of the work session in minutes.
- `SHORT_BREAK_MIN`: Duration of the short break in minutes.
- `LONG_BREAK_MIN`: Duration of the long break in minutes.

Feel free to modify these constants to suit your preferences and work habits.

## Dependencies

This project requires the following dependencies:

- Python 3.11
- Tkinter library (included in standard Python distribution)

## Conclusion

The Pomodoro Timer App provides a simple yet effective tool for managing work sessions and breaks using the Pomodoro Technique. By leveraging the power of Python and Tkinter, users can enhance their productivity and focus while working on tasks or projects.