##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv - Done

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import smtplib

# Get today's date, month
now = dt.datetime.now()
day = now.day
month = now.month

# SMTP configurations
my_email = "myemail@gmail.com"
password = "<dummy password>"

df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    if row["month"] == month and row["day"] == day:
        letter_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt") as letter:
            letter_content = letter.read()
            updated_letter = letter_content.replace("[NAME]", row["name"])

        # send email over smtp
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=row["email"],
                            msg=f"Subject: Happy Birthday\n\n{updated_letter}"
                            )
        connection.close()
