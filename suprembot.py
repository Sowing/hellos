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
import bs4 as BeautifulSoup

def buy_item(url,size):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome('./bin/chromedriver', chrome_options=options)
    driver.set_window_size(1000,1000)
    #driver.get('https://www.supremenewyork.com/shop/all/shirts')
    driver.get(url)
    #driver.find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()

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
    for i in tel:
        driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(i)
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(address1)
    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(address2)
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(zipcode)
    #driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(city)
    #driver.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys(state)
    for i in ccNum:
        driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(i)
    driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(expMon)
    driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(expYear)
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(ccVV)
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()
    time.sleep(10000)

def get_url(color, category):
    print("You want a %s in %s color" % (category, color))
    base_url = "http://www.supremenewyork.com/shop/all/"
    item_base_url = 'https://www.supremenewyork.com'
    headers = {
        "Host": "www.supremenewyork.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }

    s = requests.session()
    url = str(base_url)+str(category)
    req = s.get(url, headers=headers).text
    soup = BeautifulSoup.BeautifulSoup(req, "lxml")
    links = {}
    for box in soup.findAll('div',{"class":"inner-article"}):
        name = box.text.lower()
        #print(name)
        if "sold out" in name:
            continue #FUN
        elif color.lower() in name:
            links[box.h1.text] = box.a['href']


    if len(links) == 0:
        print("No such color in this category")
        return False
    elif len(links) == 1:
        print("Buying item : %s" % list(links.keys())[0])
        return str(item_base_url) + str(links[list(links.keys())[0]])
    else:
        print("Multiple items available, will buy the 1st one. Which you want to buy?")
        count = 0
        for key, value in links.items():
            print("[%s] Available item found : %s" % (count,key))
            count = count + 1
        item = input("Please enter the number : ")

        return str(item_base_url) + str(links[list(links.keys())[int(item)]])    
   
if __name__ == '__main__':
    colors = ["Black" , "Blue" , "Red" , "Off White" , "Navy" , "Multi" ,"Teal" , "Bright Yellow" , "Yellow Plaid" , "Olive Drab", "Dark Red" , "Magenta" , "White" , "Pink" , "Woodbine" , "Light Yellow" , "Light Burgundy" , "Denim" , "Green" , "Royal" , "Pale Peach" , "Heater Grey","Heather Mustard" , "Navy Digi Camo" , "Dark Purple" , "Orange" , "Rose" , "Ice Blue" , "Plum" , "Pale Lime" , "Bright Orange", "Hickory Stripe", "Washed Blue", "Peach", "Tan Digi Camo", "Pink Digi Camo", "pale violet", "indigo", "gold", "dark olive","navy digi camo","emerald green","silver","dusty teal","rigid indigo","yellow","brown","desrt camo","olive","charcoal","pine","burgundy","purple","maroon","snakeskin","rust","woodland camo","oxblood","ash grey","khaki","tan"]
    categories = ["accessories","jackets","shirts","tops_sweaters","sweatshirts","pants","hats","bags","shoes","skate"]
    sizes = ["XLarge", "Medium", "Large"]
    color = colors[0]
    category = categories[1]
    size = sizes[0]
    count = 0

    for category in categories:
        category = category.title()
        if count%2 != 0:
            spaces = ''
            print("[%s] %s %s" % (count, category, spaces))
        else:
            if count<10:
                spaces = (21-len(category))*' '
            else:
                spaces = (20-len(category))*' '
            print("[%s] %s %s" % (count, category, spaces), end='')
        count = count + 1
    print('\n')
    category = int(input("Please enter your category code : "))
    category = categories[category]
    print('\n')

    count = 0
    for color in colors:
        color = color.title()
        if count%2 != 0:
            spaces = ''
            print("[%s] %s %s" % (count, color, spaces))
        else:
            if count<10:
                spaces = (21-len(color))*' '
            else:
                spaces = (20-len(color))*' '
            print("[%s] %s %s" % (count, color, spaces), end='')
        count = count + 1
    print('\n')
    color = int(input("Please enter your color code : "))
    color = colors[color]

    url = get_url(color, category)
    if url:
        buy_item(url,size)
    else:
        print("Please try a different combination.")
