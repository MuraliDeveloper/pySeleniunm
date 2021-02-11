#unittest6
import unittest
import commons
import csv
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from basics.basetest import BaseTest



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


