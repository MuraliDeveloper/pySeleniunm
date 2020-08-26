#!/usr / bin / env python
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# set webdriver path here it may vary
browser = webdriver.Chrome(executable_path="C:\Murali\Training\chromedriver_win32\chromedriver.exe")



browser.get("https://en.wikipedia.org")
print(browser.title)
textobj = browser.find_element_by_id("q")
textobj.send_keys("selenium")
textobj.send_keys(Keys.ARROW_DOWN)
textobj.send_keys(Keys.ARROW_DOWN)
textobj.send_keys(Keys.ARROW_DOWN)
textobj.send_keys(Keys.ENTER)

browser.close()



# At time of writing this didn't work, but now seems to.
action = ActionChains(browser)
action.key_down(Keys.SHIFT)
action.send_keys_to_element(textobj,"selenium")
action.key_up(Keys.SHIFT)
action.send_keys_to_element(textobj,"web driver")
action.perform()
time.sleep(5)

# or
ActionChains(browser).send_keys(Keys.SHIFT, Keys.TAB, Keys.SHIFT).perform()


