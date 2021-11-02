from sys import pycache_prefix
import pyautogui;
import time
import selenium;
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.common.by import By;

# chrome_options = webdriver.ChromeOptions(); 
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);


driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Chrome()

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

for order in ordersNumber:
    print(order)




#Pegando o nome da tag para um controle posterior
    # print(driver.find_element_by_css_selector('body > main > div:nth-child(3) > div > div > div:nth-child(54) > div:nth-child(5) > input').tag_name)
    # print(driver.find_element_by_css_selector('body > main > div:nth-child(3) > div > div > div:nth-child(4) > div:nth-child(4)').tag_name)

# tab to the application oppened 
    # pyautogui.keyDown('command')
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('tab')
    # pyautogui.keyUp('command')





    # Order
#body > main > div:nth-child(3) > div > div > div:nth-child(2) > div:nth-child(1)
#body > main > div:nth-child(3) > div > div > div:nth-child(101) > div:nth-child(1)

    # Tracking
#body > main > div:nth-child(3) > div > div > div:nth-child(2) > div:nth-child(5) > input
#body > main > div:nth-child(3) > div > div > div:nth-child(3) > div:nth-child(5) > input
#body > main > div:nth-child(3) > div > div > div:nth-child(54) > div:nth-child(5) > input

        #Tracking preenchido
    #body > main > div:nth-child(3) > div > div > div:nth-child(4) > div:nth-child(4) Rastreamento
    #body > main > div:nth-child(3) > div > div > div:nth-child(4) > div:nth-child(1) Numero do pedido       
    
    
    # Status
#body > main > div:nth-child(3) > div > div > div:nth-child(2) > div:nth-child(6) > select
#body > main > div:nth-child(3) > div > div > div:nth-child(101) > div:nth-child(6) > select



# pyautogui.hotkey("command", "tab")
# pyautogui.moveTo(appLotePosition, duration=1)
# pyautogui.click()
# pyautogui.keyDown('command')
# pyautogui.keyDown('v')
# pyautogui.keyUp('command')
# pyautogui.keyUp('v')



# # pyautogui.moveTo(pedidoPosition, duration=1)
# # pyautogui.moveTo(rastreamentoPosition, duration=1)command
# # pyautogui.moveTo(situacaoPosition, duration=1)



# #From now on, the X should be the same and the Y will be increased
pedidoPosition = (235,448)
# rastreamentoPosition = (927,448)
# situacaoPosition = (1141,448)
# #Pretenting
# appLotePosition = (1101,525)
# appButtonLote = (10101, 572)
# dir = '/System/Applications/Stickies'






pyautogui.doubleClick(pedidoPosition)
pyautogui.keyDown('command')
pyautogui.press('c')
pyautogui.keyUp('command')