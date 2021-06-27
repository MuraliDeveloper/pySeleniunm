"""
<table border="1">
  <tr>
    <th>ID</th>
    <th>NAME</th>
    <th>AGE</th>
  </tr>
  <tr>
     <td>1000</td>
     <td>USER1</td>
     <td>45</td>
  </tr>
  <tr>
     <td>1001</td>
     <td>USER2</td>
     <td>54</td>
  </tr>
  <tr>
     <td>1002</td>
     <td>USER3</td>
     <td>78</td>
  </tr>
</table>

"""

from selenium.webdriver.common.keys import Keys

from seleniumEx.myBasetest import BaseTest
import time
from selenium.webdriver import ActionChains


class TableTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("http://localhost:8082/myapp/tables.html")
        self.driver.maximize_window()
        time.sleep(3)

    """
    #/html/body/table/tbody/tr[1]    ->get 1st row
    #/html/body/table/tbody/tr[1]/th[1] ->1st row , 1st column value


    #/html/body/table/tbody/tr[2]  ->2nd row
    #/html/body/table/tbody/tr[2]/td[1]  ->2nd row , 1st column value
    
    
    how to get all rows?
    rows = driver.find_elements_by_xpath("/html/body/table/tbody/tr")  #gets all the Table rows
    
    
    how to get all cols in a row?
    cols = driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")  #gets all the Table cols from 1st row
    
    How to get the column value?
    print ( driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th[1]").text )
    
    """
    def test1(self):
        rows = self.driver.find_elements_by_xpath("/html/body/table/tbody/tr")
        print("Rows= ",len(rows))

        cols = self.driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")
        print("cols= ", len(cols))

        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th[1]").text)
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th[2]").text)
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th[3]").text)

        print("********************2nd row*******************************")
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]").text)
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]").text)
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[3]").text)

        print("********************3rd row*******************************")
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[1]").text)
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[2]").text)
        print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[3]").text)

        print("using loops print all headers")
        for r in range(1,2):
            print("**************ROW" + str(r) + "*****************")
            for c in range(1, len(cols) + 1):
                print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/th["+str(c)+"]").text)

        print("using loops print all data")
        for r in range(2,len(rows) + 1):
            print("**************ROW"+str(r)+"*****************")
            for c in range(1, len(cols) + 1):
                print(self.driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text)







"""
assignment:
read from excel and compre with the html table

"""