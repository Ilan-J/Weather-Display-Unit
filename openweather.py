import json
from httpcore import request, Response
from typing import List, Literal

class OpenWeather():
    def __init__(
            self,
            apikey,
            units: Literal['standard', 'metric', 'imperial'] = 'standard',
            lang: str = 'en'
        ) -> None:

        self.apikey = apikey
        self.units = units
        self.lang = lang

        self.url = 'https://api.openweathermap.org'

    def get(self, path: str, lat: float, lon: float, /, *params: str) -> Response:
        parameters = [
            f'appid={self.apikey}',
            f'units={self.units}',
            f'lang={self.lang}',
            f'lat={lat}',
            f'lon={lon}'
        ]
        for param in params:
            parameters.append(param)
        
        print(f'Sending request to Open Weather: "{self.url}/{path}" ({lat}, {lon})')

        return request('GET', f'{self.url}/{path}?{'&'.join(parameters)}')

    def forcast5(self, lat: float, lon: float, /):
        response = self.get('data/2.5/forecast', lat, lon)
        return response.read().decode()

    def weather(self, lat: float, lon: float, /):
        response = self.get('data/2.5/weather', lat, lon)

        response = json.loads(response.read())
        print(json.dumps(response, indent=2))
        return response

    def onecall(
            self,
            lat: float, lon: float,
            exclude: List[Literal['current', 'minutely', 'hourly', 'daily', 'alerts']] = [],
            /
        ):
        if exclude != []:
            param = f'exclude={','.join(exclude)}'
            response = self.get('data/3.0/onecall', lat, lon, param)
        else:
            response = self.get('data/3.0/onecall', lat, lon)
        
        response.status
        json.loads(response.read())
    