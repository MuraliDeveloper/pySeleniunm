import unittest

import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from util.commons import getChromeDriver

#Not Done yet inprogress
class MyTest(unittest.TestCase):  # Create a class which is a childclass of unittest.testcase
    driver = None

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

    def setUp(self):
        print("setup function called")
        self.driver = getChromeDriver()
        self.driver.get("http://localhost:8082/EmpDemo/" )
        time.sleep(3)
        self.assertEqual("Employee Application", self.driver.title, "invalid title for login.html")
        self.login("admin", "admin")

        empobj = self.driver.find_element_by_id("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.driver.find_element_by_id("addEmpLbl").click()
        time.sleep(5)

    #WORKING
    def testAddNewEmp(self):
        empobj = self.driver.find_element_by_id("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.driver.find_element_by_id("addEmpLbl").click()
        time.sleep(5)

        self.driver.find_element_by_name("loginName").send_keys("soni")
        self.driver.find_element_by_name("password").send_keys("soni123")
        self.driver.find_element_by_name("fName").send_keys("soni")
        self.driver.find_element_by_name("lName").send_keys("modi")

        selectobj = Select(self.driver.find_element_by_name('designation'))
        selectobj.select_by_index(3)

        status = self.driver.find_element_by_id("fRadio").click()  # select radio button

        self.driver.find_element_by_name("dateOfBirth").send_keys("01/01/1998")

        selectobj = Select(self.driver.find_element_by_id('login.status'))
        selectobj.select_by_index(1)

        selectobj = Select(self.driver.find_element_by_id('department.id'))
        selectobj.select_by_index(1)

        selectobj = Select(self.driver.find_element_by_id('manager.id'))
        selectobj.select_by_index(1)

        self.driver.find_element_by_name("salary").send_keys("70000")

        self.driver.find_element_by_name("mobileNo").send_keys("9123456789")

        selectobj = Select(self.driver.find_element_by_name('maritalStatus'))
        selectobj.select_by_index(1)

        self.driver.find_element_by_name("addresses[0].addrLine1").send_keys("duvvada")

        self.driver.find_element_by_name("addresses[0].addrLine2").send_keys("visakha west")

        self.driver.find_element_by_name("addresses[0].city").send_keys("vizag")

        self.driver.find_element_by_name("addresses[0].state").send_keys("andhara pradesh")

        self.driver.find_element_by_name("addresses[0].country").send_keys("india")

        self.driver.find_element_by_name("addresses[0].pin").send_keys("530046")

        ############# second address

        self.driver.find_element_by_name("addresses[0].addrLine1").send_keys("duvvada new")

        self.driver.find_element_by_name("addresses[0].addrLine2").send_keys("visakha west new")

        self.driver.find_element_by_name("addresses[0].city").send_keys("vizag new")

        self.driver.find_element_by_name("addresses[0].state").send_keys("andhara pradesh")

        self.driver.find_element_by_name("addresses[0].country").send_keys("india")

        self.driver.find_element_by_name("addresses[0].pin").send_keys("530047")

        status = self.driver.find_element_by_id("accept").click()

        self.driver.find_element_by_id("submit").click()
        time.sleep(5)



    def test1(self):
        #create new emp as manager
        #under the add new emp page manager drop down should contain the person name
        empobj=self.driver.find_element_by_id("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.driver.find_element_by_id("addEmpLbl").click()
        time.sleep(5)
        self.driver.find_element_by_id("loginName").send_keys("deva")
        self.driver.find_element_by_id("password").send_keys("devanr")
        self.driver.find_element_by_name("fName").send_keys("deva")
        self.driver.find_element_by_name("lName").send_keys("kurthi")
        desginationobj=self.driver.find_element_by_name("designation")
        all_options=desginationobj.find_elements_by_tag_name("option")
        self.assertEqual(5, len(all_options))
        print(len(all_options))
        selectObj = Select(self.driver.find_element_by_name('designation'))
        selectObj.select_by_index(4)
        self.driver.find_element_by_id("fRadio").click()
        self.driver.find_element_by_name("dateOfBirth").send_keys("02/26/1995")
        self.driver.find_element_by_name("salary").send_keys("80000")
        self.driver.find_element_by_name("mobileNo").send_keys("4567891236")
        maritalobj = self.driver.find_element_by_name("maritalStatus")
        all_options = maritalobj.find_elements_by_tag_name("option")
        self.assertEqual(3, len(all_options))
        print(len(all_options))
        selectObj = Select(self.driver.find_element_by_name('maritalStatus'))
        selectObj.select_by_index(0)
        self.driver.find_element_by_id("acceptLabl").click()
        self.driver.find_element_by_id("submit").click()
        time.sleep(5)



        manobj=self.driver.find_element_by_name("manager.id")
        all_options =manobj.find_elements_by_tag_name("option")
        self.assertEqual(3, len(all_options))
        print(len(all_options))
        for option in all_options:
            print("Value is: ", option.get_attribute("value"))
            print("text  is: ", option.text)

        self.assertEqual("deva -  kurthi ",option.text)
















