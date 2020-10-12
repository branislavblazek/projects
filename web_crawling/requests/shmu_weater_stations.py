import requests
from bs4 import BeautifulSoup

base_url = 'http://www.shmu.sk/sk/?page=1&id=hydro_vod_all&station_id=6340'
content = requests.get(base_url).content

soup = BeautifulSoup(content, "html.parser")
main_content = soup.find_all("div", id="maincontent")
centers = main_content[0].find_all("div", {"class": "tcenter"})

info_table, data_table = centers[1].find_all("table", {"class": "center"})
#spracuj nazov
riadky = info_table.find_all('tr')
for udaje in riadky:
    if udaje.find('b').text in ['Názov stanice:', 'Tok:', 'Región:', 'Oblasť:']:
        print(udaje.find_all('td')[1].text)

#spracuj data
riadky = data_table.find_all('tr')

for bunka in riadky:
    data_pre_riadok = []
    udaje = bunka.find_all('td')
    for udaj in udaje:
        data_pre_riadok.append(udaj.text)
    #vypis data
    print('|{:^20}|{:^15}|{:^20}|'.format(*data_pre_riadok))

print("Press any key to continue")
input()
