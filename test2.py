import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://mail.163.com/')
time.sleep(3)
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name('email').send_keys('liangqicong2010')
driver.find_element_by_name('password').send_keys('Abc537612')
driver.find_element_by_id('dologin').click()
