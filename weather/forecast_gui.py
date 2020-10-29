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

def create_gui_window(data):
       #mam vstupne raw data, treba ich zobrazit
       #vytvor graficke okno
        canvas = tkinter.Canvas(width=1200, height=600, bg='white', scrollregion=(0,0,1200,600))
        canvas.pack()
        

       #udaje o meste
        city = data['city']

       #horny informacny div
        canvas.create_rectangle(0,0,1200,100,fill='green',outline='')
        uvod_text = '5-dňová predpoveď pre {name} [{country}: LAT:{coord_lat} LON:{coord_lon}]'.format(**city)
        canvas.create_text(600,50,text=uvod_text, font='arial 25', fill='white')
        #sunset - rise
        canvas.create_rectangle(0,100,1200,150,fill='silver',outline='')
        slnko_text = 'slnko vychádza v tomto meste {sunrise} a zapadá {sunset}'.format(**city)
        canvas.create_text(600,125,text=slnko_text, font='arial 20', fill='black')

        #formotovanie riadkov
        help_text = [
                ('Dátum', 'date', 1),
                ('Popis', 'description', 1),
                ('Max', 'temp_max', 0),
                ('Tep', 'temp', 0),
                ('Min', 'temp_min', 0),
                ('Pocitová', 'feels_like', 0),
                ('Dážď', 'rain', 0),
                ('Sneh', 'snow', 0),
                ('Rýchlosť', 'wind_speed', 0),
                ('Smer', 'wind_deg', 2),
                ('Oblačnosť', 'clouds', 2),
                ('Tlak', 'pressure', 0),
                ('Vlhkosť', 'humidity', 0),
                ('Sea level', 'sea_level', 0)
         ]
        size = [15,30,18]
        exclude = ['sea_level', 'feels_like', 'clouds', 'wind_deg', 'description']

       #horny riadok
        name_line = ''
        for index0, name in enumerate(help_text):
               if name[1] in exclude:
                       continue
               name_line += '{0:^{1}.{1}}'.format(name[0], size[name[2]])
        canvas.create_rectangle(50,160,1150,200,fill="silver", outline="black")
        canvas.create_text(600,180, text=name_line, font='arial 15', fill='black')
       
       #udaje o predpovedi
        forecast = data['forecast']
       #hlavny loop
        start_at = 210
        he = 40
        spa = 10
        for row, item in enumerate(forecast):
                info_line = ''
                for index, helper in enumerate(help_text):
                        if helper[1] in exclude:
                                continue
                        info_line += '{0:^{1}.{1}}'.format(str(item[helper[1]]), size[helper[2]])
                canvas.create_rectangle(50,start_at+he*row,1150,start_at+he*row+he,fill="silver", outline="black")
                canvas.create_text(600,start_at+he*row+he//2, text=info_line, font='arial 15')
                start_at += spa
                
        
x = Forecast_GUI(3056508).data
create_gui_window(x)
              
