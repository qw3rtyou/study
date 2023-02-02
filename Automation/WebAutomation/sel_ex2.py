import time
from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)

driver=webdriver.Chrome()

driver.implicitly_wait(3)
driver.get('https://workey.codeit.kr/costagram/index')

driver.find_element_by_css_selector('.top-nav__login-link').click()

driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')
driver.find_element_by_css_selector('.login-container__login-button').click()

time.sleep(1)

last_height=driver.execute_script('return document.body.scrollHeight;')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.5)
    
    new_height=driver.execute_script('return document.body.scrollHeight;')

    if new_height==last_height:
        break

    last_height=new_height

posts=driver.find_elements_by_css_selector('.post-list__post')

for post in posts:
    post.click()
    time.sleep(0.5)

    picture=driver.find_element_by_css_selector('.post-container__image')
    print(picture.get_attribute('style').split("\"")[1])
    
    driver.find_element_by_css_selector('.close-btn').click()
    time.sleep(0.5)

driver.quit()