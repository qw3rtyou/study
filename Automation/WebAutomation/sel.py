#-*- coding: utf-8 -*-
# Selenium 임포트
from selenium import webdriver

# 크롬 드라이버 생성 - 경로 설정 필요 없음
driver = webdriver.Chrome()

# 사이트 접속하기
driver.get('https://www.naver.com')