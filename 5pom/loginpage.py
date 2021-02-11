import unittest

from pom import commons
from pom.commonpage import commonpage


class loginpage(commonpage,unittest.TestCase):
    driver=None
    def __init__(self,pdriver):
        commonpage.__init__(self,pdriver)
        driver=pdriver
    def open(self):
        self.driver.get(commons.app_url)
        #self.assertEqual("Employee Profile",self.driver.title, "invalid title for login.html")
    def intializewebelement(self):
        self.usernameobj=self.findbyname("loginName")
        self.passwordobj=self.findbyname("password")
        self.buttonobj=self.findbyxpath("//input[@value='Login']")

    def login(self, username, password):
        self.open()
        self.intializewebelement()
        self.usernameobj.send_keys(username)
        self.passwordobj.send_keys(password)
        self.buttonobj.click()

