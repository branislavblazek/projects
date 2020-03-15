from requests_html import HTMLSession

session = HTMLSession()
stranka = session.get('https://www.mall.sk/instantna-kava')

zoznam = stranka.html.find('#content section .product-list .lst-item')

for polozka in zoznam:
    data = polozka.find('.lst-product-item-body')[0]

    udaje = {'nazov': None, 'cena': None, 'prichod': None}

    name = data.find('div h3 a')[0].text
    udaje['nazov'] = name

    price = data.find('.lst-product-item-price .lst-product-item-price-value')[0].text
    udaje['cena'] = price

    availability = data.find('.lst-product-item-availability-wrapper div product-availability')[0].attrs['delivery-date']
    udaje['prichod'] = availability

    print(udaje)