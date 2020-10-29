import requests
from bs4 import BeautifulSoup

class Moodle:
    def __init__(self):
        self.session = None
        self.username = "b18blazek"
        self.password = ""
        self.anchor = ""
        self.logintoken = ""

    def get_acees(self):
        login_url = "https://moodle.gvoza.sk/login/index.php"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        login_data = {
            "username": self.username,
            "password": self.password
        }

        #zoper auth kluc
        content = requests.get(login_url).content

        soup = BeautifulSoup(content, "html.parser")
        login_data["logintoken"] = soup.find('input', attrs={'name':"logintoken"})["value"]

        self.session = requests.Session()
        self.session.post(login_url, data=login_data, headers=headers)
        pass

    def inf_ludka(self):
        page_url = "https://moodle.gvoza.sk/course/view.php?id=16"
        content = self.session.get(page_url).content

        soup = BeautifulSoup(content, "html.parser")
        pass


test = Moodle()
test.get_acees()