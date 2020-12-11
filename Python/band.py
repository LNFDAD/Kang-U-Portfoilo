from selenium import webdriver
from bs4 import BeautifulSoup

import time
path = 'C:\\Users\\ekang\\OneDrive\\Programyoo\\chromedriver_win32 (2)\\chromedriver'
driver = webdriver.Chrome(path)
 
driver.get("http://www.ssg.com/")  

driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id('mem_id').send_keys('unirang72')
driver.find_element_by_id('mem_pw').send_keys('721117s')
driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/button').click()
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[-1])
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.execute_script("javascript:setCommonGnbCookie('useGnbAdvertCk','',-1);")


time.sleep(1000)

