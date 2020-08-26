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

    def testshowallemp(self):
        empobj = self.findbyid("EmployeeLbl")
        action = ActionChains(self.driver)
        action.move_to_element(empobj).perform()
        self.findbyid("showEmpsLbl").click()
        rows = self.driver.find_elements_by_xpath("/html/body/table/tbody/tr")  # gets all the Table rows
        print(len(rows))

        cols = self.driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/td")  # gets all the column object only for row num1
        print(len(cols))
        print("printing colums")
        count = 0
        expectedcolheaders = ["ID", "First Name", "Last Name", "Designation", "Gender", "Department", "Join Date",
                              "Mobile No", "Staus", "Action"]

        for c in range(1, len(cols) + 1):
                data = self.driver.find_element_by_xpath("/html/body/table/thead/tr/th[" + str(c) + "]")

                self.assertEqual(expectedcolheaders[count], data.text, "invalid city found" + data.text)



                count = count + 1

        for r in range(1, len(rows) +1):  # every rows
            for c in range(1, len(cols) + 1):# every column
                identifier="/html/body/table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]"
                #print(identifier)
                data = self.driver.find_element_by_xpath(identifier)
                print(data.text)







#validate column names


    #validate every row contain edit and delete
    """rows=self.findbyxpath("/html/body/table/thead/tr")

        print(type(rows))

        rows = self.findbyxpath("/html/body/table/tbody/tr")

        print("count",len(rows))
        /html/body/table/thead/tr/th[1]"""










