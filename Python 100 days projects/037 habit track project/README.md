# Habit Track Project

This Python script interacts with the Pixela API to create a user, define a graph, and post values to the graph. Pixela is a habit tracking API that allows users to visualize and track their progress over time.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- Account on Pixela API
- Username and token for authentication

## Installation

1. Clone this repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Obtain your username and token from the Pixela API website.
4. Replace placeholders in the `usefulkeys.py` file with your username and token.

## Usage

1. Run the `main.py` script.
2. The script will create a new user on Pixela API using the provided token and username.
3. It will then define a graph named "Pages Read" to track the number of pages read.
4. After defining the graph, it will post a value to the graph, representing the number of pages read for the current date.
5. Make sure to update the quantity and date parameters in the `main.py` file whenever you want to post new values to the graph.

## Configuration

- You can modify the graph parameters such as name, unit, type, and color in the `main.py` file to track different habits or metrics.
- Ensure that your token and username are correctly configured in the `usefulkeys.py` file.

## Troubleshooting

- If you encounter any issues, double-check your token and username configuration.
- Ensure that you have agreed to the terms of service on the Pixela website.

## Disclaimer

This script is for demonstration purposes only. It provides basic functionality for interacting with the Pixela API and should be used responsibly.

