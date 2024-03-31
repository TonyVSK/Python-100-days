# Auto Tinder Swiping Bot

This Python script (`main.py`) utilizes Selenium to automate interactions on the Tinder website. It automatically logs in to Tinder using Facebook, allows location access, handles notifications, accepts site cookies, and continuously likes profiles.

## Overview

The script performs the following tasks:
1. **Initializing Selenium WebDriver**:
   - It uses Selenium WebDriver with the Chrome browser to interact with the Tinder website.
   - The Chrome browser remains open after the script finishes execution for further interaction.

2. **Logging In to Tinder**:
   - It clicks on the "Login" button and then on the "Sign in with Facebook" button to log in to Tinder using Facebook credentials.

3. **Handling Location Access and Notifications**:
   - It allows access to location and handles notifications by clicking on the respective buttons.

4. **Accepting Site Cookies**:
   - It clicks on the "Allow all cookies" button to accept site cookies.

5. **Liking Profiles**:
   - It continuously clicks on the "Like" button to like profiles. The loop iterates 100 times, as there's a limit of 100 profiles per day.

## Web Scraping Process

Web scraping is performed using Selenium WebDriver, allowing the script to interact with Tinder's web interface in a browser environment. The script locates elements by their XPath and performs actions such as clicking buttons.

## Running the Script

To run the script:
1. Ensure you have the necessary Python packages installed, including `selenium` and `webdriver_manager`.
2. Make sure you have the latest version of Chrome installed on your system.
3. Update the `URL` variable in the script with the appropriate Tinder URL.
4. Run the `main.py` script.
5. Sit back and watch as the script automates interactions on Tinder!

## Limitations

Since this script interacts directly with Tinder's web interface, it may break if the structure of Tinder's HTML changes. Additionally, automating interactions like this may violate Tinder's terms of service, so use it responsibly and at your own risk.

## Contributions

Contributions to this project, including bug fixes, feature enhancements, and documentation improvements, are welcome. If you have suggestions for improving the script or encounter any issues, feel free to open an issue or submit a pull request.