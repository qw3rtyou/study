#-*- coding: utf-8 -*-
# Selenium 임포트
from selenium import webdriver

# 크롬 드라이버 생성 - 경로 설정 필요 없음
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

driver.find_element_by_css_selector('.top-nav__login-link').click()
driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')
driver.find_element_by_css_selector('.login-container__login-button').click()

print(driver.find_element_by_css_selector('.top-nav__login-link').text)