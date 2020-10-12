import requests
from bs4 import BeautifulSoup

base_url = 'https://www.strava.cz/strava/Stravnik/Prihlaseni'
content = requests.get(base_url).content

class Strava:
    def __init__(self):
        self.session = None
        self.login_url = 'https://www.strava.cz/strava/Stravnik/Prihlaseni'
        self.main_url = 'https://www.strava.cz/Strava/Stravnik/Uvod'
        self.connect()

    def connect(self):
        headers = {
            'Host': 'www.strava.cz',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'sk,cs;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '216',
            'Origin': 'https://www.strava.cz',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.strava.cz/Strava/Stravnik/prihlaseni',
            'Cookie': 'uzivatele=%5B%7B%22nazev%22%3A%22U%C5%BEivatel%201%22%2C%22jidelna%22%3A%22%22%2C%22jmeno%22%3A%22%22%7D%5D',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers'
        }
        login_data = {
            "zarizeni": 9083,
            "uzivatel": "Blaž7887",
            "heslo": "7887",
            "__VIEWSTATE": None,
            "__VIEWSTATEGENERATOR": None,
            "x": 98,
            "y": 26
        }
        content = requests.get(self.login_url).content
        soup = BeautifulSoup(content, "html.parser")
        login_data['__VIEWSTATE'] = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
        login_data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'name': '__VIEWSTATEGENERATOR'})['value']

        self.session = requests.Session()
        print('tu som')
        content = self.session.post(self.login_url, data=None, headers=headers).content
        print(content)
        c = self.session.get('https://www.strava.cz/Strava/Stravnik/Uvod').url
        print(c)

    def mainpage(self):
        content = self.session.get(self.main_url).content


scarper = Strava()
scarper.mainpage()