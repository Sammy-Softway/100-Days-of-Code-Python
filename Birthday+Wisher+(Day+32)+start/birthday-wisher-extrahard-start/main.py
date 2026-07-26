import pandas
import datetime as dt
import random
import smtplib
##################### Extra Hard Starting Project ######################

MY_EMAIL = "softway_practice@gmail.com"
MY_PASSWORD = "gbefunbotegaurus"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

fam_dict = {(row.month, row.day): {"name": row["name"], "email": row.email}
            for (index, row) in data.iterrows()}

if today_tuple in fam_dict:
    fam_name = fam_dict[today_tuple]["name"]
    fam_email = fam_dict[today_tuple]["email"]

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
        letter = file.read()
        personalized_letter = letter.replace("[NAME]", str(fam_name))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=str(fam_email),
            msg=f"Subject: Happy Birthday!\n\n{personalized_letter}"
        )

# for index,row in data.iterrows():
#     fam_name = row["name"]
#     fam_email = row.email
#     fam_month = row.month
#     fam_day = row.day
#
#     # 2. Check if today matches a birthday in the birthdays.csv
#     if fam_month == now.month and fam_day == now.day:
#         letter_options = [
#             "letter_templates/letter_1.txt",
#             "letter_templates/letter_2.txt",
#             "letter_templates/letter_3.txt",
#         ]
#         # 3. If step 2 is true, pick a random letter from letter templates and
#         # replace the [NAME] with the person's actual name from birthdays.csv
#         chosen_letter = random.choice(letter_options)
#         with open(chosen_letter, "r") as file:
#             letter = file.read()
#             personalized_letter = letter.replace("[NAME]", fam_name)
#
#         # 4. Send the letter generated in step 3 to that person's email address.
#
#         with smtplib.SMTP("smtp.gmail.com") as connection:
#             connection.starttls()
#             connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#             connection.sendmail(
#                 from_addr=MY_EMAIL,
#                 to_addrs=fam_email,
#                 msg=f"Subject: Happy Birthday!\n\n{personalized_letter}"
#             )