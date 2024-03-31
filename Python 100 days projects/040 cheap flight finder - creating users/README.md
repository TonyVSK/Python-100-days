# Flight Price Tracker with Sheety and Twilio API Integration

This Python project is a flight price tracker that integrates the Sheety API for data storage, the Kiwi API (formerly known as SkyPicker) for obtaining flight price information, and the Twilio API for sending SMS notifications. It allows users to monitor flight prices for specific destinations and receive notifications via SMS when prices drop.

## APIs Used

### 1. Sheety API
The Sheety API facilitates interaction with Google Sheets, allowing developers to read and write data to spreadsheets programmatically. It provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on spreadsheet data.

#### How it Works
The script utilizes the Sheety API to store user information and flight price data in Google Sheets. It sends user details and flight prices to the Sheety API for storage.

### 2. Twilio API
The Twilio API allows developers to send and receive SMS messages programmatically. It provides functionality for sending notifications, alerts, and other messages via SMS.

#### How it Works
The script utilizes the Twilio API to send SMS notifications to users when flight prices drop below a specified threshold. It sends SMS messages containing details of the discounted flights to the users' phone numbers.

### 3. Kiwi API (formerly SkyPicker)
The Kiwi API provides flight information, including prices, availability, and route details. It offers endpoints for searching flights based on specific criteria such as origin, destination, and travel dates.

#### How it Works
The script uses the Kiwi API to search for flight prices to specific destinations. It sends requests to the API with destination city IATA codes and receives information about available flight prices.

## Installation and Usage

1. Clone this repository to your local machine.
2. Install the required libraries.
3. Obtain API credentials for the Sheety API, Twilio API, and the Kiwi API and update the `usefulkeys.py` file with the necessary information.
4. Run the `main.py` script.
5. Follow the prompts to input user information and desired flight destinations.
6. Check your email for confirmation of user registration and SMS notifications for discounted flight prices.

## Configuration

- Ensure your Sheety API, Twilio API, and Kiwi API credentials are correctly configured in the `usefulkeys.py` file.
- Customize the project name, spreadsheet name, and other settings as necessary.

## Disclaimer

This script is for demonstration purposes only. It provides basic functionality for tracking flight prices and sending SMS notifications using the Sheety, Twilio, and Kiwi APIs and should be used responsibly. Be sure to comply with the terms of service of the respective APIs.

If you need further assistance or customization options, feel free to reach out! Happy flying! 🛫✈️
