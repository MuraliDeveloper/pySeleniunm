import unittest
import commons

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from basics.basetest import BaseTest


class MyTest(BaseTest): # Create a class which is a childclass of unittest.testcase
    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "login.html")
        time.sleep(5)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")

    def test1(self):
        nameobj = self.findbyname("loginName")
        nameobj.send_keys("admin")
        passobj = self.findbyname("password")
        passobj.send_keys("admin")
        loginodj = self.findbyxpath("//input[@value='Login']")
        loginodj.click()
        time.sleep(5)
        linkobj = self.findbyid("updateProfile")
        linkobj.click()
        time.sleep(5)

        firstnameobj = self.findbyname("fName")
        firstnameobj.clear()
        firstnameobj.send_keys("Naresh")
        updateodj = self.findbyxpath("//input[@value='Update']")
        updateodj.click()
        time.sleep(5)


