import datetime

import requests
import datetime
today = datetime.datetime.today()
print(today)
graphid = 'graph1'
pixela_endpoint = "https://pixe.la/v1/users"
username = 'avenger'
token = 'hjhjhjhjhdlkhifkl'
body = {
    'token' : token,
    'username' : username,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}
response = requests.post(url=pixela_endpoint,json=body)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id" : graphid,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : 'momiji'
}
headers = {
    'X-USER-TOKEN' : token
}
response1 = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response1.text)

body2={
    'date' : today.strftime('%Y%m%d'),
    'quantity' : '15'
}

graph_endpoint_post = f'{graph_endpoint}/{graphid}'

response2 = requests.post(url=graph_endpoint_post,json=body2,headers=headers)
print(response2.text)
body3 = {
    'quantity' : input("Enter KM: ")
}
graph_endpoint_put = f'{graph_endpoint_post}/{today.strftime("%Y%m%d")}'
response3 = requests.put(url=graph_endpoint_put,json=body3,headers=headers)
print(response3.text)
print(graph_endpoint_put)

'''response4 = requests.delete(url=graph_endpoint_put,headers=headers)
print(response4.text)'''
'https://pixe.la/v1/users/avenger/graphs/graph1'