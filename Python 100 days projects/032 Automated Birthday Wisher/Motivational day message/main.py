from random import choice
import datetime as dt
import smtplib


# Defining day of week
now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
weekDay = week[day_of_the_week]
print(weekDay)



# open txt file
with open("quotes.txt") as quotes:
    text = quotes.readlines()
    motivational_message =choice(text)

print(motivational_message)



# Email to send
my_email = "putyoursemailhere@email.com"
password = "useyourpasswordhere"
# # smtp-mail.outlook.com
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="putyoursecondemailhere@email.com", 
        msg=f"Subject:Happy {weekDay}!\n\n{motivational_message}"
    )
