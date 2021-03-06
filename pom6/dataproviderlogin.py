import time
from unittest_data_provider import data_provider
from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
import csv
from pom.loginpage import loginpage

f = open("login.csv", 'r', newline='')

reader = csv.DictReader(f)
list=[]
for row in reader:
    t=(row["userName"],row["password"],row["status"])
    list.append(t)


f.close()
data = lambda: list




class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase
   
    @data_provider(data)
    def testEx2(self, userName, password, status):
        BaseTest.setUp(self)
        self.loginpageobj = loginpage(self.driver)

        time.sleep(5)

        self.loginpageobj.login(userName, password)
        print(userName, password)
        if (status == 1):
            print("login sucess")

        else:
            print("login failure")

        time.sleep(5)
