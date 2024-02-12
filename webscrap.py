
import requests
from bs4 import BeautifulSoup


url = 'https://www.infomoney.com.br/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

print(len(links))



# print(soup.find_all('href'))