import unittest
from basics import commons
from selenium import webdriver
import time

from basics.commons import getChromeDriver


class MyTest(unittest.TestCase):     # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        print("setup function called")
        self.driver = getChromeDriver()

    def tearDown(self):
        print("teardown function is called")
        self.driver.close()

    def test1(self):                    # each instance method is a testcase.

        self.driver.get(commons.App_URL + "2.html")
        time.sleep(5)


    def test2(self):

        self.driver.get(commons.App_URL + "3.html")
        time.sleep(5)

