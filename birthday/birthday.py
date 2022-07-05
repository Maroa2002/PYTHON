import datetime as dt
import pandas
import random
import smtplib

sender_email = "matikomaroa10@gmail.com"
password = "########"
recipient_email = "matikomaroa10@yahoo.com"

today = dt.datetime.now()
today_month = today.month
today_day = today.day
today_details = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_details in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as random_letter:
        birthday_person = birthdays_dict[today_details]
        letter = random_letter.read()
        new_letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"SUBJECT:Happy Birthday\n\n{new_letter}"
                            )
