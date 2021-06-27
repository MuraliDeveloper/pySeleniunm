import time
import unittest

from seleniumEx.myBasetest import BaseTest, BASE_URL


class MyTest(BaseTest):

    def test1(self):
        self.driver.get(BASE_URL + "ex1.html")
        time.sleep(3)

    def test2(self):
        self.driver.get(BASE_URL + "ex2.html")
        time.sleep(3)

    def test3(self):
        self.driver.get(BASE_URL + "ex3.html")
        time.sleep(3)

    def test1(self):
      self.driver.get("http://www.google.com")
      pageTitle =self.driver.title

      self.assertEqual("Google" ,pageTitle , "Invalid Title")
      time.sleep(3)





