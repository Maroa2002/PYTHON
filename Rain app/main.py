import requests
import os
from twilio.rest import Client

account_sid = "AC06f908fe364c31a210ec2e1126488204"
auth_token = "12d3a5fbd5cabb198ee731d672893a85"

API_KEY = "#######################"
MY_LAT = -1.292066
MY_LONG = 36.821945
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
http_code = response.status_code
response.raise_for_status()

data = response.json()
hourly_data = data["hourly"]
sliced_data = hourly_data[:12]

will_rain = False

for hour_data in sliced_data:
    weather_code = hour_data["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to rain today so remember to bring an ☂ ",
        from_="+19379000381",
        to="+254738293178"
    )

print(message.status)

