import time
import unittest

from basics.commons import getChromeDriver

class MyTest(unittest.TestCase):

    driver = None

    def setUp(self) :
        self.driver = getChromeDriver()

    def tearDown(self) :
        self.driver.close()

    def test1(self):
        self.driver.get("https://www.gmail.com")
        time.sleep(5)


    def test2(self):
        self.driver.get("https://www.google.com")
        time.sleep(5)




