from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/orangebottle/index')

info = list()

for branch in driver.find_elements_by_css_selector('.branch'):
    city=branch.find_element_by_css_selector('.city').text
    ave=branch.find_element_by_css_selector('.ave').text
    addr=branch.find_element_by_css_selector('.address').text

    info.append([city,ave,addr])

print(info)

driver.quit()