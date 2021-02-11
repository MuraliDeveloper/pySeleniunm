
"""
Write test cases for 
1.Open gmail.com
2.Open google.com

"""
import time
import unittest
from basics.commons import getChromeDriver


#@unittest.SkipTest
class MyTest(unittest.TestCase):


    def test1(self):
        driver = getChromeDriver()

        # open google.com
        driver.get("https://www.gmail.com")

        time.sleep(5)
        # close driver
        driver.close()

    def test2(self):
        driver = getChromeDriver()

        # open google.com
        driver.get("https://www.google.com")

        time.sleep(5)
        # close driver
        driver.close()









