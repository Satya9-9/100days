import smtplib
import time
from operator import truediv

import requests
from datetime import datetime

MY_LAT = 26.218287 # Your latitude
MY_LONG = 78.182831 # Your longitude
myemail = "specter9x9x9x9@gmail.com"
password = "wsks zpnn aajy zite"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT -5 <= iss_latitude <= MY_LAT+5 and MY_LONG -5 <= iss_latitude <= MY_LONG+5):
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now>=sunset or time_now <=sunrise:
        return True

#If the ISS is close to my current position
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection= smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=myemail, password=password)
        # to add the subject to our email
        # so in keyword argument we have to add Subject:whatever ourr subject is
        # then by using the "\n\n " we can write the body of the message
        connection.sendmail(from_addr=myemail,
                            to_addrs="satya1729kumar@gmail.com",
                            msg=f"Subject:Look UP\n\nISS above us"
                            )
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



