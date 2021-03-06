import time
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


    def testwithvaliddeptname(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("searchDeptLbl").click()
        self.findbyname("name").send_keys("HR")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)

    def testwithnodeptname(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        deptobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(deptobj).perform()
        self.findbyid("searchDeptLbl").click()
        self.findbyname("name")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)
    def testwithinvaliddeptname(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)
        empobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("searchDeptLbl").click()
        self.findbyname("name").send_keys("MANAGER")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)