import requests
from bs4 import BeautifulSoup

base_url = 'https://moodle-old.gvoza.sk/user/view.php?id='
content = requests.get(base_url).content

for i in range(31):
    cislo = str(1815+i)
    content = requests.get(base_url+cislo).content
    soup = BeautifulSoup(content, "html.parser")
    main_div = soup.find('div', id='content')
    h2 = main_div.find('h2', 'main').text
    print(h2)