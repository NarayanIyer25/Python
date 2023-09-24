import requests
import datetime
from requests.auth import HTTPBasicAuth
date = datetime.datetime.today().strftime("%d/%m/%Y")
time = datetime.datetime.now().time().strftime("%I:%M:%S")
print(date,time)
APP_ID = '700a7b16'
API_KEY = '57c603809ae64f2b0436b184d3481d2b'
nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
gender = 'male'
weight = 72.5
height = 167.34
age = 27

excercise_input = input("Tell me what excericse you did ? ")
header = {
    'x-app-id': APP_ID,
    'x-app-key':API_KEY,
    'x-remote-user-id' : '6694fedb-f567-4e6b-911a-0b8ed8a13679'
}
parameter =  {
 "query":excercise_input,
 "gender":gender,
 "weight_kg":weight,
 "height_cm":height,
 "age":age
}
response = requests.post(url = nutri_endpoint ,headers= header,json=parameter)
answer = response.json()['exercises']

header1 = {
    'Authorization': 'Bearer U2hhbmthciA6QXBhY2hlQDIwMjI='
}

sheet_endpoint = 'https://api.sheety.co/40767c7e8ff1dd31c535d1b72985d67d/copyOfMyWorkouts/workouts'


for i in answer:
    parameter1 = {
        'workout':{
        'date': date,
        'time': time,
        'exercise': i['name'].title(),
        'duration': i['duration_min'],
        'calories': i['nf_calories'],
        }
    }
    response2 = requests.post(url=sheet_endpoint,json=parameter1,headers=header1)
    print(response2.json())


