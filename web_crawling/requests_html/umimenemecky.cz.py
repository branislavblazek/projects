from requests_html import HTMLSession

session = HTMLSession()
stranka = session.get('https://www.umimenemecky.cz/diktaty-slovesa-sein-a-haben-preteritum-1-uroven/76')
stranka.html.render(sleep=3)

diktat = stranka.html.find("#dictate")[0]
spans = diktat.find('span[answered]')

for span in spans:
    varians = span.attrs['variants']
    prve, druhe, rozdiel = varians.split('|')
    if rozdiel == "01":
        print(druhe)
    elif rozdiel == "10":
        print(prve)