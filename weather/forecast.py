import json
import requests
from datetime import datetime
import unicodedata

class Forecast_object:
    def __init__(self, city_id=None):
        self.KEY = '9e2d94a63be352355ba3e7d78008bc95'
        self.ANS_YES = (1, 'true', 'y', 'yes', 'yo', 'yop')
        self.path_json = 'city.list.json'
        self.weather_data = None
        self.city_id = city_id
        self.link = self.__handle_link()
        self.raw_data = None

    def __repr__(self):
        return 'An Weather object for ' + str(self.city_id)

    def __handle_link(self):
        return 'http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}&units=metric'.format(self.city_id, self.KEY) if self.city_id is not None else None

    def get_city_id(self, city_name):
        """
        This gets an name of city, returns everything
        form list where is name of city as list
        """
        #edit city_name
        edit_str_one = lambda s: ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
        edit_str = lambda s: edit_str_one(s).strip().replace(' ', '').lower()

        city_name = edit_str(city_name)
        #return value
        possible_cities = set()
        #open file
        file_handler = open(self.path_json, mode='r', encoding='utf8')
        #make json file
        json_data = json.loads(file_handler.read())
        what_inpt = None

        for json_item in json_data:
            compare = edit_str(json_item['name'])
            if compare == city_name:
                possible_cities.add((json_item['country'], json_item['coord']['lon'], json_item['coord']['lat'], json_item['id']))

        return possible_cities

    def raw_data_func(self):
        self.link = self.__handle_link()
        self.weather_data = requests.get(self.link)
        self.weather_data = self.weather_data.json()
        self.raw_data = self.weather_data

    def read_time(self, timestamp, format='full'):
        format = format.lower()
        new_time = datetime.fromtimestamp(timestamp)
        xxx = new_time
        if format == 'full':
            #01.01.2020 09:30:57
            return xxx.strftime('%d.%m.%Y %H:%M:%S')
        elif format == 'short':
            #1.1.20 9:30
            return xxx.strftime('%d.%m. %H:%M')
        elif format == 'full_h':
            #01.01.2020 09
            return xxx.strftime('%d.%m.%Y %H')
        elif format == 'short_h':
            #1.1.20 9
            return xxx.strftime('%d.%m. %H').lstrip("0").replace(".0", ".").replace(" 0", " ")
        elif format == 'full_time':
            #09:30:57
            return xxx.strftime('%H:%M:%S')
        elif format == 'short_time':
            #9:30
            return xxx.strftime('%H:%M').lstrip("0")

    def get_readable_data(self):
        if self.raw_data['cod'] != '200':
            return False
        else:
            data = {}
            city = {
                'coord_lat': self.raw_data['city']['coord']['lat'],
                'coord_lon': self.raw_data['city']['coord']['lon'],
                'country': self.raw_data['city']['country'],
                'id': self.raw_data['city']['id'],
                'name': self.raw_data['city']['name'],
                'sunrise': self.raw_data['city']['sunrise'],
                'sunset': self.raw_data['city']['sunset'],
                'timezone': self.raw_data['city']['timezone']
            }
            forecast = []
            for item_forecast in self.raw_data['list']:
                short = item_forecast
                detail_forecast = {
                    'date': self.read_time(short['dt'], 'short'),
                    'temp': short['main']['temp'],
                    'feels_like': short['main']['feels_like'],
                    'temp_min': short['main']['temp_min'],
                    'temp_max': short['main']['temp_max'],
                    'pressure': short['main']['pressure'],
                    'sea_level': short['main']['sea_level'],
                    'humidity': short['main']['humidity'],
                    'description': short['weather'][0]['description'],
                    'clouds': short['clouds']['all'],
                    'wind_speed': short['wind']['speed'],
                    'wind_deg': short['wind']['deg'],
                    'rain': '-',
                    'snow': '-'
                }
                if 'rain' in item_forecast:
                    detail_forecast['rain'] = item_forecast['rain']['3h']
                if 'snow' in item_forecast:
                    detail_forecast['snow'] = item_forecast['snow']['3h']

                forecast.append(detail_forecast)

            data = {
                'city': city,
                'forecast': forecast
            }

            return data
