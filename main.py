import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Twilio
account_sid = 'YOUR_Twilio_ID'
auth_token = os.environ.get("AUTH_TOKEN")

# Get the weather data using OpenWeatherMap API
api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": YOUR_LAT_INT,
    "lon": YOUR_LON_INT,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12] # This will get only 12 hours of weather data

# If the hour data's code is anything less than 700, alert me using Twilio API
will_rain = False
for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

# Send a SMS message
if will_rain:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring your umbrella.☔️",
        from_='YOUR TWILLO NUMBER',
        to='YOUR-PHONE-NUMBER'
    )
    print(message.status)

