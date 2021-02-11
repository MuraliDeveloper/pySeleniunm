import time
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

    def testlogintoapp(self):
        self.login("admin", "mahetha")
        time.sleep(5)
        deptobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(deptobj).perform()
        self.findbyid("showDeptsLbl").click()
        time.sleep(5)



