from sys import pycache_prefix
import pyautogui as gui; #🥺
import time
import selenium;
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.common.by import By;



chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Chrome(options=chrome_options)

#Window configuration
driver.get("https://marcelstein.com/elochallenge/starttest.php?token=ce3e75ea4b1681dec7ed81ab2e836599")
driver.fullscreen_window()
time.sleep(2)


# Getting the Lote number
loadNumber = driver.find_element_by_id('lblnumLote').get_attribute('innerText')

# Putting the Pedido number into a list
ordersNumber = []
for x in range(2,102):
    ordersNumber.append(driver.find_element_by_css_selector('body > main > div:nth-child(3) > div > div > div:nth-child(%s) > div:nth-child(1)' % x).get_attribute('innerText'))


rows = []
for x in range(2,102):
   rows.append(driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]' % x))

#teste 
for x in range(2,10):
    element = Select(driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[6]/select' % x)).select_by_visible_text("Postado")
    gui.moveTo(element.location())




