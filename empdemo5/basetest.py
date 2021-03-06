
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from basics import commons
import time

class BaseTest(unittest.TestCase):     # Create a class which is a childclass of unittest.testcase
    driver=None

    def setUp(self):
        print("setup function called")
        self.driver = commons.getChromeDriver()
        time.sleep(5)

    def tearDown(self):
        print("teardown function is called")
        self.driver.close()

    def checkDisplayAndEnabled(self, *elements):
        for element in elements:
            self.assertTrue(element.is_enabled())
            self.assertTrue(element.is_displayed())

    def findbyname(self,name):
        elementobj = self.driver.find_element_by_name(name)
        self.checkDisplayAndEnabled(elementobj)
        return elementobj
    def findbyid(self,id):
        elementobj=self.driver.find_element_by_id(id)
        self.checkDisplayAndEnabled(elementobj)
        return elementobj
    def findbyxpath(self,xpath):
        elementobj=self.driver.find_element_by_xpath(xpath)
        self.checkDisplayAndEnabled(elementobj)
        return  elementobj

    def findbylink(self, link_text):
        elementobj = self.driver.find_element_by_link_text(link_text)
        self.checkDisplayAndEnabled(elementobj)
        return elementobj

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

    def checkHeaderlinks(self):
        self.linkvalidation("logout","empProfile","mySubordinates",)

        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.linkvalidation("empCreate", "searchEmp","empGetByFilters","getAllEmps")

        DepartmentLblobj = self.findbyid("DepartmentLbl")
        action = ActionChains(self.driver)
        action.move_to_element(DepartmentLblobj).perform()
        self.linkvalidation("deptCreate","searchDept","getDepts")


    def linkvalidation(self,*hrefs):
        for href in hrefs:
            self.findbyxpath("//a[@href='"+href+"']")



















