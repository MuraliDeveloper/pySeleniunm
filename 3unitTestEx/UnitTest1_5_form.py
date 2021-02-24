#unittest1

import unittest
from basics import commons
from selenium import webdriver
import time
from basics.basetest import BaseTest


class MyTest(BaseTest):     # Create a class which is a childclass of unittest.testcase

    def test1(self):

        # open google.com
        self.driver.get(commons.app_url + "form1.html")
        time.sleep(5)
        self.assertEqual("welcome to form1", self.driver.title,"invalid title for form.html")


    def test2(self):

        # open google.com
        self.driver.get(commons.app_url + "form.html")
        time.sleep(5)
        self.assertEqual("my form page", self.driver.title,"invalid title for form.html")

        firstnameobj = self.driver.find_element_by_name("uName")
        firstnameobj.send_keys("kumar")

        lastnameobj =self. driver.find_element_by_name("LName")
        lastnameobj.send_keys("mahetha")

        passwordobj = self.driver.find_element_by_name("password")
        passwordobj.send_keys("jjjjjjnkh")

        time.sleep(5)


