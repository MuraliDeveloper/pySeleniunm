import time
import commons

from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains


from pom.loginpage import loginpage


class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.loginpageobj=loginpage(self.driver)

        time.sleep(5)


    def testlogintoappbyvaliduser(self):
        self.loginpageobj.login("admin","mahetha")

       
        time.sleep(5)
    def testloginwithemptyuername(self): #negative test case
        self.loginpageobj.login("", "mahetha")
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def testloginwithemptypassword(self):
        self.loginpageobj.login("admin", "")
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)
    def testloginwithusernameandemptypassword(self):
        self.loginpageobj.login("","")
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)
    def testvalidusernameandwrongpassword(self):
        self.loginpageobj.login("admin", "admin")
        time.sleep(5)
    def testvalidpasswordandwrongusername(self):
        self.loginpageobj.login("naresh", "mahetha")
        time.sleep(5)

    def testinvaliduser(self):
        self.loginpageobj.login("naresh", "mahetha")

        time.sleep(5)



