
"""
Write test cases for
1.open driver
2.Open gmail.com
3.close driver

4.Open driver
5.Open google.com
6.close driver

use setup() and teardown()
"""
import time
import unittest
from basics.commons import getChromeDriver


driver = None

class MyTest(unittest.TestCase):

    def setUp(self) :
        global  driver
        driver = getChromeDriver()

    def tearDown(self) :
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










