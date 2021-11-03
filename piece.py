from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

for k in range(1,101):
    try:
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[5]/input' % k)
    except NoSuchElementException:
        print("not found")
    else:
            if(driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[5]/input' % k).get_attribute('innerText')!= ""):
                print("not this")
            else:
                trackersNumber.append(driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div[%s]/div[5]/input' % k))


for x in range(0,100):
    try:
        trackersNumber[x].clear()
        driver.execute_script("arguments[0].setAttribute('value',arguments[1])",trackersNumber[x], x)
    except ElementNotInteractableException:
        print("not")
        time.sleep(0.5)