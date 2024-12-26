import datetime as dt
import random
import smtplib

MY_EMAIL = "sebastiantestingenvironment@gmail.com"
MY_PASSWORD = "aiwy frmc vgeq tgfz"

class DayOfWeek:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def send_motivational_email() -> None:
    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == DayOfWeek.THURSDAY:
        with open('quotes.txt', 'r') as file:
            content = file.readlines()  # Reads all lines into a list
            quote = random.choice(content)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="morerasebas999@gmail.com",
                                msg=f"Subject:Motivation quote \n\n{quote}")
            connection.close()

if __name__ == '__main__':
    send_motivational_email()