import requests
import datetime
today = datetime.datetime.now().strftime('%d/%m/%Y')
print(today)
six_months = (datetime.datetime.now() + datetime.timedelta(6*30)).strftime('%d/%m/%Y')
print(six_months)
cityname = 'paris'
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.sheetyUrl = requests.get(url = 'https://api.sheety.co/40767c7e8ff1dd31c535d1b72985d67d/copyOfFlightDeals/prices')
        self.price = ''
        self.departure_airport_code= ''
        self.departure_city = 'paris'

    def return_data(self):
        return self.sheetyUrl.json()['prices']

    def check_price(self,destination_code,price,departure_city):
        self.header = {
            'apikey' : 'wEhQ3sWmZxSyDdWzQ_6C8nPAyZ59X9nc'
        }
        self.parameter = {
            'fly_from' : 'LON',
            'fly_to': destination_code,
            'date_from' : today,
            'date_to' : six_months
        }
        response = requests.get(url = 'https://api.tequila.kiwi.com/v2/search',headers=self.header,params=self.parameter)
        for i in response.json()['data']:
            if price < i['price']:
                return f'{i["cityTo"]} : {i["price"]}'


flight_data = FlightData()
flight_data.check_price()