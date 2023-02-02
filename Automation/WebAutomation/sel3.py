from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://workey.codeit.kr/costagram/index')

wait = WebDriverWait(driver, 3)

login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

id_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')

pw_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()

#driver.quit()