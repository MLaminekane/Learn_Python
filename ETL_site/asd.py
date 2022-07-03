import requests
from bs4 import BeautifulSoup
url = 'https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296776-extrayez-et-transformez-des-donnees-avec-l-extraction-web'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)