
"""
Write test cases for 
1.open driver
2.Open http://127.0.0.1:8000/htmls/form/
3.Open http://127.0.0.1:8000/htmls/ex2/
4.close driver

validate the title
"""


import time
import unittest

from selenium.webdriver.support.select import Select
from unittest_dataprovider import data_provider

from basics.commons import getChromeDriver, BASE_URL

driver = None

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global  driver
        driver = getChromeDriver()
        # open google.com
        driver.get(BASE_URL + "form/")

        # assert the title

    @classmethod
    def tearDownClass(cls):
        # close driver
        global driver
        driver.close()

    data = lambda: (
        ("user1",),
        ("user2",),
        ("user3",),
        ("user4",),
        ("user5",),
        ( "user65",),
        ("user7",),
        ("user8",),
        ("user9",)
    )

    #<input type="text" id="myname" name="uName">
    # here iput : tag
    # type , id, name are attribites.
    @data_provider(data)
    def testFirstNameRextField(self,name):
        elemntObj =  driver.find_element_by_name("uName")
        self.assertEqual("text",elemntObj.get_attribute("type"))

        elemntObj.clear()
        elemntObj.send_keys(name)
        time.sleep(3)

