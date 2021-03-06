import time

from empdemo5.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from pom6.loginpage import loginpage

class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        #create the obj for loginpage
        self.loginpageobj=loginpage(self.driver)
        time.sleep(5)


    # 1.test with valid username and password
    def testLogintoAppbyvalidCreds(self):
        # enter login name
        self.loginpageobj.login("admin", "admin")
        time.sleep(3)
        self.loginpageobj.validateTitle()
        # self.checklinks()

    # 2.test with valid username and invalid password
    def testLogintoAppbyInvalidCreds(self):
        self.loginpageobj.login("admin", "admin1")
        time.sleep(3)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
        self.loginpageobj.validateInvalidError()
        time.sleep(5)

    # 3.test with invalid username and invalid password
    def testLogintoAppbyInvalidUnAndPass(self):
        self.loginpageobj.login("admin1", "admin1")
        time.sleep(3)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
        self.loginpageobj.validateInvalidError()
        time.sleep(5)

    # 4. test with empty username
    def testLoginWithEmptyUserName(self):  # negative test case
        self.loginpageobj.login("", "admin")
        self.loginpageobj.validateUserEmpty()


    # 5. test with enmpty password
    def testLoginWithEmptyPassword(self):
        self.loginpageobj.login("admin", "")
        self.loginpageobj.validatePasswordEmpty()

     # 6. test with enmpty username and password
    def testLoginWithEmptyUnameAndPassword(self):
        self.loginpageobj.login("", "")
        self.loginpageobj.validateUserEmpty()

