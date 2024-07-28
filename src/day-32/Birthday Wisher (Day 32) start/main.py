# import smtplib

# SMTP_URL = "smtp.gmail.com"
# my_email = "testsendermail@gmail.com"
# password = "<passwordRemoved>"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="testreceivermail@gmail.com",
#                     msg="Subject:Hello\n\nThis is mail body of my email")
# connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# print(type(now))
#
# dat_of_birth = dt.datetime(year=1997, month=4, day=15, hour=4)
# print(dat_of_birth)

import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        # print(quotes_list)

    monday_quote = random.choice(quotes_list)
    print(monday_quote)

    SMTP_URL = "smtp.gmail.com"
    my_email = "testsendermail@gmail.com"
    password = "<passwordRemoved>"

    connection = smtplib.SMTP(SMTP_URL)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="testreceivermail@gmail.com",
                        msg=f"Subject:Monday Motivational Quote\n\n{monday_quote}")
    connection.close()