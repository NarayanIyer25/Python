
import requests
from twilio.rest import Client


client = Client(account_sid, auth_token)



OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall?'
parameter = {
    'lat': 51.507351,
    'lon': -0.127758,
    'exclude': "current,minutely,daily"
}
response = requests.get(OWM_ENDPOINT,params=parameter)
print(response.json())
hour_data = response.json()['hourly']
weather_data = []
for i in range(len(hour_data)):
    if i<=12:
        weather_data.append(hour_data[i]['weather'])
boolean = False
for i in weather_data:
    value = i[0]['id']
    if int(value)<700:
        boolean = True
val = ''
if boolean:
    val = "Bring Your Umbrella"
message = client.messages.create(
  from_=,
  to=',
  body= val
)
