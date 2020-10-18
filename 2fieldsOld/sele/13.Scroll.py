#!/usr / bin / env python
from selenium import webdriver
import time

# set webdriver path here it may vary
driver = webdriver.Chrome(executable_path="C:\Murali\Training\chromedriver_win32\chromedriver.exe")
# brower = webdriver.Firefox(executable_path ="C:\Murali\chromedriver.exe")
# brower = webdriver.Ie(executable_path ="C:\Murali\chromedriver.exe")


website_URL = "https://www.twitter.com"
driver.get(website_URL)
time.sleep(5)

#scroll to pixcel
driver.execute_script("window.scrollTo(0, 200);")
time.sleep(5)

#scroll to end page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()




#Scrolling to target element ("BROWSE TEMPLATES" button at the bottom of page) using actions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
target = driver.find_element_by_link_text('BROWSE TEMPLATES')
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()



#Scrolling to target element ("BROWSE TEMPLATES" button at the bottom of page) with JavaScript
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
target = driver.find_element_by_link_text('BROWSE TEMPLATES')
driver.execute_script('arguments[0].scrollIntoView(true);', target)


#Scrolling to the bottom of page with Keys
"""
 send_keys(Keys.DOWN)/send_keys(Keys.UP) and send_keys(Keys.PAGE_DOWN)/send_keys(Keys.PAGE_UP) also could be used for scrolling
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
driver.find_element_by_tag_name('body').send_keys(Keys.END) # Use send_keys(Keys.HOME) to scroll up to the top of page



 #Scrolling to target element ("BROWSE TEMPLATES" button at the bottom of page) with built-in method
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
target = driver.find_element_by_link_text('BROWSE TEMPLATES')
target.location_once_scrolled_into_view