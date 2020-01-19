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

    def __repr__(self):
        if self.output_mode == 'console':
            for index, key in enumerate(self.data):
                first_line = ''
                if index == 0:
                    first_line = '{0:_^53.53}'.format('')
                else:
                    first_line = '{0:-^53.53}'.format('')
                print(first_line)
                second_line = '|'
                left = str('{0:^25.25}'.format(str(key)))
                second_line += left + '|'
                right = str('{0:^25.25}'.format(str(self.data[key])))
                second_line += right + '|'
                print(second_line)
                if index == len(self.data) - 1:
                    print('{0:-^53.53}'.format(''))
        return ''

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

console_data = Weather_CMD()
print(console_data)
