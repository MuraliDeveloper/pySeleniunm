from pom6 import commons

driver_url="C:\\Murali\\Training\\Selenium\\chromedriver_win32\\chromedriver.exe"

def getChromeDriver():
    return  webdriver.Chrome(executable_path=driver_url)

import unittest

import time


from empdemo5.basetest import BaseTest
from selenium import webdriver


from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from unittest_dataprovider import data_provider



class GoogleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = commons.getChromeDriver()
        self.driver.get("https://www.google.com")
        time.sleep(2)



    """
        1.Open google.com
        2.type selenium
        3.Press Enter key
    """
    data = lambda: (
        (  "selenium",),
        ( "java",),
        (  "pycharm download",),
        (  "manual testing",),

    )

    @data_provider(data)
    def testProvider(self, search):
        textobj = self.driver.find_element_by_name("q")
        textobj.clear()
        textobj.send_keys(search)
        time.sleep(5)
        textobj.send_keys(Keys.ENTER)
        time.sleep(5)