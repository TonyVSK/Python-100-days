# Instagram Follower Automation Script

This Python script (`main.py`) automates the process of logging into Instagram, finding followers of a specified account, and following them. It utilizes Selenium WebDriver for web automation.

## Overview

The script consists of the following files:

- `main.py`: Contains the main script for Instagram follower automation.
- `instafollower.py`: Contains the `InstaFollower` class, which encapsulates methods for Instagram automation.
- `keyfiles.py`: Contains sensitive information such as email and password.

## Functionality

### `instafollower.py`

1. **InstaFollower Class**:
   - The class `InstaFollower` encapsulates methods for Instagram automation.

2. **Initialization**:
   - In the `__init__` method, a Selenium WebDriver is created using Chrome.
   - The WebDriver navigates to the Instagram login page.

3. **Login** (`login()`):
   - Enters the provided email and password in the login form and submits it.

4. **Find Followers** (`find_followers()`):
   - Navigates to the profile page of the specified Instagram account.
   - Clicks on the "Followers" tab to view the list of followers.

5. **Follow Users** (`follow()`):
   - Finds and clicks on the "Follow" button for each follower in the list.

### `main.py`

- Instantiates an `InstaFollower` object and calls its methods to perform Instagram follower automation.

### `keyfiles.py`

- Contains email and password information required for logging into Instagram. **Note:** Ensure to replace these with your actual Instagram credentials.

## Running the Script

1. Ensure you have the necessary Python packages installed, including `selenium` and `webdriver_manager`.
2. Make sure you have the latest version of Chrome installed on your system.
3. Update the `email` and `password` variables in `keyfiles.py` with your Instagram credentials.
4. Run the `main.py` script to start the Instagram follower automation process.

## Limitations

Since this script interacts directly with Instagram's web interface, it may break if the structure of the website's HTML changes. Additionally, automating interactions like this may violate Instagram's terms of service, so use it responsibly and at your own risk.

## Contributions

Contributions to this project, including bug fixes, feature enhancements, and documentation improvements, are welcome. If you have suggestions for improving the script or encounter any issues, feel free to open an issue or submit a pull request.