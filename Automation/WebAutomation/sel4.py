import time
from selenium import webdriver

# 웹 드라이버 설정
driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

print(driver.execute_script('return document.body.scrollHeight'))

# 현재 scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    time.sleep(3)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print(driver.execute_script('return document.body.scrollHeight'))

driver.quit()