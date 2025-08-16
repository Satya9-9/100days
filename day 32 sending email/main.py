import datetime as dt
import random
import smtplib

myemail = "specter9x9x9x9@gmail.com"
password = "wsks zpnn aajy zite"


now = dt.datetime.now()
curr_Day = now.weekday()
print(curr_Day)



day_of_quote = 5
# if wekday is friday then it will send me email
if day_of_quote == curr_Day:
    with open("quotes.txt") as quotes:
        all_quotes = [quote.rstrip() for quote in quotes.readlines()]
        print(all_quotes)

    random_quote = random.choice(all_quotes)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myemail, password=password)
        # to add the subject to our email
        # so in keyword argument we have to add Subject:whatever ourr subject is
        # then by using the "\n\n " we can write the body of the message
        connection.sendmail(from_addr=myemail,
                            to_addrs="satya1729kumar@gmail.com",
                            msg=f"Subject:Quote\n\n{random_quote}"
                            )