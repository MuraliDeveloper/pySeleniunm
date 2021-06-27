
from selenium.webdriver.common.keys import Keys

from seleniumEx.myBasetest import BaseTest
import time
from selenium.webdriver import ActionChains


class TableTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("http://localhost:8082/myapp/xpath2.html")
        self.driver.maximize_window()
        time.sleep(3)

    """
       <a href="https://www.gmail.com">click here</a>  <br/>
       <a href="https://www.fb.com">click here</a>  <br/>
    """
    def test1(self):
        link =  self.driver.find_element_by_xpath("//a[@href='https://www.gmail.com']")
        link.click()
        time.sleep(3)

    def test2(self):
        link = self.driver.find_element_by_xpath("//a[@href='https://www.fb.com']")
        link.click()
        time.sleep(3)

    """
         <input type="button" value="RESET" onclick="f1()"/><br/><br/>
         <input type="button" value="ADD" onclick="f2()"/><br/>
         <p id="dynamicData"></p>
         ADD selected
         RESET selected
    """
    def test3(self):
        bt1 = self.driver.find_element_by_xpath("//input[@value='RESET']")
        bt1.click()
        dynaText = self.driver.find_element_by_id("dynamicData").text
        self.assertEqual("RESET selected", dynaText)
        time.sleep(3)


        bt2 = self.driver.find_element_by_xpath("//input[@value='ADD']")
        bt2.click()
        dynaText = self.driver.find_element_by_id("dynamicData").text
        self.assertEqual("ADD selected", dynaText)
        time.sleep(3)

    """
        <p class="show"> Hello1 </p>
        <p class="show"> Hello2 </p>
        <p class="show"> Hello3  </p>
        <p class="show"> Hello4  </p>
    
    """
    def testPara(self):
        elements = self.driver.find_elements_by_xpath("//p[@class='show']")
        self.assertEqual(4 , len(elements))

        for element in elements:
            self.assertTrue("Hello" in element.text)










