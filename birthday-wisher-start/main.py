##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas
import random

my_email = "jerrypythontest@hotmail.com"
password = "zfxndwnrqqohfnjv"

now = dt.datetime.now()
month = now.month
day = now.day

df = pandas.read_csv("birthdays.csv")
birthday_record = df.to_dict(orient="records")

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(letters)

for birthday in birthday_record:
    if month == birthday["month"] and day == birthday["day"]:
        with open(f"letter_templates/{letter}") as letter_file:
            letter_contents = letter_file.read()
            updated_letter = letter_contents.replace("[NAME]", birthday["name"])
            print(updated_letter)
            with open(f"birthday_letter_for_{birthday["name"]}", mode="w") as completed_letter:
                completed_letter.write(updated_letter)

        with smtplib.SMTP("smtp-mail.outlook.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="jerrybang0203@hotmail.com",
                                msg=f"Subject:Happy Birthday!\n\n{updated_letter}")
