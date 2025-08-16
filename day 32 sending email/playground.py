# import smtplib
#
# # Generated app password
# # Your app password for your device
#
#
# myemail = "specter9x9x9x9@gmail.com"
# password = "wsks zpnn aajy zite"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=myemail, password=password)
#     # to add the subject to our email
#     # so in keyword argument we have to add Subject:whatever ourr subject is
#     # then by using the "\n\n " we can write the body of the message
#     connection.sendmail(from_addr=myemail,
#                         to_addrs="satya1729kumar@gmail.com",
#                         msg="Subject:hey\n\n hello Konichiwa"
#                         )
#     # connection.close()


# import datetime as dt
# # here now method gives the current date and time
# now = dt.datetime.now()
# print(type(now))
# year = now.year
# print(type(year),year)
#
# month =now.month
# print(month)
#
# day = now.day
# week = now.weekday()
# print(week,day)
#
# date_of_birth = dt.datetime(year=2002,month=5,day=10)
# print(date_of_birth)

with open("quotes.txt") as quotes:
    file = [quote.rstrip() for quote in quotes.readlines()]
    print(file)