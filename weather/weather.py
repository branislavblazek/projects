import json
import requests
#x = '{ "name":"John", "age":30, "city":"New York"}'
#y = json.loads(x)
#y['age']
from datetime import datetime
import unicodedata

class Weather_object:
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
        return 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}&units=metric'.format(self.city_id, self.KEY) if self.city_id is not None else None

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

    def get_readable_data(self):
        if self.raw_data['cod'] != 200:
            return False
        else:
            new_data = {
                'city': self.raw_data['name'],
                'country': self.raw_data['sys']['country'],
                'id': self.raw_data['id'],
                'coord': (self.raw_data['coord']['lat'], self.raw_data['coord']['lon']),
                'datetime': self.read_time(self.raw_data['dt']),
                'sunrise': self.read_time(self.raw_data['sys']['sunrise']),
                'sunset': self.read_time(self.raw_data['sys']['sunset']),
                'timezone': 'UTC + ' + str(int(self.raw_data['timezone'])//3600) + 'h',
                'visibility': self.raw_data['visibility'],
                'clouds': self.raw_data['clouds']['all'],
                'feels_like': self.raw_data['main']['feels_like'],
                'humidity': self.raw_data['main']['humidity'],
                'pressure': self.raw_data['main']['pressure'],
                'temp': self.raw_data['main']['temp'],
                'temp_max': self.raw_data['main']['temp_max'],
                'temp_min': self.raw_data['main']['temp_min'],
                'description': self.raw_data['weather'][0]['description'],
                'wind_speed': self.raw_data['wind']['speed'],
                'wind_deg': self.raw_data['wind']['deg'] if 'deg' in self.raw_data['wind'] else '-',
                'rain_1h': '-',
                'rain_3h': '-',
                'snow_1h': '-',
                'snow_3h': '-'
            }
            if 'rain' in self.raw_data:
                new_data['rain_1h'] = self.raw_data['rain']['1h'] if '1h' in self.raw_data['rain'] else '-',
                new_data['rain_3h'] = self.raw_data['rain']['3h'] if '3h' in self.raw_data['rain'] else '-'
            if 'snow' in self.raw_data:
                new_data['snow_1h'] = self.raw_data['snow']['1h'] if '1h' in self.raw_data['snow'] else '-',
                new_data['snow_3h'] = self.raw_data['snow']['3h'] if '3h' in self.raw_data['snow'] else '-'

        return new_data


    def read_time(self, timestamp):
        return datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y %H:%M:%S')
