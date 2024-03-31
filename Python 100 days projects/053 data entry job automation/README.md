# Data Entry Job Automation: Zillow Clone Data Scraper and Form Filler

This Python script (`main.py`) scrapes data from a Zillow clone website and uses Selenium WebDriver to fill out a Google Form with the scraped data.

## Overview

The script consists of the following functionality:

- Scraping house address, prices, and links from a Zillow clone website (`URL`).
- Using Selenium WebDriver to fill out a Google Form (`URL`) with the scraped data.

## Functionality

### Scraping Zillow Clone Data

1. **House Address**:
   - Scrapes house addresses from the Zillow clone website.
   - The addresses are extracted from the anchor tags with class `StyledPropertyCardDataArea-anchor`.

2. **House Prices**:
   - Scrapes house prices from the Zillow clone website.
   - The prices are extracted from elements with class `PropertyCardWrapper`.

3. **House Links**:
   - Scrapes links to house listings from the Zillow clone website.
   - The links are extracted from anchor tags with class `StyledPropertyCardDataArea-anchor`.

### Filling Google Form

1. **Initialization**:
   - Opens the Google Form specified by `URL`.

2. **Form Filling**:
   - Iterates through each scraped house address, price, and link.
   - Enters the data into the corresponding input fields of the Google Form.
   - Submits the form.

## Running the Script

1. Ensure you have the necessary Python packages installed, including `BeautifulSoup`, `requests`, and `selenium`.
2. Make sure you have the latest version of Chrome installed on your system.
3. Update the `URL` variable with the link to the Zillow clone website and the Google Form link (`URL`).
4. Run the `main.py` script to start the scraping and form filling process.

## Limitations

- The script may need adjustments if the structure of the Zillow clone website or the Google Form changes.
- Ensure proper permissions and ethical use when scraping data from websites.

## Contributions

Contributions to this project, including bug fixes, feature enhancements, and documentation improvements, are welcome. If you have suggestions for improving the script or encounter any issues, feel free to open an issue or submit a pull request.