import requests
from bs4 import BeautifulSoup

base_url = 'https://www.umimenemecky.cz/diktaty-slovesa-sein-a-haben-preteritum-1-uroven/77'
content = requests.get(base_url).content

soup = BeautifulSoup(content, "html.parser")
main_content = soup.find('div', id='dictate')
spans = main_content.find_all('span')
print()