#unittest5
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
        self.driver.get(commons.app_url + "alert.html")
        time.sleep(5)
        self.assertEqual("Home Page", self.driver.title, "invalid title for alert.html")
    def test1(self):
        buttonobj=self.findbyname("alert1")
        buttonobj.click()
        alertObj = self.driver.switch_to.alert    #to get the alert obj
        msg=alertObj.text  #to get the alert msg
        self.assertEqual("do you want to continue", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()

        time.sleep(5)
        self.assertEqual(self.driver.title,"Google")
    def test2(self):
        buttonobj = self.findbyname("alert1")
        buttonobj.click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("do you want to continue", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.dismiss()
        time.sleep(5)
        self.assertEqual(self.driver.title, "Gmail")
    def test3(self):
        buttonobj = self.findbyname("alert2")
        buttonobj.click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("enter page", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.send_keys("https://www:facebook.com")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)





