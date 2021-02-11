import unittest
import commons

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "login.html")
        time.sleep(5)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
        self.login("admin", "mahetha")
        self.checklinks()

    def test1(self):
        #create new emp as manager
        #under the add new emp page manager drop down should contain the person name
        empobj=self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("addEmpLbl").click()
        time.sleep(5)
        self.findbyid("loginName").send_keys("deva")
        self.findbyid("password").send_keys("devanr")
        self.findbyname("fName").send_keys("deva")
        self.findbyname("lName").send_keys("kurthi")
        desginationobj=self.findbyname("designation")
        all_options=desginationobj.find_elements_by_tag_name("option")
        self.assertEqual(5, len(all_options))
        print(len(all_options))
        selectObj = Select(self.findbyname('designation'))
        selectObj.select_by_index(4)
        self.findbyid("fRadio").click()
        self.findbyname("dateOfBirth").send_keys("02/26/1995")
        self.findbyname("salary").send_keys("80000")
        self.findbyname("mobileNo").send_keys("4567891236")
        maritalobj = self.findbyname("maritalStatus")
        all_options = maritalobj.find_elements_by_tag_name("option")
        self.assertEqual(3, len(all_options))
        print(len(all_options))
        selectObj = Select(self.findbyname('maritalStatus'))
        selectObj.select_by_index(0)
        self.findbyid("acceptLabl").click()
        self.findbyid("submit").click()
        time.sleep(5)



        manobj=self.findbyname("manager.id")
        all_options =manobj.find_elements_by_tag_name("option")
        self.assertEqual(3, len(all_options))
        print(len(all_options))
        for option in all_options:
            print("Value is: ", option.get_attribute("value"))
            print("text  is: ", option.text)

        self.assertEqual("deva -  kurthi ",option.text)












