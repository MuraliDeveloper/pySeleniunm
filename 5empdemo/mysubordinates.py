import unittest
import commons

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains


class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "login.html")
        time.sleep(5)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
    def testsubord(self):
       self.findbyxpath("//a[@href='mySubordinates']").click()