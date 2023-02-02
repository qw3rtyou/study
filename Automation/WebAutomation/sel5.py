import time
from selenium import webdriver
from openpyxl import Workbook

wb=Workbook(write_only=True)
ws=wb.create_sheet('플레이 리스트')
ws.append(['제목','해시태그','좋아요','곡 수'])

# 웹 드라이버 설정
driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

# 현재 scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    time.sleep(0.5)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

playlists=driver.find_elements_by_css_selector('div.playlist__meta')

for playlist in playlists:
    title=playlist.find_element_by_css_selector('h3.title').text
    hashtags=playlist.find_element_by_css_selector('p.tags').text
    like_count=playlist.find_element_by_css_selector('span.data__like-count').text
    music_count=playlist.find_element_by_css_selector('span.data__music-count').text

    ws.append([title,hashtags,like_count,music_count])

driver.quit()
wb.save('플레이리스트_정보.xlsx')

