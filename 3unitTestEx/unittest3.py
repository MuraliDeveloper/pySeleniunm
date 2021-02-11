#unittest3
import unittest
import commons
from selenium import webdriver
import time

from basics.basetest import BaseTest


class MyTest(BaseTest):     # Create a class which is a childclass of unittest.testcase



    def test1(self):  # each instance method is a testcase.

        # open google.com
        self.driver.get(commons.app_url + "drag.html")

        time.sleep(5)
        self.assertEqual("welcome to drag1", self.driver.title)

