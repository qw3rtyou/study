브라우저를 제어하는 도구
클릭, 스크롤, 키보드 입력 등등의 기능을 코드로 구현 할 수 있음

# 환경 설정

pip로 라이브러리 설치하고            

	pip3 install selenium==3.141

웹드라이버를 설치하고

	https://chromedriver.chromium.org/downloads

웹드라이버를 c/windows로 옮기면 웹드라이버를 사용할 수 있음

# 웹사이트 가져오기

```python
#-*- coding: utf-8 -*-
# Selenium 임포트
from selenium import webdriver
# 크롬 드라이버 생성 - 경로 설정 필요 없음
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

driver.find_element_by_css_selector('.top-nav__login-link').click()
#driver.find_element_by_css_selector('#app > nav > div > a').click()
#이렇게 개발자도구의 copy selector를 사용해서 가져올 수도 있음

driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')
driver.find_element_by_css_selector('.login-container__login-button').click()

#웹요소 텍스트나 속성 가져오기
web_element=driver.find_element_by_css_selector('.top-nav__login-link')
print(web_element.text)
print(web_element.get_attribute('attr'))
```

# 다양한 find_element 메소드
. 이나 # 과 같은 문자 안 써줘도 됨

태그 이름으로 찾기
	driver.find_element_by_tag_name('tag_name')

id로 찾기
	driver.find_element_by_id('id-name')

class로 찾기
	driver.find_element_by_class_name('class-name')

복수 요소 찾기
```python
#element 뒤에 s 붙여주면 모든 요소를 리스트로 가져옴
# CSS 선택자
driver.find_elements_by_css_selector('selector')

# 태그 이름
driver.find_elements_by_tag_name('tag_name')

# class 이름
driver.find_elements_by_class_name('class-name')
```

# Selenium Wait
### implicitly_wait()
요소를 못찾으면 파라미터로 받은 값만큼 기다림
모든 코드에 적용
driver.implicitly_wait(3)

### time.sleep()
sleep()를 적은 곳만 파라미터로 받은 값만큼 기다림
```python
import time
time.sleep(1)
```

### Explicit Wait

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_link = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

id_box = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
#visibility_of_element_located()
#웹 요소가 실제로 보일 때까지 기다리라는 뜻
id_box.send_keys('codeit')

pw_box = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')

login_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()


#똑같은 기간을 사용한다면 한번만 만들어도 됨
wait = WebDriverWait(driver, 3)

login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

id_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')

pw_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()
```


### 유용한 wait 조건들
element_to_be_clickable() 웹 요소가 클릭 가능한 상태일 때까지 기다림.
visibility_of_element_located() 웹 요소가 실제로 보일 때까지 기다림.
text_to_be_present_in_element() 웹 요소 안에 텍스트가 로딩될 때까지 기다림.
invisibility_of_element_located() 웹 요소가 안 보일 때까지 기다림.


# 액션 체인
Selenium에서 액션 체인(Action Chain)은 사용자의
마우스, 키보드 동작(action)을 사슬(chain)처럼 이어서 실행하는 것을 뜻함
클릭, 키보드 입력 외의 동작은 액션 체인이 꼭 필요
많은 동작을 한 번에 묶어서 실행할 수 있음
사용자 동작 시나리오가 복잡해질 때 유용

### 액션 체인 사용
한 줄의 코드에서, 꼬리에 꼬리를 무는 방식으로 연결하는 방식
하나의 액션을 한 줄로 만들어서, 나열하는 방식

연결하는 방식
```python
# 아이디 박스, 비밀번호 박스, 로그인 버튼 찾아놓기
id_box = driver.find_element_by_css_selector('.login-container__login-input')
pw_box = driver.find_element_by_css_selector('.login-container__password-input')
login_button = driver.find_element_by_css_selector('.login-container__login-button')

# 액션 실행
(ActionChains(driver)
	.send_keys_to_element(id_box, 'codeit')
	.send_keys_to_element(pw_box, 'datascience')
	.click(login_button)
	.perform())
```

나열하는 방식
```python
# 아이디 박스, 비밀번호 박스, 로그인 버튼 찾아놓기
id_box = driver.find_element_by_css_selector('.login-container__login-input')
pw_box = driver.find_element_by_css_selector('.login-container__password-input')
login_button = driver.find_element_by_css_selector('.login-container__login-button')

