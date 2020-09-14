import unittest
import commons
from selenium import webdriver
import time

class MyTest(unittest.TestCase):     # Create a class which is a childclass of unittest.testcase

    def test1(self):                    # each instance method is a testcase.
        # get driver
        driver = webdriver.Chrome(executable_path=commons.driver_url)

        # open google.com
        driver.get(commons.App_URL + "2.html")
        time.sleep(5)
        driver.close()

    def test2(self):
        # get driver
        driver = webdriver.Chrome(executable_path=commons.driver_url)

        # open google.com
        driver.get(commons.App_URL + "drag.html")
        time.sleep(5)
        driver.close()

