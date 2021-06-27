
import unittest


from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from basics import commons
from basics.commons import getChromeDriver

"""
   1.test with valid username and password
   2.test with  valid username and invalid password
   3.test with invalid username and  password
   4.test with empty username
   5.test with empty password
   6.test with empty username and password
   """

class MyTest(unittest.TestCase):  # Create a class which is a childclass of unittest.testcase
    driver = None

    def setUp(self):
        print("setup function called")
        self.driver = getChromeDriver()
        self.driver.get("http://localhost:8082/EmpDemo/" )
        time.sleep(3)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")

    # 1.test with valid username and password
    def testLogintoAppbyvalidCreds(self):
        #enter login name
        elementobj = self.driver.find_element_by_name("loginName")
        self.assertTrue(elementobj.is_enabled())
        self.assertTrue(elementobj.is_displayed())
        elementobj.send_keys("admin")

        # enter password
        passwordObj = self.driver.find_element_by_name("password")
        self.assertTrue(passwordObj.is_enabled())
        self.assertTrue(passwordObj.is_displayed())
        passwordObj.send_keys("admin")
        time.sleep(3)

        # click on login button
        loginObj = self.driver.find_element_by_xpath("//input[@value='Login']")
        self.assertTrue(loginObj.is_enabled())
        self.assertTrue(loginObj.is_displayed())
        loginObj.click()
        time.sleep(3)
        self.assertEqual("Employee Profile",self.driver.title, "invalid title for home page")
        #self.checklinks()

    # 2.test with valid username and invalid password
    def testLogintoAppbyInvalidCreds(self):
            # enter login name
            elementobj = self.driver.find_element_by_name("loginName")
            self.assertTrue(elementobj.is_enabled())
            self.assertTrue(elementobj.is_displayed())
            elementobj.send_keys("admin")

            # enter password
            passwordObj = self.driver.find_element_by_name("password")
            self.assertTrue(passwordObj.is_enabled())
            self.assertTrue(passwordObj.is_displayed())
            passwordObj.send_keys("admin1")
            time.sleep(3)

            # click on login button
            loginObj = self.driver.find_element_by_xpath("//input[@value='Login']")
            self.assertTrue(loginObj.is_enabled())
            self.assertTrue(loginObj.is_displayed())
            loginObj.click()
            time.sleep(3)
            self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")

            errorObj = self.driver.find_element_by_xpath("//font[@color='Red']")
            self.assertTrue(errorObj.is_enabled())
            self.assertTrue(errorObj.is_displayed())
            self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")

            time.sleep(3)

    # 3.test with invalid username and invalid password
    def testLogintoAppbyInvalidUnAndPass(self):
        # enter login name
        elementobj = self.driver.find_element_by_name("loginName")
        self.assertTrue(elementobj.is_enabled())
        self.assertTrue(elementobj.is_displayed())
        elementobj.send_keys("admin2")

        # enter password
        passwordObj = self.driver.find_element_by_name("password")
        self.assertTrue(passwordObj.is_enabled())
        self.assertTrue(passwordObj.is_displayed())
        passwordObj.send_keys("admin1")
        time.sleep(3)

        # click on login button
        loginObj = self.driver.find_element_by_xpath("//input[@value='Login']")
        self.assertTrue(loginObj.is_enabled())
        self.assertTrue(loginObj.is_displayed())
        loginObj.click()
        time.sleep(3)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")

        errorObj = self.driver.find_element_by_xpath("//font[@color='Red']")
        self.assertTrue(errorObj.is_enabled())
        self.assertTrue(errorObj.is_displayed())
        self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")

        time.sleep(5)

    def testLoginWithEmptyUserName(self): #negative test case
        # enter login name
        elementobj = self.driver.find_element_by_name("loginName")
        self.assertTrue(elementobj.is_enabled())
        self.assertTrue(elementobj.is_displayed())
        elementobj.send_keys("")

        # enter password
        passwordObj = self.driver.find_element_by_name("password")
        self.assertTrue(passwordObj.is_enabled())
        self.assertTrue(passwordObj.is_displayed())
        passwordObj.send_keys("admin1")
        time.sleep(3)

        # click on login button
        loginObj = self.driver.find_element_by_xpath("//input[@value='Login']")
        self.assertTrue(loginObj.is_enabled())
        self.assertTrue(loginObj.is_displayed())
        loginObj.click()
        time.sleep(3)

        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testLoginWithEmptyPassword(self):
        # enter login name
        elementobj = self.driver.find_element_by_name("loginName")
        self.assertTrue(elementobj.is_enabled())
        self.assertTrue(elementobj.is_displayed())
        elementobj.send_keys("admin2")

        # enter password
        passwordObj = self.driver.find_element_by_name("password")
        self.assertTrue(passwordObj.is_enabled())
        self.assertTrue(passwordObj.is_displayed())
        passwordObj.send_keys("")
        time.sleep(3)

        # click on login button
        loginObj = self.driver.find_element_by_xpath("//input[@value='Login']")
        self.assertTrue(loginObj.is_enabled())
        self.assertTrue(loginObj.is_displayed())
        loginObj.click()
        time.sleep(3)
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testLoginWithEmptyUnameAndPassword(self):
        # enter login name
        elementobj = self.driver.find_element_by_name("loginName")
        self.assertTrue(elementobj.is_enabled())
        self.assertTrue(elementobj.is_displayed())
        elementobj.send_keys("")

        # enter password
        passwordObj = self.driver.find_element_by_name("password")
        self.assertTrue(passwordObj.is_enabled())
        self.assertTrue(passwordObj.is_displayed())
        passwordObj.send_keys("")
        time.sleep(3)

        # click on login button
        loginObj = self.driver.find_element_by_xpath("//input[@value='Login']")
        self.assertTrue(loginObj.is_enabled())
        self.assertTrue(loginObj.is_displayed())
        loginObj.click()
        time.sleep(3)
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)


















