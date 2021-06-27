import time



from selenium.webdriver.common.action_chains import ActionChains

from pom6.basetest import BaseTest
from pom6.loginpage import loginpage


class MyTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.loginpageobj = loginpage(self.driver)
        self.changepasswordpageobj=changepasswordpage(self.driver)
        self.addnewemppageobj=addnewemppage(self.driver)
        time.sleep(5)

    def testaddnewemp(self):
        self.loginpageobj.login("admin", "admin")
        time.sleep(5)
        self.addnewemppageobj.addnewemp("kdevi","kdevi123","k","devi","12/12/1996","58462","1478523695")
