import requests
from datetime import datetime
import smtplib
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude)
print(iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.
def iss_position_check():
    if MY_LAT-5 == -(iss_latitude) or MY_LAT + 5 == -(iss_latitude):
        return True
    elif MY_LAT-5 == (iss_latitude) or MY_LAT + 5 == (iss_latitude):
        return True


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

time_now = datetime.now().time()
print(iss_latitude)
print(iss_longitude)
print(sunset)
time_now = str(time_now).split(':')[0]
def check_night():
    if sunset<=time_now or time_now<=sunrise:
        return True

#If the ISS is close to my current position
if iss_position_check():

# and it is currently dark
    if check_night():
# Then send me an email to tell me to look up.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user='shankarnarayanan252525@gmail.com',
                             password='jwdbtubartqjuczm')
            connection.sendmail(from_addr='shankarnarayanan252525@gmail.com',
                            to_addrs='narayan.shankar.2506@gmail.com',
                            msg = "subject:ISS_OVERHEAD\n\njust look up in the sky")
# BONUS: run the code every 60 seconds.



