# Fitness Tracker with Nutritionix and Sheety APIs

This Python script integrates two APIs, Nutritionix and Sheety, to create a fitness tracking application. The Nutritionix API is used to log exercises and retrieve their nutritional information, while the Sheety API is employed to store this data in a spreadsheet for further analysis.

## APIs in Use

### 1. Nutritionix API
The Nutritionix API provides nutrition and exercise data, allowing developers to build applications that track dietary intake and physical activity. It offers endpoints for natural language processing of exercises, enabling users to log workouts effortlessly.

#### How it Works
The script sends a POST request to the Nutritionix API's `/v2/natural/exercise` endpoint with exercise details provided by the user. The API processes the query and returns information such as exercise name, duration, and calories burned.

### 2. Sheety API
The Sheety API facilitates interaction with Google Sheets, enabling developers to read from and write to Google Sheets programmatically. It provides endpoints to perform CRUD operations on spreadsheet data.

#### How it Works
After retrieving exercise data from Nutritionix, the script sends a POST request to the Sheety API to add a new row containing the exercise details to a specified Google Sheets document. Subsequently, it sends a GET request to fetch the updated spreadsheet data for verification.

## Installation and Usage

1. Clone this repository to your local machine.
2. Install the required libraries.
3. Obtain API credentials for Nutritionix and Sheety APIs and update the `usefulkeys.py` file with the necessary information.
4. Run the `main.py` script.
5. Follow the prompts to input your workout details.
6. View the updated spreadsheet to see the logged exercise data.

## Configuration

- Ensure that your Nutritionix and Sheety API credentials are correctly configured in the `usefulkeys.py` file.
- Customize the Google Sheets document name, project name, and sheet name according to your preferences.

## Disclaimer

This script is for demonstration purposes only. It provides basic functionality for logging exercises using the Nutritionix and Sheety APIs and should be used responsibly. Make sure to comply with the terms of service of the respective APIs.

Feel free to reach out for further assistance or customization options. Happy tracking!
