import datetime as dt
import random

import pandas as pd
import smtplib

MY_EMAIL = "sebastiantestingenvironment@gmail.com"
MY_PASSWORD = "aiwy frmc vgeq tgfz"


def birthday_wisher() -> None:
    today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
    data = pd.read_csv("birthdays.csv")
    birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{content}")
            connection.close()


if __name__ == '__main__':
    birthday_wisher()
