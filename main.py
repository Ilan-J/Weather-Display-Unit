import os
from dotenv import load_dotenv
from openweather import OpenWeather

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')



def run(openweather: OpenWeather):
    response = openweather.weather(48.499247, -2.73221)
    print(response)

if __name__ == '__main__':
    if OPEN_WEATHER_API_KEY == None or OPEN_WEATHER_API_KEY == '':
        print('Requires an Open Weather API Key to start!')
        exit(1)

    run(OpenWeather(OPEN_WEATHER_API_KEY, 'metric', 'fr'))
