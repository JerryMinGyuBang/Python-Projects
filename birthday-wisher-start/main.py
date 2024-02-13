##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas

my_email = "jerrybang02@gmail.com"
password = "hxjdkeeezopyijyt"

now = dt.datetime.now()
month = now.month
day = now.day

df = pandas.read_csv("birthdays.csv")
birthday_record = df.to_dict(orient="records")
for birthday in birthday_record:
    if month == birthday["month"] and day == birthday["day"]:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday["email"], msg="hi")
