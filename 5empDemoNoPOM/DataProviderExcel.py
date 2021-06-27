import time
import unittest
from unittest_dataprovider import data_provider

import csv

"""
steps:
1.read from csv and convert csv data to list of tuples
2.keep inside the lambda

"""

f = open("login.csv", 'r', newline='')
reader = csv.DictReader(f)
list=[]
for row in reader:
    t=(row["userName"],row["password"],row["status"])
    list.append(t)
f.close()


data = lambda: list


from util.commons import getChromeDriver


class MyTest(unittest.TestCase):  # Create a class which is a childclass of unittest.testcase
    driver = None

    def setUp(self):
        self.driver = getChromeDriver()
        self.driver.get("http://localhost:8082/EmpDemo/" )
        time.sleep(3)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
   
    @data_provider(data)
    def testEx2(self, userName, password, status):
        self.login(userName, password)
        print(userName, password)

        if (status == 1): # Login success
            time.sleep(3)
            self.assertEqual("Employee Profile", self.driver.title, "invalid title for home page")
        else: # Login Failure
            time.sleep(3)
            self.assertEqual("Welcome to Employee Application", self.driver.title, "invalid title for login.html")

            errorObj = self.driver.find_element_by_xpath("//font[@color='Red']")
            self.assertTrue(errorObj.is_enabled())
            self.assertTrue(errorObj.is_displayed())
            self.assertEqual("Invalid Login.", errorObj.text, "invalid error msg")

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
