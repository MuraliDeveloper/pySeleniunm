import time
from unittest_data_provider import data_provider
from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains

from pom.loginpage import loginpage


class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.loginpageobj = loginpage(self.driver)

        time.sleep(5)

    data = lambda: (
        ("admin", "admin"),
        ("admin", "mahetha"),
        ("naresh", "mahetha"),
        ("admin", ""),
        ("", "")
    )

    @data_provider(data)
    def testEx2(self, username, password):
        self.loginpageobj.login(username, password)
        time.sleep(5)
