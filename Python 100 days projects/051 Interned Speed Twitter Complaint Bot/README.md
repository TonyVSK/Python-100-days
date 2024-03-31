# Internet Speed Twitter Complaint Bot

This Python script (`main.py`) utilizes Selenium to perform an internet speed test on Speedtest.net and notifies about slow download speed on Twitter.

## Overview

The script performs the following tasks:
1. **Initializing Selenium WebDriver**:
   - It uses Selenium WebDriver with the Chrome browser to interact with the Speedtest.net website.
   - The Chrome browser remains open after the script finishes execution for further interaction.

2. **Accepting Site Cookies**:
   - It clicks on the "Accept" button to accept site cookies, if present.

3. **Starting Speed Test**:
   - It clicks on the "GO" button to start the speed test.

4. **Measuring Download Speed**:
   - It waits for the speed test to complete (approximately 35 seconds) and extracts the download speed from the results.

5. **Notification on Twitter**:
   - If the download speed is below 50 Mbps, it sends a notification to a Twitter account using Selenium WebDriver to automate the process.
   - It opens Twitter in a separate browser window, composes a tweet with the speed test result, and submits the tweet.

## Running the Script

To run the script:
1. Ensure you have the necessary Python packages installed, including `selenium` and `webdriver_manager`.
2. Make sure you have the latest version of Chrome installed on your system.
3. Update the `URL` variable in the script with the appropriate Speedtest.net URL.
4. Run the `main.py` script.
5. Sit back and watch as the script performs the internet speed test and notifies about slow download speed on Twitter!

## Limitations

Since this script interacts directly with Speedtest.net and Twitter's web interfaces, it may break if the structure of these websites' HTML changes. Additionally, automating interactions like this may violate the terms of service of these websites, so use it responsibly and at your own risk.

## Contributions

Contributions to this project, including bug fixes, feature enhancements, and documentation improvements, are welcome. If you have suggestions for improving the script or encounter any issues, feel free to open an issue or submit a pull request.