# 액션 실행
actions = ActionChains(driver)
actions.send_keys_to_element(id_box, 'codeit')
actions.send_keys_to_element(pw_box, 'datascience')
actions.click(login_button)
actions.perform()
```

### 액션 체인 기능

함수에 parameter=None은 파라미터가 선택적이라는 뜻
나머지 파라미터는 필수

클릭
.click(element=None)
웹 요소 element를 파라미터로 전달해 주면 element를 클릭하고 그렇지 않으면 현재 마우스가 위치해 있는 곳을 클릭

더블 클릭
.double_click(element=None)
웹 요소 element를 파라미터로 전달해 주면 element를 더블 클릭하고 그렇지 않으면 현재 마우스가 위치해 있는 곳을 더블 클릭

우클릭
.context_click(element=None)
웹 요소 element를 파라미터로 전달해 주면 element를 우클릭하고 그렇지 않으면 현재 마우스가 위치해 있는 곳을 우클릭

드래그 앤 드롭
.drag_and_drop(source, target)
source 웹 요소를 클릭해서 target 웹 요소까지 드래그한 다음, 드롭

마우스 이동
.move_to_element(element)
element 웹 요소까지 마우스를 움직임

키보드 입력
.send_keys(keys)
.send_keys_to_element(element, keys)
send_keys()는 현재 선택된 웹 요소에 키보드 입력을 보내고, send_keys_to_element()는 element 요소에 키보드 입력을 보냄

동작 중지
.pause(seconds)
seconds초 동안 동작을 멈춤 
액션 체인에는 time.sleep() 대신 .pause()를 쓰면 됨


# Selenium과 BeautifulSoup
selenium을 이용해서 스크래핑도 가능하지만
bs를 사용하는 편이 더 빠르고 효율적이다.
따라서 웹페이지에서 원하는 동작을 selenium으로 모두 실행한 후
bs로 전체페이지를 분석하는 편이 좋다.

```python
### 스크롤 완료 ### 
music_page = driver.page_source
driver.quit()

soup = BeautifulSoup(music_page, 'html.parser')
```
# Selenium과 Javascript
selenium으로 javascript 코드를 실행 시킬 수 있다.
이 코드로 전체 페이지의 세로 길이를 참조해 스크롤을 제어할 수도 있다.

	driver.execute_script("window.scrollTo(0, 200);")


# 웹에서 이미지 가져오기
웹이서 이미지를 가져오면

	/images/costagram/posts/post0.jpg

보통 이런 식으로 주소라기보단 경로에 가까운 텍스트를 얻을 수 있다.
따라서 앞에다가 URL의 도메인 부분을 알아내서 붙여줘야한다.

	https://www.asdf.kr/경로

이미지를 다운로드 받으려면

```python
response = requests.get(image_url)
	with open('image.jpg', 'wb+') as f:
		f.write(response.content)
```
	


# 옵션 고르기

```python
from selenium.webdriver.support.ui import Select
cityCode_select = Select(driver.find_element_by_css_selector('#cityCode'))
# 옵션 이름으로 선택 (웹사이트에서 보이는 옵션 이름)
cityCode_select.select_by_visible_text('서울특별시')

# 옵션의 value로 선택 ('서울특별시' 옵션의 value는 1100)
cityCode_select.select_by_value('1100')

# 옵션의 인덱스로 선택 ('서울특별시'는 두 번째 옵션)
cityCode_select.select_by_index(1)
```

# 웹 브라우저 제어하기

### 네비게이션
#### 웹 페이지로 이동
driver.get('URL')
#### 뒤로가기(이전 페이지로 이동)
driver.back()
#### 앞으로가기(이후 페이지로 이동)
driver.forward()
#### 새로고침
driver.refresh()
#### 현재 URL 가져오기
driver.current_url

### 웹 브라우저 창 (window) 제어
*어떤 웹사이트들은 브라우저 창 크기에 따라 콘텐츠가 다르게 디스플레이되거나, 
창 크기가 너무 작으면 아예 로딩이 안될 수 있음

풀스크린
driver.fullscreen_window()

최대화
driver.maximize_window()

최소화
driver.minimize_window()

크기 조절
driver.set_window_size(800, 600) # 창 크기 (800, 600)으로 설정

스크린샷
driver.get_screenshot_as_file('image_name.png') # image_name.png라는 파일에 저장

### 웹 브라우저 창 여러 개 다루기
Selenium이 포커스된 탭을 바꾸려면 아래 코드를 실행
아래 코드를 실행하면 i 번째 탭으로 포커스가 바뀐다.

	driver.switch_to.window(driver.window_handles[i])

현재 포커스된 탭은 driver.current_window_handle로 확인

### iframe 다루기
iframe 태그는 html 태그 중 하나
html문서 안에 또다른 html문서를 삽입할 때 사용
그런데 iframe 태그 안에 html문서를 담고 있는게 아니라
그냥 참조하는 거임 따라서 iframe 안에 있는 태그, 요소를
찾으려고하면 실패함

iframe으로 이동하려면 창 여러개 다루는 것과 비슷하게 driver.switch_to사용
탭/창이 아닌 프레임으로 이동하는 것이니까 driver.switch_to.frame()

driver.switch_to.frame() 안에는
1. iframe 웹 요소
2. iframe의 id 속성값
3. iframe의 name 속성값(name 속성값은 중복될 수 있음)
4. iframe 인덱스
가 들어갈 수 있음

```python
# 웹 요소 파라미터로 사용
driver.switch_to.frame(driver.find_element_by_css_selector('#mainFrame')

# iframe의 id 또는 name 속성값 사용
driver.switch_to.frame('mainFrame')

# iframe 인덱스 사용
driver.switch_to.frame(0)

# 상위 iframe으로 이동
driver.switch_to.parent_frame()

# 웹 페이지 / 최상위 프레임 / 메인 프레임으로 이동 
driver.switch_to.default_content()
```

### headless 모드
웹브라우저가 눈에 보이지 않는 상태
백그라운드에서 실행되는 모드
더 빠르고 자원을 덜 소모함
오류파악이 힘듬   

```python
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome("chromedriver 경로", options=options)
```
