
"""
Write test cases for 
1.open driver
2.Open gmail.com
3.Open google.com
4.close driver

"""
import time
import unittest
from basics.commons import getChromeDriver


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
        driver.get("https://www.gmail.com")
        time.sleep(5)


    def test2(self):
       # open google.com
        driver.get("https://www.google.com")
        time.sleep(5)










