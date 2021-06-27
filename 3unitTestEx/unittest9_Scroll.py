#!/usr / bin / env python

from seleniumEx.myBasetest import BaseTest
import time
from selenium.webdriver import ActionChains


class ScrollTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("https://www.youtube.com")
        self.driver.maximize_window()
        time.sleep(2)

    def test1(self):
        # scroll to pixcel
        self.driver.execute_script("window.scrollTo(0, 1200);")
        time.sleep(3)

     #Need Fix
    def test2(self):
        # scroll to end page (works on I.E.)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)


    def test3(self):
        element = self.driver.find_element_by_tag_name("html")
        element.send_keys(Keys.END)
        time.sleep(3)
        element.send_keys(Keys.END)
        time.sleep(3)



"""
scroll to the element
"""
driver = webdriver.Chrome()
driver.get('')
target = driver.find_element_by_name('data')
driver.execute_script('arguments[0].scrollIntoView(true);', target)
time.sleep(5)




#Scrolling to target element ("BROWSE TEMPLATES" button at the bottom of page) using actions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.youtube.com/')
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