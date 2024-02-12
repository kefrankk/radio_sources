import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# galaxies infos
columns = ['NSAID', 'RAdeg-gal', 'DEdeg-gal', 'RAdeg-spec', 'DEdeg-spec', 'Sep', 'z', 'mass', 'SFR', 'metallicity', 'Ref', 'Class']

rows = []
gal = []
with open('Molina2021_Dwarf_sample.txt', 'r') as prop:

    for line_number, line in enumerate(prop):
        if line_number > 43:
            row = line.split()
            rows.append(row)

    
    for i in range(len(rows)):
        gal.append(rows[i])


properties = pd.DataFrame(gal, columns=columns)

RA_gal, dec_gal = properties['RAdeg-gal'].values, properties['DEdeg-gal'].values

# tranforming to string to be able to use selenium for research
galaxy = []
for o in range(len(RA_gal)):
    galaxy.append([str(RA_gal[o]) + ' ' +str(dec_gal[o])])

# print(galaxy)


url = 'https://sundog.stsci.edu/cgi-bin/searchfirst'


for i in range(len(galaxy)):
    # using selenium to serach for our query
    driver = webdriver.Chrome()
    
    driver.get(url)

    driver.find_element(By.XPATH, '//input[@id="pos"]').clear()
    form_radec = driver.find_element(By.XPATH, '//input[@id="pos"]').send_keys(galaxy[i])

    buttom = driver.find_element(By.XPATH, '//input[@type="submit"]')
    buttom.click()


    elements = driver.find_element(By.TAG_NAME, 'pre')
    
    if 'Position is not in the area currently covered by the FIRST catalog' not in elements.text:
        print(galaxy[i])



    driver.quit()


# def search_galaxy(position):
#     driver = webdriver.Chrome()
    
#     try: 

#         url = 'https://sundog.stsci.edu/cgi-bin/searchfirst'
#         driver.get(url)

        


    # except:
    #     print('abri o site!')




exit()

# opening the website where we want to search for our query


response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


# # print(soup)
inputs = []
for link in soup.find_all('input'):
    inputs.append(link.get('value'))
print(inputs)







# print(soup.find_all('href'))