
"""
Write test cases for 
1.open driver
2.Open http://127.0.0.1:8000/htmls/ex1/
3.Open http://127.0.0.1:8000/htmls/ex2/
4.close driver

validate the title
"""


import time
import unittest
from basics.commons import getChromeDriver, BASE_URL

driver = None

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global  driver
        driver = getChromeDriver()

    @classmethod
    def tearDownClass(cls):
        # close driver
        global driver
        driver.close()

    def test1(self):
        # open google.com
        driver.get(BASE_URL+"ex1/")
        time.sleep(5)

    def test2(self):
       # open google.com
        driver.get(BASE_URL+"ex2/")
        time.sleep(5)

    def test3(self):
        # open google.com
        driver.get(BASE_URL + "alert/")
        time.sleep(5)










