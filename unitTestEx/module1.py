



import unittest
import commons
from selenium import webdriver

class MyTest(unittest.TestCase):     # Create a class which is a childclass of unittest.testcase
    driver=None

    def setUp(self):
        print("setup function called")
        self.driver = webdriver.Chrome(executable_path=commons.driver_url)

    def tearDown(self):
        print("teardown function is called")
        self.driver.close()
