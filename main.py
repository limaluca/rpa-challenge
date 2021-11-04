import pyautogui as gui; #🥺
import time;
import selenium;
import pyperclip;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome('./chromedriver.exe')
driver = webdriver.Chrome()

#Window configuration
driver.get("https://marcelstein.com/elochallenge/")
window_before = driver.window_handles[0]
driver.find_element_by_id("token").send_keys("ce3e75ea4b1681dec7ed81ab2e836599")
driver.find_element_by_class_name("btn-primary").click()
time.sleep(3)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
gui.click(500,500)
time.sleep(3)



#External Apps Location on screen
    #This is a temporary solution. The tuples store a X and Y value for a point in the screen. 
        #The main issue is: The values must be changed manually in order to match a different computer/screen
        
textify = (34, 133)
stlog = (34,44)
lote_stlog = (817,482)
carregarButton_STLOG = (817,506)
remessa_STLOG = (815,593)
localizarButton_STLOG = (815,621)
rastreamento_stlog = (1059,500)
rastreamento_stlog_adjust =(1075,514)
rastreamento_stlog_second_adjust = (994,514)
situacao_stlog =  (1013,577)
rastreamentoPoint = (836,450)


# Stores the load number 
loadNumber = driver.find_element_by_id('lblnumLote').get_attribute('innerText')



# Stores each order into a list
ordersNumber = []
for x in range(2,102):
    ordersNumber.append(driver.find_element_by_css_selector('body > main > div:nth-child(3) > div > div > div:nth-child(%s) > div:nth-child(1)' % x).get_attribute('innerText'))

# Opens external applications 
gui.hotkey('win', 'd')
gui.doubleClick(textify)
time.sleep(1)
gui.doubleClick(stlog)
time.sleep(16)

#Handles the ST_LOG app once before looping
gui.write(loadNumber)
time.sleep(1)
gui.click(carregarButton_STLOG)
time.sleep(5)


#Stores each tracking input into a list
trackersNumber = []
for w in range(2,102):
        try:
                driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[5]/input' % w)
        except NoSuchElementException:
                print("This element is not a tracking input")
        else:
                if(driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[5]/input' % w).get_attribute('innerText')!= ""):
                        print("eh uma div")
                else:
                        trackersNumber.append(driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[5]/input' % w))

#Loops through each order 
for x in range(2,102):
        gui.click(remessa_STLOG)
        gui.keyDown('ctrl')
        gui.keyDown('a')
        gui.keyUp('ctrl')
        gui.keyUp('a')
        gui.press('delete')
        gui.write(ordersNumber[x-2])
        gui.click(localizarButton_STLOG)
        time.sleep(5)

        #Handles Situação
        
        gui.keyDown('shift')
        gui.click(situacao_stlog)
        gui.keyUp('shift')
        gui.hotkey('ctrl','c')
        situacao = pyperclip.paste()
        if(situacao == 'Em transferencia'):
                situacao ='Em transferência'
        if(situacao == 'Recebido pelo destinatario'):
                situacao = 'Recebido pelo destinatário'
        Select(driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[6]/select' % x)).select_by_visible_text(situacao)

        time.sleep(0.2)
 
        gui.keyDown('shift')
        gui.click(rastreamento_stlog)
        gui.keyUp('shift')
        time.sleep(0.25)
        gui.click(rastreamento_stlog_adjust)
        gui.keyDown('ctrl')
        gui.keyDown('shift')
        gui.click(rastreamento_stlog_adjust)
        gui.click(rastreamento_stlog_second_adjust,duration=0.2)
        gui.keyUp('ctrl')
        gui.keyUp('shift')
        time.sleep(0.2)
        gui.hotkey('ctrl','c')
        


        try:
                time.sleep(0.2)
                #driver.execute_script("arguments[0].setAttribute('value',arguments[1])",trackersNumber[x-2], pyperclip.paste())
                trackersNumber[x-2].send_keys(str(pyperclip.paste()))
        except ElementNotInteractableException:
                print("not iterable tracker")
        except IndexError:
                print('nao ta na lista de trackers')

#Final steps
time.sleep(2)
gui.keyDown('alt')
gui.press('tab')
gui.press('tab')
gui.keyUp('alt')
time.sleep(1)
gui.click(500,500)
time.sleep(3)

driver.find_element_by_class_name("btn-primary").click()


time.sleep(10)

