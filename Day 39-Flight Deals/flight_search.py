import requests
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.iatacode = ''

    def get_destination_code(self,cityname):
        self.header = {
            'apikey': 'wEhQ3sWmZxSyDdWzQ_6C8nPAyZ59X9nc'
        }
        self.query = {
            'term': cityname,
            'location_type': 'airport'
        }
        response = requests.get(url=f'https://api.tequila.kiwi.com/locations/query', params=self.query,
                                headers=self.header)
        self.iatacode = response.json()['locations'][0]['code']
        return self.iatacode


FlightSearch()


