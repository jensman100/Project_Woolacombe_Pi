'''
Scrapes current wave data
Gets current time
Saves to CSV

To be run every half an hour
'''

import requests
from bs4 import BeautifulSoup as bs
from csv import DictWriter
from datetime import datetime

# Website which data is scraped from
url = 'https://magicseaweed.com/Woolacombe-Surf-Report/1352/'

# Path where CSV is saved
path_ = r'C:\Users\joeh2\OneDrive - University of Southampton\Documents\Project Woolacombe\Code_fr_fr\Wave_swell.csv'

# Obtaining the the html
try:
    page = requests.get(url)

except:
    raise Exception('Try connecting to the internet')


# print(page) # will start with 2 if success, 4 or 5 is bad 

# Makes it readable for python
soup = bs(page.content, 'html.parser')

### CURRENT SWELL ###

wind = soup.find(class_ ="h5 nomargin-top").get_text()
information = soup.find(class_ ="svg-icon-container msw-js-tooltip")["title"]

direction, degree = information.split('-')
direction = direction[:-2]
degree = degree[1:]


print(direction, degree)