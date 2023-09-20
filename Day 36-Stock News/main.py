import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


from twilio.rest import Client

account_sid = 
auth_token = 
client = Client(account_sid, auth_token)

paramter1 = {'apiKey':,
             'qInTitle': COMPANY_NAME}
parameter = {
'function':'TIME_SERIES_DAILY',
'symbol' : STOCK_NAME,
'apikey' : 
}


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(url=STOCK_ENDPOINT,params=parameter)
data = response.json()['Time Series (Daily)']

values = [value['4. close'] for (key,value) in data.items()]

yesterday  = int(float(values[0]))

d_yesterday = int(float(values[1]))
result = yesterday-d_yesterday
if result < 0:
    downfall = '🔻'
else:
    downfall = '🔺'
result = abs(result)
percentage = (( yesterday - d_yesterday) / d_yesterday ) * 100

percentage = 6
if percentage >= 5:
    print("Get News")
    response = requests.get(url=NEWS_ENDPOINT, params=paramter1)
    data = response.json()
    print(data)
    print(data['articles'][1:3])
    print(response.status_code)

    data_lst_comp = [f"{COMPANY_NAME} {downfall} \nHeadline: {i['title']} \nBreif: {i['description']}" for i in data['articles'][0:3]]

    for i in data_lst_comp:
        message = client.messages.create(
            from_=,
            to=,
            body= i)

