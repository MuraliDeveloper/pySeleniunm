import time
import unittest
from selenium.webdriver.support.select import Select

from empdemo.basetest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains

from pom import commons
from pom.commonpage import commonpage


class addnewemppage(commonpage,unittest.TestCase):
    def open(self):
        self.empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(self.empobj).perform()
        self.findbyid("addEmpLbl").click()
        time.sleep(5)

    def intializeelement(self):

        self.loginobj=self.findbyid("loginName")
        self.passobj=self.findbyid("password")
        self.firstnameobj=self.findbyname("fName")
        self.lastnameobj=self.findbyname("lName")
        self.desginationobj = self.findbyname("designation")
        all_options = self.desginationobj.find_elements_by_tag_name("option")
        #self.assertEqual(5, len(all_options))
        print(len(all_options))
        selectObj = Select(self.findbyname('designation'))
        selectObj.select_by_index(3)
        self.radioobj=self.findbyid("fRadio")
        self.dobobj= self.findbyname("dateOfBirth")
        self.salaryobj=self.findbyname("salary")
        self.mobileobj=self.findbyname("mobileNo")
        maritalobj = self.findbyname("maritalStatus")
        all_options = maritalobj.find_elements_by_tag_name("option")
        #self.assertEqual(3, len(all_options))
        print(len(all_options))
        selectObj = Select(self.findbyname('maritalStatus'))
        selectObj.select_by_index(0)
        self.acceptobj=self.findbyid("acceptLabl")

        self.submitobj=self.findbyid("submit")

    def addnewemp(self,login,password,fname,lname,dob,salary,mobile ):
        self.open()
        self.intializeelement()


        self.loginobj.send_keys(login)
        self.passobj.send_keys(password)
        self.firstnameobj.send_keys(fname)
        self.lastnameobj.send_keys(lname)
        self.radioobj.click()
        self.dobobj.send_keys(dob)
        self.salaryobj.send_keys(salary)
        self.mobileobj.send_keys(mobile)
        self.acceptobj.click()
        self.submitobj.click()
        time.sleep(5)


        


