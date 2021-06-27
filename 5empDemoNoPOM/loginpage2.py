
import unittest


from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

"""
   1.test with valid username and password
   2.test with  valid username and invalid password
   3.test with invalid username and  password
   4.test with empty username
   5.test with empty password
   6.test with empty username and password
"""


from basics import commons
from basics.commons import getChromeDriver


class MyTest2(unittest.TestCase):  # Create a class which is a childclass of unittest.testcase
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
        self.login("admin","admin")
        time.sleep(3)
        self.assertEqual("Employee Profile",self.driver.title, "invalid title for home page")
        #self.checklinks()

    # 2.test with valid username and invalid password
    def testLogintoAppbyInvalidCreds(self):
            self.login("admin", "admin1")
            time.sleep(3)
            self.assertEqual("Welcome to Employee Application", self.driver.title, "invalid title for login.html")

            errorObj = self.driver.find_element_by_xpath("//font[@color='Red']")
            self.assertTrue(errorObj.is_enabled())
            self.assertTrue(errorObj.is_displayed())
            self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")

            time.sleep(5)

    # 3.test with invalid username and invalid password
    def testLogintoAppbyInvalidUnAndPass(self):
        self.login("admin1", "admin1")
        time.sleep(3)
        self.assertEqual("Welcome to Employee Application", self.driver.title, "invalid title for login.html")

        errorObj = self.driver.find_element_by_xpath("//font[@color='Red']")
        self.assertTrue(errorObj.is_enabled())
        self.assertTrue(errorObj.is_displayed())
        self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")

        time.sleep(5)


   # 4. test with enmpty username
    def testLoginWithEmptyUserName(self): #negative test case
        self.login("","admin")

        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    # 5. test with enmpty password
    def testLoginWithEmptyPassword(self):
        self.login("admin", "")

        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    # 6. test with enmpty username and password
    def testLoginWithEmptyUnameAndPassword(self):
        self.login("", "")

        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def login(self, userName, password):
            # enter login name
            elementobj = self.driver.find_element_by_name("loginName")
            self.assertTrue(elementobj.is_enabled())
            self.assertTrue(elementobj.is_displayed())
            elementobj.send_keys(userName)

            # enter password
            passwordObj = self.driver.find_element_by_name("password")
            self.assertTrue(passwordObj.is_enabled())
            self.assertTrue(passwordObj.is_displayed())
            passwordObj.send_keys(password)
            time.sleep(3)

            # click on login button
            loginObj = self.driver.find_element_by_xpath("//input[@value='Login']")
            self.assertTrue(loginObj.is_enabled())
            self.assertTrue(loginObj.is_displayed())
            loginObj.click()

            # below not tested

    def testLoginAdmin(self):
        self.findbyname("loginName").send_keys("admin")

        self.findbyname("password").send_keys("admin")
        self.findbyxpath("//input[@value='Login']").click()
        self.assertEqual("Employee Profile", self.driver.title, "invalid title for login.html")  # validate title
        time.sleep(5)
        self.driver.find_element_by_link_text("My Profile")
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.driver.find_element_by_link_text("Add New Employee")
        self.driver.find_element_by_link_text("Change Password")
        self.driver.find_element_by_link_text("Advance Search")
        self.driver.find_element_by_link_text("Show All Employees")
        self.driver.find_element_by_link_text("My Subordinates")
        DepartmentLblobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(DepartmentLblobj).perform()
        self.driver.find_element_by_link_text("Add New Department")
        self.driver.find_element_by_link_text("Search Department")
        self.driver.find_element_by_link_text("Show All Departments")
        self.driver.find_element_by_link_text("Logout")
        time.sleep(5)


















