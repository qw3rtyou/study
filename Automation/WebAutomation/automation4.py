# Selenium 임포트
from selenium import webdriver

# 크롬 드라이버 생성
driver = webdriver.Chrome('chromedriver 경로를 넣어 주세요')

# 사이트 접속하기
driver.get('https://www.naver.com')

# 크롬 드라이버 종료
driver.quit() 