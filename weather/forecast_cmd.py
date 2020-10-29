from forecast import Forecast_object

class Forecast_CMD:
    def __init__(self, city_id=None):
        self.ANS_YES = ('1', 'true', 'y', 'yes', 'yo', 'yop')
        self.object = Forecast_object(city_id)

        if city_id is not None:
            self.object.city_id = city_id
        else:
            self.object.city_id = self.get_city_id()

        self.data = self.get_readable_data()

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
    help_text = [
        ('Time', 'date', 1),
        ('Description', 'description', 1),
        ('Max temp', 'temp_max', 0),
        ('Temp', 'temp', 0),
        ('Min temp', 'temp_min', 0),
        ('Feels like', 'feels_like', 0),
        ('Rain', 'rain', 0),
        ('Snow', 'snow', 0),
        ('Wind speed', 'wind_speed', 0),
        ('wind deg', 'wind_deg', 2),
        ('Clouds', 'clouds', 2),
        ('Pressure', 'pressure', 0),
        ('Humidity', 'humidity', 0),
        ('Sea level', 'sea_level', 0)
    ]

    size = [10, 17, 6]

    city = data['city']
    intro_line_formula = '5-day forecast for {name}, {country}({id}); LAT: {coord_lat}, LON: {coord_lon}; Sun will rise at {sunrise} and set {sunset}; timezone is {timezone}'.format(**city)

    dlzka = 0
    for nic, nic2, value in help_text:
        dlzka += size[value]
    dlzka = dlzka + len(help_text) + 1

    forecast = data['forecast']

    up_line = '{0:_^{1}.{1}}'.format('', dlzka)
    intro_line = '|' + '{0:^{1}.{1}}'.format(intro_line_formula, dlzka-2) + '|'
    print(up_line)
    print(intro_line)
    down_line = list(up_line)
    down_line[0] = '|'
    down_line[-1] = '|'
    down_line = "".join(down_line)
    print(down_line)

    line_with_help = ''
    for index0, help in enumerate(help_text):
        help_line = '|'
        text = '{0:^{1}.{1}}'.format(help[0], size[help[2]])
        help_line += text
        if index0 == len(help_text)-1:
            help_line += '|'
        line_with_help += help_line
    print(line_with_help)

    for row, item in enumerate(forecast):
        first_line = '{0:-^{1}.{1}}'.format('', dlzka)
        print(first_line)

        for index, helper in enumerate(help_text):
            second_line = '|'
            text = '{0:^{1}.{1}}'.format(str(item[helper[1]]), size[helper[2]])
            second_line += text

            if index == len(help_text) - 1:
                second_line += '|'

            print(second_line, end='')

        print()

        if row == len(forecast)-1:
            print('{0:-^{1}.{1}}'.format('', dlzka))

    print(line_with_help)
    print('{0:-^{1}.{1}}'.format('', dlzka))

x = Forecast_CMD(3056508).data
create_console_table(x)
