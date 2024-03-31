# Cookie Clicker Automation

This Python script (`main.py`) uses Selenium to automate clicking cookies in the game "Cookie Clicker." It opens the game in a Chrome browser window and continuously clicks the cookie to earn cookies, as well as automatically purchases upgrades when enough cookies are accumulated.

## Overview

The script performs the following tasks:
1. **Initializing Selenium WebDriver**:
   - It uses Selenium WebDriver with the Chrome browser to interact with the "Cookie Clicker" web game.
   - The Chrome browser remains open after the script finishes execution for further interaction.

2. **Selecting Language and Handling Cookies**:
   - It selects the desired language (in this case, Portuguese-Brazil) and handles site cookies by clicking on the respective buttons on the game's landing page.

3. **Cookie Clicking Automation**:
   - The script continuously clicks the large cookie element on the game's interface to earn cookies.
   - It also automatically purchases upgrades (e.g., mouse clickers, grandmas) from the game's store when enough cookies are accumulated.

## Web Scraping Process

Web scraping is performed using Selenium WebDriver, which allows the script to interact with the game's web interface in a browser environment. The script locates elements by their XPath or CSS selector and performs actions such as clicking buttons and retrieving text.

## Running the Script

To run the script:
1. Ensure you have the necessary Python packages installed, including `selenium` and `webdriver_manager`.
2. Make sure you have the latest version of Chrome installed on your system.
3. Update the `URL` variable in the script with the URL of the "Cookie Clicker" game.
4. Run the `main.py` script.
5. Sit back and watch as the script automates clicking the cookie and purchasing upgrades in the game!

## Limitations

Since this script interacts directly with the game's web interface, it may break if the structure of the game's HTML changes. Additionally, automating game interactions like this may be against the terms of service of some games, so use it responsibly and at your own risk.

## Contributions

Contributions to this project, including bug fixes, feature enhancements, and documentation improvements, are welcome. If you have suggestions for improving the script or encounter any issues, feel free to open an issue or submit a pull request.