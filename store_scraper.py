import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.figure_factory as ff
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

path = '/Users/jordan5560/Desktop/Projects/tj_locations/chromedriver'

driver = webdriver.Chrome(path)
driver.set_window_size(1120, 1000)
driver.get("https://locations.traderjoes.com/ca/")
cities = driver.find_elements_by_class_name('itemlist')
city_list = []
for city in cities:
        city_list.append(city.text)

num_stores_by_city = []

print(city_list)
print(len(city_list))

index = 0
while index < len(city_list):
        print(city_list[index])
        cities = driver.find_elements_by_class_name('itemlist')
        cities[index].click()
        num = len(driver.find_elements_by_class_name('address-left'))
        num_stores_by_city.append(num)
        if num != 0:
                driver.find_element_by_xpath(
                    '//*[@id="content"]/a[2]').click()
        else:
                print("number of stores in " +
                      city_list[index] + " not found")
        index += 1


driver.close()
df = pd.DataFrame()
df['city_name'] = city_list
df['store_num'] = num_stores_by_city
df.to_csv('scraped_store_data.csv')
