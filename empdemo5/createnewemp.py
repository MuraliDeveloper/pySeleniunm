import unittest


from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from basics import commons
from empdemo5.basetest import BaseTest


class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "login.html")
        time.sleep(5)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
        self.login("admin", "admin")
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



    def testaddnewemp(self):
        self.findbyname("loginName").send_keys("soni")
        self.findbyname("password").send_keys("soni123")
        self.findbyname("fName").send_keys("soni")
        self.findbyname("lName").send_keys("modi")

        selectobj = Select(self.findbyname('designation'))
        selectobj.select_by_index(3)

        status = self.findbyname("fRadio").click()  # select radio button

        self.findbyname("dateOfBirth").send_keys("01/01/1998")

        selectobj = Select(self.findbyid('login.status'))
        selectobj.select_by_index(1)

        selectobj = Select(self.findbyid('department.id'))
        selectobj.select_by_index(4)

        selectobj = Select(self.findbyid('manager.id'))
        selectobj.select_by_index(1)

        self.findbyname("salary").send_keys("70000")

        self.findbyname("mobileNo").send_keys("9123456789")

        selectobj = Select(self.findbyid('maritalStatus'))
        selectobj.select_by_index(1)

        self.findbyname("addresses[0].addrLine1").send_keys("duvvada")

        self.findbyname("addresses[0].addrLine2").send_keys("visakha west")

        self.findbyname("addresses[0].city").send_keys("vizag")

        self.findbyname("addresses[0].state").send_keys("andhara pradesh")

        self.findbyname("addresses[0].country").send_keys("india")

        self.findbyname("addresses[0].pin").send_keys("530046")

        ############# second address

        self.findbyname("addresses[0].addrLine1").send_keys("duvvada new")

        self.findbyname("addresses[0].addrLine2").send_keys("visakha west new")

        self.findbyname("addresses[0].city").send_keys("vizag new")

        self.findbyname("addresses[0].state").send_keys("andhara pradesh")

        self.findbyname("addresses[0].country").send_keys("india")

        self.findbyname("addresses[0].pin").send_keys("530047")

        status = self.findbyid("accept").click()

        self.findbyid("submit").click()
        time.sleep(5)














