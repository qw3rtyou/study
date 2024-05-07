from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

# round1

response = requests.get("https://m.blog.naver.com/assamlike/220363106541")
page = response.text

# print(page)

soup = BeautifulSoup(page, "html.parser")

target_span_tags = soup.select("#viewTypeSelector > div > p > span")

for target_span_tag in target_span_tags:
    print(target_span_tag.get_text())

target_p_tags = soup.select("#viewTypeSelector > div > p ")

for target_p_tag in target_p_tags:
    print(target_p_tag.get_text())

# round2

response = requests.get("https://blog.naver.com/keit_newtech/221243192335")
page = response.text

print(page)

soup = BeautifulSoup(page, "html.parser")

target_span_tags = soup.select(
    "#SEDOC-1522654302743--1003946270 > div.se_component_wrap.sect_dsc.__se_component_area > div:nth-child(3) > div > div > div > div > div > p"
)

for target_span_tag in target_span_tags:
    print(target_span_tag.get_attribute_list)
