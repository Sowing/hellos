from selenium import webdriver
import time
import sys
''' 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://python.org')
'''
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome('./bin/chromedriver', chrome_options=options)
driver.set_window_size(100,100)
driver.get('http://www.supremenewyork.com/shop/all')

wait = WebDriverWait(driver, 10)