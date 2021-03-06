import unittest


from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from basics import commons
from basics.basetest import BaseTest



class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        # complete login
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "login.html")
        time.sleep(5)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
        self.login("admin", "admin")
        self.checkHeaderlinks()
        self.findbyid("changePwd").click()
        time.sleep(5)

    def testwithcorrectdata(self):
        self.findbyname("currPass").send_keys("admin")
        self.findbyname("newPass").send_keys("admin123")
        self.findbyname("confirmPass").send_keys("admin123")
        self.findbyname("Change Password").click()
        time.sleep(5)


    def testwithdifferentnewandconfirmpasswords(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("admin")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

        self.findbyid("changePwd").click()
        time.sleep(5)
        self.findbyname("currPass").send_keys("admin")
        self.findbyname("newPass").send_keys("mahetha")
        self.findbyname("confirmPass").send_keys("mahitha")
        self.findbyname("Change Password").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("New Pass and  confirmPass should be same!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testwithinvalidoldpass(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

        self.findbyid("changePwd").click()
        time.sleep(5)
        self.findbyname("currPass").send_keys("admin")
        self.findbyname("newPass").send_keys("mahetha")
        self.findbyname("confirmPass").send_keys("mahetha")
        self.findbyname("Change Password").click()
        time.sleep(5)

    def testwithinvalidoldpassanddifferentnewandconfirmpasswords(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

        self.findbyid("changePwd").click()
        time.sleep(5)
        self.findbyname("currPass").send_keys("admin")
        self.findbyname("newPass").send_keys("mahetha")
        self.findbyname("confirmPass").send_keys("mahitha")
        self.findbyname("Change Password").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("New Pass and  confirmPass should be same!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)
    def testwithemptynewandconfirmpass(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

        self.findbyid("changePwd").click()
        time.sleep(5)
        self.findbyname("currPass").send_keys("mahetha")
        self.findbyname("newPass")
        self.findbyname("confirmPass")
        self.findbyname("Change Password").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide new Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testwithemptynewpass(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

        self.findbyid("changePwd").click()
        time.sleep(5)
        self.findbyname("currPass").send_keys("mahetha")
        self.findbyname("newPass")
        self.findbyname("confirmPass").send_keys("admin")
        self.findbyname("Change Password").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide new Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testwithemptycurrentpass(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

        self.findbyid("changePwd").click()
        time.sleep(5)
        self.findbyname("currPass")
        self.findbyname("newPass").send_keys("admin")
        self.findbyname("confirmPass").send_keys("admin")
        self.findbyname("Change Password").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide current Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testwithallempty(self):
        self.findbyname("loginName").send_keys("admin")
        self.findbyname("password").send_keys("mahetha")
        self.findbyxpath("//input[@value='Login']").click()
        time.sleep(5)

        self.findbyid("changePwd").click()
        time.sleep(5)
        self.findbyname("currPass")
        self.findbyname("newPass")
        self.findbyname("confirmPass")
        self.findbyname("Change Password").click()
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide current Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)




