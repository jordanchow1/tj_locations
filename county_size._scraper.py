from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv

path = '/Users/jordan5560/Desktop/Projects/tj_locations/chromedriver'

driver = webdriver.Chrome(path)
url = 'https://en.wikipedia.org/wiki/List_of_counties_in_California'
driver.get(url)
county_list = {}
county_index = 0
processing_cities = True

# while processing_cities:
baseTable = driver.find_element_by_xpath(
    '//*[@id="mw-content-text"]/div/table[2]')
tableRows = baseTable.find_elements_by_tag_name("tr")
for i in range(1, len(tableRows)):
        alist = []
        county_text = tableRows[i].find_element_by_tag_name('th').text

        county_size = tableRows[i].find_elements_by_tag_name('td')
        for i in county_size:
                alist.append(i.text)
        county_list[county_text] = alist[7]

print(county_list)

driver.close()

file = open("county_size.csv", "w")

writer = csv.writer(file, )
for key, value in county_list.items():
        writer.writerow([key, value])

file.close()
