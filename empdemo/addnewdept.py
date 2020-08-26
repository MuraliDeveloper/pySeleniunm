import time
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

    def testaddnewdept(self):
        deptobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(deptobj).perform()
        self.findbyid("addDeptLbl").click()
        self.findbyname("name").send_keys("Testing")
        dropdownobj=self.findbyname("manager.id")
        all_options = dropdownobj.find_elements_by_tag_name("option")
        self.assertEqual(7, len(all_options))
        selectObj = Select(self.findbyname('manager.id'))
        selectObj.select_by_index(5)
        self.findbyid("submit").click()
        time.sleep(5)
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("addEmpLbl").click()
        time.sleep(5)
        depobj=self.findbyname("department.id")
        all_options = depobj.find_elements_by_tag_name("option")
        self.assertEqual(5, len(all_options))
        print(len(all_options))
        self.assertEqual("Testing","//option[starts-with(text(), 'Testing')]")
        """for option in all_options:
            print("Value is: ", option.get_attribute("value"))
            print("text  is: ", option.text)

        


        #self.assertEqual("21", depobj.get_attribute("value"))

        #dept value should be in dropdown in add new emp page"""

    def testaddnewdeptwhichisalreadyexists(self):#it is adding same dept again without showing any warning msg that dept name already exist for same head
        deptobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(deptobj).perform()
        self.findbyid("addDeptLbl").click()
        self.findbyname("name").send_keys("Testing")
        dropdownobj=self.findbyname("manager.id")
        all_options = dropdownobj.find_elements_by_tag_name("option")
        self.assertEqual(7, len(all_options))
        selectObj = Select(self.findbyname('manager.id'))
        selectObj.select_by_index(5)
        self.findbyid("submit").click()
        time.sleep(5)
    def testwithemptyfield(self):
        deptobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(deptobj).perform()
        self.findbyid("addDeptLbl").click()
        self.findbyname("name")
        dropdownobj = self.findbyname("manager.id")
        all_options = dropdownobj.find_elements_by_tag_name("option")
        self.assertEqual(7, len(all_options))
        selectObj = Select(self.findbyname('manager.id'))
        selectObj.select_by_index(5)
        self.findbyid("submit").click()
        alertObj = self.driver.switch_to.alert
        msg = alertObj.text
        self.assertEqual("Please provide department Name!", msg, "invalid msg for alert1")
        time.sleep(5)
        alertObj.accept()

