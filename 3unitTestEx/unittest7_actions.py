import unittest
import commons
import csv
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from basics.basetest import BaseTest

"""
How to move the mouse near the element
solution)

1.get the web element object (where we need to move the mouse)
2.create the actions object
3.call the move_to_element() method
4.call the perform method


How to create the actions obj?
solution)
action = ActionChains(self.driver)
"""


class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "data.html")
        time.sleep(5)
        self.assertEqual("data page", self.driver.title, "invalid title for alert.html")

    def test1(self):
        #mouse operations
        get_div = self.driver.find_element_by_class_name('round-button')
        self.assertEqual("Click Here",get_div.text)
        imageobj=self.findbyxpath("//img[@src='VoterID.JPG']")
        action = ActionChains(self.driver)
        action.move_to_element(imageobj).perform()
        time.sleep(5)
        linkobj=self.findbyid("mylabel")
        action = ActionChains(self.driver)
        action.move_to_element(linkobj).perform()
        time.sleep(5)

        textField = self.findbyname("name")
        action = ActionChains(self.driver)
        action.move_to_element(textField)
        time.sleep(5)
        action.click()
        time.sleep(5)
        action.send_keys_to_element(textField, "selenium")
        time.sleep(5)
        action.double_click(textField)
        time.sleep(5)
        action.context_click(textField)
        time.sleep(5)
        action.perform()

        time.sleep(5)
        action.move_to_element(textField).click().send_keys_to_element(textField, "selenium").double_click(
            textField).context_click(textField).perform()
        time.sleep(5)
    """
    1.Open google.com
    2.type selenium
    3.Press Enter key
    """
    def test2(self):
        self.driver.get("https://www.google.com")
        textobj=self.findbyname("q")
        textobj.send_keys("selenium")
        time.sleep(5)
        textobj.send_keys(Keys.ENTER)
        time.sleep(5)
   """
    1.Open google.com
    2.Press SHIFT
    3.Type "selenium"
    4.Release SHIFT
    5.Type "web driver"
    6.Press Enter key
    """
    def test4(self):
        self.driver.get("https://www.google.com")
        textobj = self.findbyname("q")
        time.sleep(5)
        action = ActionChains(self.driver)
        action.key_down(Keys.SHIFT).send_keys_to_element(textobj, "selenium").key_up(Keys.SHIFT)\
            .send_keys_to_element(textobj, " web driver")\
            .send_keys_to_element(textobj, Keys.ENTER)\
            .perform()

        """
        action.key_down(Keys.SHIFT)
        action.send_keys_to_element(textobj, "selenium")
        action.key_up(Keys.SHIFT)
        action.send_keys_to_element(textobj, "web driver")
        action.send_keys_to_element(textobj, Keys.ENTER)
        action.perform()
        """
        time.sleep(5)
    
    """
    1.Open google.com
    2.type selenium
    3.Press Arrow Down
    4.Press Arrow Down
    5.Press Arrow Down
    6.Press Enter key
    """
    def test3(self):
        self.driver.get("https://www.google.com")
        textobj = self.findbyname("q")
        textobj.send_keys("selenium")
        time.sleep(5)
        textobj.send_keys(Keys.ARROW_DOWN)
        textobj.send_keys(Keys.ARROW_DOWN)
        textobj.send_keys(Keys.ARROW_DOWN)
        textobj.send_keys(Keys.ENTER)
    
    def test4(self):
        self.driver.get("https://www.google.com")
        textobj = self.findbyname("q")
        time.sleep(5)
        action = ActionChains(self.driver)
        action.key_down(Keys.SHIFT)
        action.send_keys_to_element(textobj, "selenium")
        action.key_up(Keys.SHIFT)
        action.send_keys_to_element(textobj, "web driver")
        action.send_keys_to_element(textobj, Keys.ENTER)
        action.perform()
        time.sleep(5)

    def testGoogle8(self):
                self.driver.get("https://www.google.com")
                textobj = self.driver.find_element_by_name("q")
                time.sleep(5)

                textobj.send_keys("selenium")
                time.sleep(3)
                textobj.send_keys(Keys.ARROW_DOWN)
                time.sleep(3)
                textobj.send_keys(Keys.ARROW_DOWN)
                time.sleep(3)
                textobj.send_keys(Keys.ARROW_DOWN)
                time.sleep(3)
                textobj.send_keys(Keys.ENTER)
                time.sleep(3) 


    def test5(self):
        self.driver.get("https://www.google.com")
        cookies = self.driver.get_cookies()

        for cookie in cookies:
            print(type(cookie))
            print(cookie)
            self.assertTrue("domain" in cookie.keys())
        self.driver.delete_all_cookies()
        print(self.driver.current_url)
        print(self.driver.session_id)





