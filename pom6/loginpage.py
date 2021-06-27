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
      - verification
      - any action 
      
page class should contain the logic for :
 A> identifying the webElements
 B> any action on web element
 
 so far the A & B is written in test class.
 if we write in test class it is diffcult for reusabilty.
 that why we are moving the logic for A & B to the page class.
  
steps:

1.Create the page class with web-elementObjs and methods
2. create the obj for the  page class inside the test class.
3. using the page object call the functions for any actions or assertions.

"""
from pom6 import commons
from pom6.commonpage import commonpage
import time


#class loginpage(commonpage):
class loginpage(unittest.TestCase):
   
   #contsr is initrializing th driver
    def __init__(self,pdriver):
         self.driver=pdriver

    def open(self):
        self.driver.get("http://loclhost:8086/EmpDemo/")
        #self.assertEqual("Employee Profile",self.driver.title, "invalid title for login.html")

    def intializeWebElements(self):
        self.usernameobj=self.driver.find_element_by_name("loginName")
        self.passwordobj=self.driver.find_element_by_name("password")
        self.buttonobj=self.driver.find_element_by_xpath("//input[@value='Login']")


    def checkDisplayAndEnabled(self, *elements):
         for element in elements:
            self.assertTrue(element.is_enabled())
            self.assertTrue(element.is_displayed())

    def login(self, username, password):
        self.open()
        self.intializeWebElements()
        self.usernameobj.send_keys(username)
        self.passwordobj.send_keys(password)
        self.checkDisplayAndEnabled(self.usernameobj,self.passwordobj,self.buttonobj)
        self.buttonobj.click()

    def validateTitle(self):
        self.assertEquals("Employee Profile", self.driver.title, "invalid title for home page")

    def validateInvalidLogin(self):
        errorObj = self.driver.find_element_by_xpath("//font[@color='Red']")
        self.assertTrue(errorObj.is_enabled())
        self.assertTrue(errorObj.is_displayed())
        self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")
        self.assertEqual("Welcome to Employee Application", self.driver.title, "invalid title for login.html")


    def validateUserEmpty(self):
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide loginName!", msg, "invalid msg for alert1")
        time.sleep(2)
        alertObj.accept()
        time.sleep(2)

    def validatePasswordEmpty(self):
        alertObj = self.driver.switch_to.alert  # to get the alert obj
        msg = alertObj.text  # to get the alert msg
        self.assertEqual("Please provide Password!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()
        time.sleep(5)



