import requests
from bs4 import BeautifulSoup
import re
import json

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
        #niekedy nie je potrebne csrf auth
        #login_data['csrfauth'] = ''

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
                    print(''.join(obsah))

    def my_marks(self):
        marks_url = 'https://gvoza.edupage.org/znamky/?what=studentviewer&nadobdobie=P2&doRq=1&what=studentviewer&updateLastView=0'
        content = self.session.get(marks_url).content
        soup = BeautifulSoup(content, 'html.parser')
        scripts = soup.find_all('script', {'type': 'text/javascript'})
        scripts = [script for script in scripts if len(script.attrs) == 1]
        text_scriptu = scripts[2].text
        whole_obj = re.search(r"\"vsetkyZnamky\":(\[[^\[\]]+\])", text_scriptu).group(1)

        #toto dole zoberie nazvy predmetov
        subjects = re.search(r"\"predmety\":(.+?(?=}})}})", text_scriptu).group(1)
        predmety = json.loads(subjects)

        #toto berie ucitelov
        teachers = re.search(r"\"ucitelia\":(.+?(?=}})}})", text_scriptu).group(1)
        ucitelia = json.loads(teachers)
        
        #toto berie znamky
        marks = re.findall(r"\{[^\{\}]+\}", whole_obj)

        znamky = [json.loads(mark) for mark in marks]
        print('{:35} | {:^7} | {:<30} | {:^22} | {:}'.format('Prednet', 'Znamka', 'Meno ucitela', 'Datum vlozenia', 'Datum podpisania'))
        print('{0:_^35} | {0:_^7} | {0:_<30} | {0:_^22} | {0:_^22}'.format(''))
        for znamka in znamky:
            data = {}
            predmet = znamka['predmetid']
            data['predmet'] = predmety[predmet]['p_meno']
            data['hodnota'] = znamka['data']
            ucitel = znamka['ucitelid']
            data['ucitel'] = ucitelia[ucitel]['firstname'] + ' ' + ucitelia[ucitel]['lastname']
            data['datum'] = znamka['datum']
            data['podpisane'] = znamka['podpisane']
            print('{predmet:35} | {hodnota:^7} | {ucitel:30} | {datum:^22} | {podpisane:}'.format(**data))


        pass

handler = Edupage()

#handler.my_account()

handler.my_marks()

