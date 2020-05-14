import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv

path = '/Users/jordan5560/Desktop/Projects/tj_locations/chromedriver'

driver = webdriver.Chrome(path)
url = 'https://locations.traderjoes.com/ca/'
driver.get(url)
city_list = {}
city_index = 0
processing_cities = True

while processing_cities:

        cities = driver.find_elements_by_css_selector('.itemlist a')

        if city_index < len(cities):
                city_text = cities[city_index].text
                cities[city_index].click()
                store_locations = driver.find_elements_by_css_selector(
                    '.itemlist')
                city_list[city_text] = len(store_locations)
                driver.get(url)
                city_index += 1
        else:
                processing_cities = False

file = open("store_df.csv", "w")

writer = csv.writer(file, )
for key, value in city_list.items():
        writer.writerow([key, value])

file.close()
