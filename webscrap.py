
import re
import time
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# Run selenium without showing the browser
chrome_options = Options()
chrome_options.add_argument("--headless=new")



# columns of the table
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


with open('radio_sources.txt', 'w') as r:

    for i in tqdm(range(len(galaxy)), desc= "Searching for radio sources"):

        # opening SDSS Sky Server to obtain sexagesimal coordinates
        driver0 = webdriver.Chrome(options=chrome_options)

        url0 = 'https://skyserver.sdss.org/dr18/VisualTools/explore/summary'
        driver0.get(url0)

        # expands the search by
        expand = driver0.find_element(By.ID, 'searchcard')
        expand.click()

        time.sleep(0.5)
        searchRA_ = driver0.find_element(By.XPATH, '//input[@id = "searchRa"]').clear()
        searchRA = driver0.find_element(By.XPATH, '//input[@id = "searchRa"]').send_keys(RA_gal[i])

        searchDec_ = driver0.find_element(By.XPATH, '//input[@id = "searchDec"]').clear()
        searchDEC = driver0.find_element(By.XPATH, '//input[@id = "searchDec"]').send_keys(dec_gal[i])

        searchGO = driver0.find_element(By.XPATH, '//input[@value = "Go"]')
        searchGO.click()

        metadata = driver0.find_element(By.ID, 'MetadataCardHeader')
        metadata.click()

        sexag_ = driver0.find_elements(By.XPATH, '//table')


        bp = BeautifulSoup(sexag_[1].get_attribute('innerHTML'), 'html.parser')

        sexagesimal = bp.find('th', string = 'Sexagesimal').find_next('td').text
 

        # FIRST Catalog website
        driver = webdriver.Chrome(options=chrome_options)

        url = 'https://sundog.stsci.edu/cgi-bin/searchfirst'
        driver.get(url)

        driver.find_element(By.XPATH, '//input[@id="pos"]').clear()
        form_radec = driver.find_element(By.XPATH, '//input[@id="pos"]').send_keys(sexagesimal)

        buttom = driver.find_element(By.XPATH, '//input[@type="submit"]')
        buttom.click()

        # time.sleep(3)

        elements = driver.find_element(By.TAG_NAME, 'pre')


        if 'Flux' in elements.text:
            r.write('{} {}\n'.format(RA_gal[i], dec_gal[i]))


        
driver0.quit()        
driver.quit()



