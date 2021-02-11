#basetext
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import commons
from selenium import webdriver
import time

class commonpage:
    def __init__(self, driver):
        self.driver = driver
        print("constructor is called")





    def checkdisplayandenabled(self, *elements):
        for element in elements:

            self.assertTrue(element.is_enabled())
            self.assertTrue(element.is_displayed())

    def findbyname(self,name):

        elementobj = self.driver.find_element_by_name(name)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def findbyid(self,id):
        elementobj=self.driver.find_element_by_id(id)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def findbyxpath(self,xpath):
        elementobj=self.driver.find_element_by_xpath(xpath)
        self.checkdisplayandenabled( elementobj)
        return  elementobj

    def findbylink(self, link_text):
        elementobj = self.driver.find_element_by_link_text(link_text)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def checklinks(self):
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



















