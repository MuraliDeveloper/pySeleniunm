
"""
Write test cases for 
1.open driver
2.Open http://127.0.0.1:8000/htmls/ex1/
3.Open http://127.0.0.1:8000/htmls/ex2/
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
        driver.get("http://127.0.0.1:8000/htmls/ex1/")
        time.sleep(5)


    def test2(self):
       # open google.com
        driver.get("http://127.0.0.1:8000/htmls/ex2/")
        time.sleep(5)










