import unittest
""""
There are two types of classes:
- page class  [for every web page]
- test classes [for every web page]



1.for every page there is a page class

2.the page class contains
   - instace variables 
      [web element objects]
   - methods
      [every operation on the page ]
      - verifictaion
      - any action 
      
page class should contain the logic for :
 -> identifying the webelements
 -> any action on web element
 
  so far the A & B is writeen in test class.
 if we write in test class it is diffcult for reusabilty.
 that why we are moving the logic to the page class.
  
  
  -> crate the obj for the class loginpage.
-> using the login page object call the functions for any actions or assertions.


"""
from pom6 import commons
from pom6.commonpage import commonpage
import time
class loginpage(commonpage,unittest.TestCase):


    def __init__(self,pdriver):
        commonpage.__init__(self,pdriver)
        self.driver=pdriver

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
        self.checkdisplayandenabled(self.usernameobj,self.passwordobj,self.buttonobj)
        self.buttonobj.click()

    def validateTitle(self):
        self.assertEquals("Employee Profile", self.driver.title, "invalid title for home page")

    def validateInvalidError(self):
        errorObj = self.driver.find_element_by_xpath("//font[@color='Red']")
        self.assertTrue(errorObj.is_enabled())
        self.assertTrue(errorObj.is_displayed())
        self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")

    def validateUserEmpty(self):
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        #self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)

    def validatePasswordEmpty(self):
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        #self.assertEqual("Please provide Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)



