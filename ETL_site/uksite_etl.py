import requests
from bs4 import BeautifulSoup
url = 'https://www.gov.uk/search/news-and-communications'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)
print(soup.title.string)
print(soup.find(id='global-cookie-message'))
soup.find_all("p", class_="title")
titres = soup.find_all('a', class_="gem-c-document-list__item-title")
for titre in titres:
    print(titre.string)
descr = "gem-c-document-list__item-description"
description = soup.find_all('p', class_=descr)  
titres_bs = soup.find_all("a", class_="gem-c-document-list__item-title")
titres = []
for titre in titres_bs:
    titres.append(titre.string)
print(titre)

