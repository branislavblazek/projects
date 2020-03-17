import requests
from bs4 import BeautifulSoup
import time

class Edupage:
    def __init__(self):
        self.session = None
        self.username = "BranislavBlazek"
        self.password = 'C232AELEMW'
        self.get_accces()

    def get_accces(self):
        login_url = 'https://gvoza.edupage.org/login/edubarLogin.php'

        #headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        #login data
        login_data = {
            "username": self.username,
            "password": self.password
        }

        #zoper auth kluc
        content = requests.get(login_url).content

        soup = BeautifulSoup(content, "html.parser")
        login_data['csrfauth'] = soup.find('input', attrs={'name': "csrfauth"})['value']

        self.session = requests.Session()
        self.session.post(login_url, data=login_data, headers=headers)

    def main_page(self):
        #ziskaj hlavnu stranku
        my_account = "https://gvoza.edupage.org/user/"
        content = self.session.get(my_account).content

    def my_account(self):
        account_url = 'https://gvoza.edupage.org/portal/?cmd=MyAccount'
        content = self.session.get(account_url).content

        soup = BeautifulSoup(content, "html.parser")
        field_list = soup.find_all('ul', {'accountBoxes'})

        for field in field_list:
            ludia = field.find_all('li')
            for clovek in ludia:
                if len(clovek.contents) == 0:
                    continue

                if len(clovek.find('h4').text.strip()) < 10:
                    print(clovek.find('h4').text.strip())
                else:
                    print('User')

                riadky = clovek.find_all('tr')
                for riadok in riadky:
                    obsah = []
                    bunka = riadok.find_all('td')
                    for info in bunka:
                        obsah.append(info.text)
                    print(obsah)


handler = Edupage()

#handler.my_account()