from weather import Weather_object

class Weather_CMD:
    def __init__(self, city_id=None, output_mode='console'):
        self.ANS_YES = ('1', 'true', 'y', 'yes', 'yo', 'yop')
        self.object = Weather_object(city_id)

        if city_id is not None:
            self.object.city_id = city_id
        else:
            self.object.city_id = self.get_city_id()

        self.data = self.get_readable_data()
        self.output_mode = output_mode

    def ask_for_city(self):
        user_city = input('Enter a name of city: ')
        possible_cities = self.object.get_city_id(user_city)
        new_city_id = False
        for city in possible_cities:
            answer = input('Is {0}[{1}, {2}] your city? '.format(city[0], city[1], city[2]))
            if answer.rstrip().lstrip().lower() in self.ANS_YES:
                new_city_id = city[3]
                break

        if new_city_id == False:
            print('Your location is incorrect, check Syntax!')

        return new_city_id

    def get_city_id(self):
        maybe_id = self.ask_for_city()
        while maybe_id == False:
            again = input('Do you want to enter a location again? ')
            if again in self.ANS_YES:
                maybe_id = self.ask_for_city()
            else:
                print('Found not city, exiting program!')
                return False
        return maybe_id

    def get_readable_data(self):
        self.object.raw_data_func()
        data = self.object.get_readable_data()

        if data == False:
            print('A weather data for your city does not exist! Check city ID!')
            return False

        return data

def create_console_table(data):
    intro = [
        ('Place', ('city', 'country')),
        ('ID', 'id'),
        ('Coords', 'coord'),
        ('Updated', 'datetime'),
        ('Timezone', 'timezone'),
        ('Surise', 'sunrise'),
        ('Sunset', 'sunset'),
        ('Description', 'description'),
        ('Visibility', 'visibility'),
        ('Clouds', 'clouds'),
        ('Humidity', 'humidity'),
        ('Pressure', 'pressure'),
        ('Max temp', 'temp_max'),
        ('Temp', 'temp'),
        ('Min temp', 'temp_min'),
        ('Feels like', 'feels_like'),
        ('Wind speed', 'wind_speed'),
        ('Wind degree', 'wind_deg'),
        ('Rain last hour', 'rain_1h'),
        ('Snow last hour', 'snow_1h'),
        ('Rain last 3 hours', 'rain_3h'),
        ('Snow last 3 hours', 'snow_3h')
    ]

    pocet_okien = len(data) + 1
    pocet_stien = pocet_okien + 1
    dlzka = (pocet_okien * 25) + pocet_stien

    data.insert(0, intro)

    for row, item in enumerate(intro):
        first_line = ''
        if row == 0:
            first_line = '{0:_^{1}.{1}}'.format('', dlzka)
        else:
            first_line = '{0:-^{1}.{1}}'.format('', dlzka)
        print(first_line)

        for index, values in enumerate(data):
            second_line = '|'
            if index == 0:
                text = str('{0:^25.25}'.format(item[0]))
                second_line += text
            else:
                value = ''
                if isinstance(item[1], str):
                    value = values[item[1]]
                else:
                    for need in item[1]:
                        value += values[need]
                text = str('{0:^25.25}'.format(str(value)))
                second_line += text

                if index == len(data) - 1:
                    second_line += '|'

            print(second_line, end='')
        print(end='\n')

        if row == len(intro) - 1:
            print('{0:-^{1}.{1}}'.format('', dlzka))

number = input('Enter the number of cities you want to see... ')
inputs = []
if int(number) == 0:
    print('Okay, your problem, you dont want to see it.')
else:
    for i in range(int(number)):
        inputs.append(Weather_CMD().data)
    create_console_table([*inputs])
