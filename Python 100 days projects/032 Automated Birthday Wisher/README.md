# Birthday Reminder and Email Sender

This Python project (folder Automated Birthday Wisher) serves as a reminder for birthdays stored in a CSV file (`birthdays.csv`). It checks if today's date matches any birthday in the file, generates a personalized birthday message using a template, and sends the message via email to the respective person.

## Project Overview

The project involves the following steps:

1. **Update Birthday Details**: Users are required to update the `birthdays.csv` file with their friends and family's birthday details. Each entry should include the person's name, birth month, and day.

2. **Check for Birthdays**: The script checks if today's date matches any birthday in the `birthdays.csv` file. It compares the month and day of today's date with those in the CSV file.

3. **Generate Birthday Message**: If there is a match, the script randomly selects a letter template from the `letter_templates` directory and replaces the `[NAME]` placeholder with the person's actual name from the CSV file.

4. **Send Email**: The personalized birthday message is sent via email to the respective person's email address. The script supports sending emails through SMTP servers such as Gmail, Yahoo, Hotmail, and Outlook.

## Educational Purpose

This project serves as an educational tool for Python learners to practice working with CSV files, datetime manipulation, string formatting, and email automation using libraries such as Pandas, datetime, smtplib, and random.

### Libraries Used:

- **Pandas**: Used for reading and manipulating CSV files containing birthday data.
- **datetime**: Utilized for retrieving today's date and comparing it with birthday dates.
- **smtplib**: Enables sending emails via SMTP servers. It provides functionality for establishing connections, logging in, and sending email messages.
- **random**: Used for selecting a random letter template for generating personalized birthday messages.

By working on this project, learners can gain hands-on experience in file handling, data manipulation, conditional statements, and email automation, which are essential skills for building real-world applications in Python.

## Instructions for Usage

1. Update the `birthdays.csv` file with the birthday details of friends and family.
2. Ensure that one of the entries in the CSV file matches today's date for testing purposes.
3. Run the script (`main.py`).
4. If today matches a birthday in the CSV file, a personalized birthday message will be generated and sent via email to the respective person.

## Conclusion

The Birthday Reminder and Email Sender project provides an interactive and practical learning experience for Python enthusiasts. By following the steps outlined in the project, users can deepen their understanding of file handling, datetime manipulation, conditional statements, and email automation while celebrating special occasions with their loved ones in a unique and personalized way.


## Weekly Motivational Email Sender

This Python script sends weekly motivational emails containing randomly selected quotes to inspire recipients at the beginning of each week. The project utilizes Python's `datetime`, `random`, and `smtplib` libraries to generate motivational messages and send them via email.

### Project Overview

The script performs the following tasks:

1. **Determining the Day of the Week**: It retrieves the current day of the week using the `datetime` module and maps it to the corresponding weekday name. This information is used to personalize the subject of the motivational email with the current day of the week.

2. **Selecting a Random Quote**: The script reads a text file (`quotes.txt`) containing a collection of motivational quotes. It randomly selects one quote from the file to include in the email content.

3. **Sending the Email**: Using the SMTP (Simple Mail Transfer Protocol) protocol and a configured email account, the script sends the motivational email to the designated recipient. It includes the selected quote in the email body and customizes the subject with the current day of the week.

### Educational Purpose

This project serves as an educational tool for Python learners to explore email automation, file handling, and random selection in Python. By working on this script, users can gain hands-on experience in utilizing Python libraries for sending emails, reading files, and incorporating randomness into their applications.

#### Libraries Used:

- **datetime**: Utilized for retrieving the current date and determining the day of the week.
- **random**: Used for selecting a random quote from the collection.
- **smtplib**: Enables sending email messages using SMTP servers, facilitating email automation.

### Instructions for Usage

1. Ensure that the necessary libraries (`datetime`, `random`, `smtplib`) are installed.
2. Create a text file named `quotes.txt` containing a list of motivational quotes, each on a separate line.
3. Replace placeholders in the script, such as email addresses and passwords, with your own credentials.
4. Run the `main.py` script to execute the program.
5. Check the designated email address to receive the weekly motivational email with a randomly selected quote.

### Conclusion

The Weekly Motivational Email Sender project provides a practical demonstration of email automation using Python. By automating the process of sending motivational messages, the script encourages users to start their week on a positive note and fosters personal growth and inspiration.
