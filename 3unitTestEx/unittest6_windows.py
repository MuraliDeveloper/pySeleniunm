#unittest6
import unittest
import commons
import csv
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from basics.basetest import BaseTest


"""
How to get all windows?
solution)
windows =  driver.window_handles


How to get each window?
solution)
win1 = windows[0]  #fetches obj for 1st window
win2 = windows[1]  #fetches obj for 2nd window

How to switch between the window?
solution)
driver.switch_to.window(win1)  #switches to the 1st window
driver.switch_to.window(win2)  #switches to the 2nd window


How to click on link?
1.get the webelement obj
2.call click() method

<a id="gLink1" href="/htmls/form/" onclick="window.open('/htmls/form/',
                         'newwindow',
                         'width=700,height=750');return false;">
                         Open Window</a>

How to get the link object?

1.exact match of link text
linkObj = driver.find_element_by_link_text("Open Window")
linkObj.click()


2.partial match of link text
linkObj = driver.find_element_by_partial_link_text("Window")
linkObj.click()


"""
class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "window1.html")
        time.sleep(5)
        self.assertEqual("test3", self.driver.title, "invalid title for form.html")

    def test1(self):
       
        textobj=self.findbyid("gLink1")
        textobj.click() 
        time.sleep(5)
        windows = self.driver.window_handles
        print(windows)
        win1 = self.driver.window_handles[0]
        win2 = self.driver.window_handles[1]

        self.driver.switch_to.window(win2)
        self.assertEqual(self.driver.title, "Hello Python")

        fisrtobj=self.findbyname("name")
        fisrtobj.send_keys("murali")
        secondobj=self.findbyname("password")
        secondobj.send_keys("swamy")
        time.sleep(5)


        self.driver.switch_to.window(win1)
        textfieldobj=self.findbyname("uName")
        textfieldobj.send_keys("ram")
        time.sleep(5)
        self.assertEqual(self.driver.title,"test3")


