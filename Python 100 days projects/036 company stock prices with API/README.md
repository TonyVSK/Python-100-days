# Stock Analysis and News Notifier

This Python script retrieves stock price data and related news articles for a specified company. It uses the Alpha Vantage API to get stock price information and the News API to fetch news articles.

## Requirements

- Python 3.11
- `requests` library (`pip install requests`)
- Alpha Vantage API key
- News API key
- Email account for sending notifications

## Installation

1. Clone this repository to your local machine.
2. Install the required libraries.
3. Obtain API keys for Alpha Vantage and News API by signing up on their respective websites.
4. Replace placeholders in the `apikey.py` file with your API keys.
5. Set up an email account to send notifications. Update the email configuration in `main.py`.

## Usage

1. Run the `main.py` script.
2. The script will fetch the latest stock price data for the specified company (default: Tesla Inc).
3. It will compare the current stock price with the previous day's price. If there's a significant change, it will print corresponding news articles.
4. If there's a decrease in stock price beyond a certain threshold, it will send an email notification with the news articles.
5. If there's a notable increase in stock price, it will also send an email notification.

## Configuration

- You can change the default company and stock symbol in the `main.py` file.
- Adjust the threshold for significant changes in stock price according to your preferences.

## Troubleshooting

- Ensure that your API keys are correctly configured and have sufficient permissions.
- Check your email configuration to ensure that the script can send notifications successfully.

## Disclaimer

This script is for educational purposes only. It provides basic stock analysis and news notifications and should not be used for making financial decisions.