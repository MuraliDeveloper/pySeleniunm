import unittest
import commons

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "login.html")
        time.sleep(5)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")


    def testsearchbyfirstname(self):
        self.login("admin", "mahetha")
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("advSearchEmpLbl").click()
        self.findbyname("fName").send_keys("deva")
        self.findbyxpath("//input[@type='submit']").click()
        time.sleep(5)

    def testsearchbylastname(self):
        self.login("admin", "mahetha")
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("advSearchEmpLbl").click()
        self.findbyname("lName").send_keys("reddy")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)

    def  testwithdeptname(self):
        self.login("admin", "mahetha")
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("advSearchEmpLbl").click()
        self.findbyname("deptId").send_keys("admin")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)

    def  testwithcity(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("advSearchEmpLbl").click()
        self.findbyname("city").send_keys("tirupathi")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)

    def testwith2fieldsdatawithdiffempdetails(self):#showing as No Results Found
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("advSearchEmpLbl").click()
        self.findbyname("lName").send_keys("reddy")
        self.findbyname("fName").send_keys("deva")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)

    def testwith3fieldsdatawithdiffempdetails(self):#showing as No Results Found
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("advSearchEmpLbl").click()
        self.findbyname("lName").send_keys("reddy")
        self.findbyname("fName").send_keys("deva")
        self.findbyname("city").send_keys("tirupathi")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)




