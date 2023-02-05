from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

response=requests.get("https://blog.naver.com/sunny_0313")
page=response.text

#print(page)


driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://blog.naver.com/hammer1346")

driver.switch_to.frame('mainFrame') 
element_clickable=driver.find_elements_by_css_selector('#post-area > div:nth-child(15) > div > table.post-body > tbody > tr > td.bcc > div > div > a > img')[0]

print('*********************')
print(element_clickable.text)
print('*********************')

element_clickable.click()

driver.close()