import time

from empdemo5.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from pom6.loginpage import loginpage

"""
   1.test with valid username and password
   2.test with  valid username and invalid password
   3.test with invalid username and  password
   4.test with empty username
   5.test with empty password
   6.test with empty username and password
"""

class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    #create the obj for loginpage class
    def setUp(self):
        BaseTest.setUp(self)
        self.loginpageobj=loginpage(self.driver)
        time.sleep(5)

    # 1.test with valid username and valid password
    def testLoginWithValiduser(self):
        self.loginpageobj.login("admin","admin")
        time.sleep(5)
        self.loginpageobj.validateTitle()

    # 2.test with valid username and invalid password
    def testLogintoAppbyInvalidCreds(self):
        self.loginpageobj.login("admin", "admin1")
        time.sleep(3)
        self.loginpageobj.validateInvalidLogin()

        time.sleep(2)

    # 3.test with invalid username and invalid password
    def testLogintoAppbyInvalidUnAndPass(self):
        self.loginpageobj.login("admin1", "admin1")
        time.sleep(3)
        self.loginpageobj.validateInvalidLogin()
        time.sleep()

    #4 test with empty username
    def testLoginWithEmptyUsername(self): #negative test case
        self.loginpageobj.login("", "xyz")
        self.loginpageobj.validateUserEmpty()
        time.sleep(2)

    # 5 test with empty pass
    def testLoginWithEmptyPassword(self):
        self.loginpageobj.login("admin", "")
        self.loginpageobj.validatePasswordEmpty()
        time.sleep(2)

    # 6  test with empty username and pass
    def testLoginWithEmptyUsernameAndEmptypassword(self):
        self.loginpageobj.login("", "")
        self.loginpageobj.validateUserEmpty()




