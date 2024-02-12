import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


columns = ['NSAID', 'RAdeg-gal', 'DEdeg-gal', 'RAdeg-spec', 'DEdeg-spec', 'Sep', 'z', 'mass', 'SFR', 'metallicity', 'Ref', 'Class']

rows = []
galaxy = []
with open('galaxy_properties.txt', 'r') as prop:

    for line_number, line in enumerate(prop):
        if line_number > 43:
            row = line.split()
            rows.append(row)

    
    for i in range(len(rows)):
        galaxy.append(rows[i])


properties = pd.DataFrame(galaxy, columns=columns)

RA_gal, dec_gal = properties['RAdeg-gal'].values, properties['DEdeg-gal'].values



# opening the website where we want to search for our query

url = 'https://sundog.stsci.edu/cgi-bin/searchfirst'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


# # print(soup)
inputs = []
for link in soup.find_all('input'):
    inputs.append(link.get('value'))
print(inputs)





# print(soup.find_all('href'))