from bs4 import BeautifulSoup
import requests
import wget

#base url
base_url = lambda link: 'http://www.shmu.sk/{0}'.format(link)
aladin_data = lambda city: 'sk/?page=1&id=meteo_num_mgram&nwp_mesto={0}'.format(city)
city = 31920

full_link = base_url(aladin_data(city))

content = requests.get(full_link).content

soup = BeautifulSoup(content, "html.parser")
image = soup.find("img", id="imageArea")
image_src = image['src']

print('Downloading...')
aladin = wget.download(base_url(image_src))
