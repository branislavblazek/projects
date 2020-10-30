from forecast import Forecast_object
import tkinter

class Forecast_GUI:
       def __init__(self, city_id=None):
              self.object = Forecast_object(city_id)

              if city_id is not None:
                     self.object.city_id = city_id
              else:
                     print('NENACITALO MI')

              self.data = self.get_readable_data()

       def get_readable_data(self):
              self.object.raw_data_func()
              data = self.object.get_readable_data()

              if data == False:
                     print('Nieco sa pokazilo!')
                     return False

              return data

class GUI_Window:
        def __init__(self, data):
                #mam vstupne raw data, treba ich zobrazit
                #vytvor graficke okno
                self.canvas = tkinter.Canvas(width=1200, height=600, bg='white')
                self.canvas.pack()
        
                #udaje o meste
                self.city = data['city']
                #udaje o predpovedi
                self.forecast = data['forecast']
                #formatovanie riadkov
                self.help_text = [
                        ('Dátum', 'date', 1, 5),
                        ('Popis', 'description', 1, 5),
                        ('Max', 'temp_max', 0, 1),
                        ('Tep', 'temp', 0, 1),
                        ('Min', 'temp_min', 0, 1),
                        ('Pocitova', 'feels_like', 0, 1),
                        ('Dážď', 'rain', 0, 2),
                        ('Sneh', 'snow', 0, 2),
                        ('Rýchlosť', 'wind_speed', 0, 3),
                        ('Smer', 'wind_deg', 0, 5),
                        ('Oblačnosť', 'clouds', 0, 0),
                        ('Tlak', 'pressure', 0, 4),
                        ('Vlhkosť', 'humidity', 0, 0),
                        ('Sea level', 'sea_level', 0, 4)
                ]
                self.exclude = ['sea_level', 'wind_deg', 'description']
                self.size = [11,15]
                self.symbols = ['%', '°', 'mm', 'met/sec', 'hPa', '']
                self.ids = []
                self.offsetTop = 0
                self.bottomScreen = -1
                self.kresli_obrazovku()
                self.scrollbars()
                self.canvas.bind('<Button-1>', self.clickOn)

        def kresli_obrazovku(self):
                offsetTop = self.offsetTop
                #horny informacny div
                self.ids.append(self.canvas.create_rectangle(0,offsetTop,1170,offsetTop+100,fill='green',outline=''))
                uvod_text = '5-dňová predpoveď pre {name} [{country}: LAT:{coord_lat} LON:{coord_lon}]'.format(**self.city)
                self.ids.append(self.canvas.create_text(600,offsetTop+50,text=uvod_text, font='arial 25', fill='white'))
                #sunset - rise
                self.ids.append(self.canvas.create_rectangle(0,offsetTop+100,1170,offsetTop+150,fill='silver',outline=''))
                slnko_text = 'slnko vychádza v tomto meste {sunrise} a zapadá {sunset}'.format(**self.city)
                self.ids.append(self.canvas.create_text(600,offsetTop+125,text=slnko_text, font='arial 20', fill='black'))
                #horny riadok
                name_line = ''
                for index0, name in enumerate(self.help_text):
                       if name[1] in self.exclude:
                               continue
                       name_line += '{0:^{1}.{1}}'.format(name[0], self.size[name[2]])
                self.ids.append(self.canvas.create_rectangle(35,offsetTop+160,1125,offsetTop+200,fill="silver", outline="black"))
                self.ids.append(self.canvas.create_text(600,offsetTop+180, text=name_line, font='arial 15', fill='black'))
               
               
                #hlavny loop
                start_at = 210
                he = 40
                spa = 10
                for row, item in enumerate(self.forecast):
                        info_line = ''
                        for index, helper in enumerate(self.help_text):
                                if helper[1] in self.exclude:
                                        continue
                                value = str(item[helper[1]])
                                value += self.symbols[helper[3]] if value is not '-' else ''
                                value = '{0: ^{1}}'.format(value, self.size[helper[2]])
                                
                                info_line += value
                        self.ids.append(self.canvas.create_rectangle(35,offsetTop+start_at+he*row,1125,offsetTop+start_at+he*row+he,fill="silver", outline="black"))
                        self.ids.append(self.canvas.create_text(600,offsetTop+start_at+he*row+he//2, text=info_line, font='arial 15'))
                        start_at += spa

                #paticka
                self.ids.append(self.canvas.create_rectangle(0, offsetTop+start_at+he*row+he+50,1170, offsetTop+start_at+he*row+he+115, fill='silver', outline='black'))
                self.ids.append(self.canvas.create_text(600,offsetTop+start_at+he*row+he+80, text='Vytvoril Branislav Blažek. Dáta sú z https://openweathermap.org/', font='arial 15'))
                self.bottomScreen = offsetTop+start_at+he*row+he+110
        
        def cisti_obrazovku(self):
                #ids su na to aby som mohol scrollovat
                self.canvas.delete(*self.ids)
                self.ids = []
        
        #ovladacie prvky
        def scrollbars(self):
                self.canvas.create_text(1185,17,text='▲', font='arial 30')
                self.canvas.create_text(1185,585,text='▼', font='arial 30')

        def clickOn(self, event):
                y = event.y
                x = event.x
                #je v prvom okienku
                if x >= 1170 and x <= 1200 and y >= 0 and y <= 30:
                        if self.offsetTop < 0:
                                self.offsetTop += 20
                                self.cisti_obrazovku()
                                self.kresli_obrazovku()
                elif x >= 1170 and x <= 1200 and y >= 270 and y <= 800:
                        if self.bottomScreen > 600:
                                self.offsetTop -= 20
                                self.cisti_obrazovku()
                                self.kresli_obrazovku()
        
x = Forecast_GUI(3056508).data
g = GUI_Window(x)
              
