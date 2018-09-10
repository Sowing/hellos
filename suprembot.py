import platform
import sys
import requests
import json
import random
import datetime
import time
from lxml import etree
from concurrent import futures as cf
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome('./bin/chromedriver', chrome_options=options)
    driver.set_window_size(1000,1000)
    #driver.get('https://www.supremenewyork.com/shop/all/shirts')
    driver.get('http://www.supremenewyork.com/shop/tops-sweaters/twgfyonia/hoyxnd7z1')
    wait = WebDriverWait(driver, 100)
    time.sleep(2)
    #clickme = driver.find_element_by_xpath('//*[@id="container"]/article[5]/div/a')
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    time.sleep(2)
    name = 'Nany Zhang'
    email = 'zn900708@gmail.com'
    tel = '9087352108'
    address1 = '330 Madison Ave'
    address2 = '4th floor'
    zipcode = '10017'
    state = 'NJ'
    city = 'Jersey City'
    ccNum = '4859108075936737'
    expMon = '08'
    expYear = '2022'
    ccVV = '878'
    #driver.find_element_by_xpath('//*[@id="cart-address"]/fieldset/div[1]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(name)
    #driver.find_element_by_xpath('//*[@id="cart-address"]/fieldset/div[2]').click()
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(email)
    #driver.find_element_by_xpath('//*[@id="cart-address"]/fieldset/div[3]').click()
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(tel)
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(address1)
    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(address2)
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(zipcode)
    #driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(city)
    #driver.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys(state)
    driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(ccNum)
    driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(expMon)
    driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(expYear)
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(ccVV)
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()



