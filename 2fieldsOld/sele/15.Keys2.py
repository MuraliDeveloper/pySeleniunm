#!/usr / bin / env python
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# set webdriver path here it may vary
driver = webdriver.Chrome(executable_path="C:\Murali\Training\chromedriver_win32\chromedriver.exe")

"""
oen google
enter "selenium"
press down
press down
press down
enter
"""

driver.get("https://www.google.com")
print(driver.title)
textobj = driver.find_element_by_name("q")
textobj.send_keys("selenium")
time.sleep(5)
textobj.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
textobj.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
textobj.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
textobj.send_keys(Keys.ENTER)

driver.close()


"""
perform shift key on google search
"""
# At time of writing this didn't work, but now seems to.
driver.get("https://www.google.com")
textobj = driver.find_element_by_name("q")
action = ActionChains(driver)
action.key_down(Keys.SHIFT)
action.send_keys_to_element(textobj,"selenium")
action.key_up(Keys.SHIFT)
action.send_keys_to_element(textobj,"web driver")
action.perform()
time.sleep(5)

# or
ActionChains(driver).send_keys(Keys.SHIFT, Keys.TAB, Keys.SHIFT).perform()


