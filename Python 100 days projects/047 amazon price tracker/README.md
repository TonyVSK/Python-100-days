# Amazon Price Tracker

This Python script (`main.py`) is designed to scrape the price of a specific product from Amazon and send an email notification if the price drops below a certain threshold.

## Overview

The script performs the following tasks:
1. **Scraping Amazon Product Page to Get Price**:
   - Utilizes web scraping techniques to retrieve the price of a specified product from its Amazon product page.
   - The URL of the product page is hardcoded in the script.
2. **Sending Email When Price Is Low**:
   - If the price of the product is below a specified threshold (in this case, $100), the script sends an email notification to the specified recipient(s) using SMTP (Simple Mail Transfer Protocol).
   - The sender's email address and password are hardcoded in the script for demonstration purposes. In a production environment, it's recommended to use environment variables or a more secure method for storing sensitive information.

## Web Scraping Process

Web scraping is the process of extracting data from websites. In this script:
- The `requests` library is used to fetch the HTML content of the Amazon product page.
- BeautifulSoup (`bs4`) is employed to parse the HTML content and extract the price of the product.

## Sending Email Notification

The script uses SMTP to send an email notification when the price of the product drops below the specified threshold. It sends a simple email message containing the product's price and a link to the product page on Amazon.

## Running the Script

To run the script:
1. Ensure you have the necessary Python packages installed, including `beautifulsoup4` and `requests`.
2. Update the `URL` variable in the script with the URL of the Amazon product page you want to monitor.
3. Replace the sender's email address (`my_email`) and password (`password`) with your own email credentials.
4. Run the `main.py` script.
5. If the price of the product drops below the specified threshold, an email notification will be sent to the recipient(s) specified in the script.

## Limitations

Web scraping can sometimes be fragile and may break if the structure of the website being scraped changes. Additionally, using web scraping to access data from websites may be subject to legal and ethical considerations, so it's essential to review and adhere to the website's terms of service and scraping policies.

## Contributions

Contributions to this project, including bug fixes, feature enhancements, and documentation improvements, are welcome. If you have suggestions for improving the script or encountering any issues, feel free to open an issue or submit a pull request.