# rain_alert
## Problem: Give a rain alert via SMS when it is going to rain in 12 hours
## Solutions

0. All the library needed for this project
```
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Need these for PythonAnywhere to run this script at 7 AM PST
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
```

1. Set up my Twilio API
```
account_sid = 'YOUR_Twilio_ID'
auth_token = os.environ.get("AUTH_TOKEN")
```

2. Get the weather data using OpenWeatherMap API
```
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
```
3. If the hour data's code is anything less than 700, alert me using Twilio API
```
will_rain = False
for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True
```

4. Send a SMS message
```
if will_rain:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring your umbrella.☔️",
        from_='YOUR TWILLO NUMBER',
        to='YOUR-PHONE-NUMBER'
    )
    print(message.status)
```
## Lessons
1. With a few line of codes, I can get a weather alert--what an amazing world we're living in!
2. Like Naval said, we're living in the age of automation--robot army is already here!
