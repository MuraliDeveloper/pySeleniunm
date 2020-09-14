#basetext
import unittest
from selenium import webdriver
from basics import commons

class BaseTest(unittest.TestCase):     # Create a class which is a childclass of unittest.testcase
    driver=None

    def setUp(self):
        print("setup function called")
        self.driver = webdriver.Chrome(executable_path=commons.driver_url)

    def tearDown(self):
        print("teardown function is called")
        self.driver.close()

    def checkdisplayandenabled(self, *elements):
        for element in elements:
            self.assertTrue(element.is_enabled())
            self.assertTrue(element.is_displayed())

    def checkcheckbox(self,*elements):
        for element in elements:
            self.assertEqual(element.get_attribute("type"), "checkbox")

    def checkradiobutton(self, *elements):
        for element in elements:
            self.assertEqual(element.get_attribute("type"), "radio")
    def checktext(self,*elements):
        for element in elements:
            self.assertEqual(element.get_attribute("type"), "text")
    def findbyname(self,name):

        elementobj = self.driver.find_element_by_name(name)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def findbyid(self,id):
        elementobj=self.driver.find_element_by_id(id)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def findbytagname(self,tag_name):
        elementobj = self.driver.find_element_by_tag_name(tag_name)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def findbylink(self,link_text):
        elementobj = self.driver.find_element_by_link_text(link_text)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def findbyplink(self,link_text):
        elementobj = self.driver.find_element_by_partial_link_text(link_text)
        self.checkdisplayandenabled(elementobj)
        return elementobj
    def findbyxpath(self,xpath):
        elementobj=self.driver.find_element_by_xpath(xpath)
        self.checkdisplayandenabled( elementobj)
        return  elementobj









