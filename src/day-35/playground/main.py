import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API_KEY = "ecbd46bbdcedcbd3271c3868bbb07b43"
LATITUDE = 18.52043
LONGITUDE = 73.856743

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": WEATHER_API_KEY,
    "cnt": 4
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0])

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring Umbrella")

#############################################################################
############################ TWILIO INTEGRATION #############################

from twilio.rest import Client

account_sid = "AC6994b496f641dcc57234fce48b080bc9"
auth_token = "9626cc7eaa6cd9d2cac9ddad16e52704"

client = Client(account_sid, auth_token)
# message = client.messages.create(
#   from_='+12516510630',
#   body='Hello World!!',
#   to='+919545767032'
# )


if will_rain:
    print("Bring Umbrella")
    message = client.messages.create(
        from_="+12516510630",
        body="Bring Umbrella",
        to="+919545767032"
    )

    print(message.status)