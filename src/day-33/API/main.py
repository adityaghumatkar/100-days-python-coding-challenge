import requests

# # ISS current location
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# # Kanye West Quotes
# k_response = requests.get(url="https://api.kanye.rest")
# k_response.raise_for_status()
#
# k_data = k_response.json()
# print(k_data)

import datetime as dt
import smtplib

now = dt.datetime.now()

MY_LAT = 51.507351
MY_LONG = -0.127758


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.now().hour
    if now >= sunset or now <= sunrise:
        return True


# ISS current location
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_lng <= MY_LONG + 5:
        return True

# SMTP configurations
my_email = "myemail@gmail.com"
password = "<dummy password>"

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="recieversemail@gmail.com",
                        msg="Subject: Look Up\n\n the ISS is above you in the sky."
                        )
    connection.close()