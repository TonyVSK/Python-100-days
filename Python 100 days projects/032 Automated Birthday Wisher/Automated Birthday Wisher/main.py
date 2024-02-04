##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import pandas
from random import choice
import datetime as dt
import smtplib


data = pandas.read_csv("./birthdays.csv")
person = data.to_dict(orient="records")



# Defining day of today
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


# Defining day of someone's birthday
data = pandas.read_csv("./birthdays.csv")
person = data.to_dict(orient="records")
name_of_person = person[0]['name']

if int(person[0]['day']) == int(day):
    # open txt file
    with open("./letter_templates/letter_1.txt") as file:
        text = file.read()
        novoTexto=text.replace('[NAME]', f'{name_of_person}')

        



    # # Email to send
    my_email = "putyouremailhere@email.com"
    password = "putyourapppasswordhere"
    # # smtp-mail.outlook.com
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="putyoursecondemailhere@email.com", 
            msg=f"Subject:Happy birthday!\n\n{novoTexto}"
        )
