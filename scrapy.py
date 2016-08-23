from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from pprint import pprint


url = "http://www.zillow.com/homes/for_sale/San-Diego-CA-92122/96664_rid/size_sort/32.94386,-117.066193,32.697177,-117.435265_rect/11_zm/1_p/1_fr/"

driver = webdriver.Chrome()
driver.get(url)

x = driver.find_element_by_class_name('photo-cards')
housing_cards = x.find_elements_by_tag_name('li')

print len(housing_cards)

# for housing_card in housing_cards:


driver.close()