# Flight Price Tracker with Sheety API Integration

This Python project is a flight price tracker that integrates the Sheety API for data storage and the Kiwi API (formerly known as SkyPicker) for obtaining flight price information. It allows users to monitor flight prices for specific destinations and receive email notifications when prices drop.

## APIs Used

### 1. Sheety API
The Sheety API facilitates interaction with Google Sheets, allowing developers to read and write data to spreadsheets programmatically. It provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on spreadsheet data.

#### How it Works
The script utilizes the Sheety API to update a Google spreadsheet with the lowest flight prices found. It sends flight data, such as city IATA code and lowest price, to the spreadsheet.

### 2. Kiwi API (formerly SkyPicker)
The Kiwi API provides flight information, including prices, availability, and route details. It offers endpoints for searching flights based on specific criteria such as origin, destination, and travel dates.

#### How it Works
The script uses the Kiwi API to search for flight prices to specific destinations. It sends requests to the API with destination city IATA codes and receives information about available flight prices.

## Installation and Usage

1. Clone this repository to your local machine.
2. Install the required libraries.
3. Obtain API credentials for the Sheety API and the Kiwi API and update the `usefulkeys.py` file with the necessary information.
4. Run the `main.py` script.
5. Follow the prompts to input your travel details and desired dates.
6. Check your email to receive notifications about lower flight prices.

## Configuration

- Ensure your Sheety API and Kiwi API credentials are correctly configured in the `usefulkeys.py` file.
- Customize the project name, spreadsheet name, and other settings as necessary.

## Disclaimer

This script is for demonstration purposes only. It provides basic functionality for tracking flight prices and sending email notifications using the Sheety and Kiwi APIs and should be used responsibly. Be sure to comply with the terms of service of the respective APIs.

If you need further assistance or customization options, feel free to reach out 🛫✈️