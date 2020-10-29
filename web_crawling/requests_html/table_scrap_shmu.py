from requests_html import HTMLSession

session = HTMLSession()
stranka = session.get('http://www.shmu.sk/sk/?page=1&id=hydro_vod_all&station_id=6340')

info_table, data_table = stranka.html.find('#maincontent .tcenter table')

#spracuj nazov
riadok = info_table.find('tr')

for udaje in riadok:
    if udaje.find('b')[0].text in ['Názov stanice:', 'Tok:', 'Región:', 'Oblasť:']:
        print(udaje.find('td')[1].text)

#spracuj data
riadok = data_table.find('tr')

for bunka in riadok:
    data_pre_riadok = []
    udaje = bunka.find('td')
    for udaj in udaje:
        data_pre_riadok.append(udaj.text)
    #vypis data
    print('|{:^20}|{:^15}|{:^20}|'.format(*data_pre_riadok))


pass