# import smtplib
#
# my_email = "softway_practice@gmail.com"
# my_password = "gbefunbotegaurus"
#
# # server = smtplib.SMTP("smtp.gmail.com", 587)
# # server.starttls()
# # server.login(user=my_email, password=my_password)
# # server.sendmail(from_addr=my_email,
# #                 to_addrs="softway_testing@yahoo.com",
# #                 msg="Subject: Hello\n\n This is the body of my email")
# # server.close()
#
#
# with smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.starttls()
#     server.login(user=my_email, password=my_password)
#     server.sendmail(
#         from_addr=my_email,
#         to_addrs="softway_testing@yahoo.com",
#         msg="Subject: Hello\n\n This is the body of my email"
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()

print(now)
print(year)
print(month)
print(day)
print(weekday)

date_of_birth = dt.datetime(year=1996,month=7,day=31)
print(date_of_birth)