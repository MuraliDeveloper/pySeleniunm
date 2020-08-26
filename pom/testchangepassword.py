import time
import commons

from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains

from pom.changepasswordpage import changepasswordpage
from pom.loginpage import loginpage




class MyTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.loginpageobj = loginpage(self.driver)
        self.changepasswordpageobj=changepasswordpage(self.driver)
        time.sleep(5)

    def testchangepassword(self):
        self.loginpageobj.login("admin", "admin")
        time.sleep(5)
        self.changepasswordpageobj.changepassword("mahetha","admin","admin")