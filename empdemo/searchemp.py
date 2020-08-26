import unittest
import commons

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from basics.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "login.html")
        time.sleep(5)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")


    def testsearchbyname(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("searchEmpLbl").click()
        self.findbyname("reqData").send_keys("deva")
        self.findbyxpath("//input[@type='radio' and @value='1']").click()
        self.findbyxpath("//input[@type='submit']").click()
        time.sleep(5)

    def testsearchbyid(self):#it is not selecting search by id

        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("searchEmpLbl").click()
        self.findbyxpath("//input[@type='radio' and @value='2']").click()
        self.findbyname("reqData").send_keys("112")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)

    def  testwithemptysearchbox(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("searchEmpLbl").click()
        self.findbyxpath("//input[@type='radio' and @value='2']").click()
        self.findbyname("reqData")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)
