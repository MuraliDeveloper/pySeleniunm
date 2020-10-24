import unittest
import commons
import csv
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

from basics.basetest import BaseTest



class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "xpath1.html")
        self.driver.implicitly_wait(10)
        self.assertEqual("Insert title here", self.driver.title, "invalid title for xpath1.html")

    def test1(self):
        """



        """


        #link1=self.driver.find_element_by_xpath("/html/body/a[1]")
        link1=self.findbyxpath("//a[@href='https://www.gmail.com']")
        link1.click()
        time.sleep(5)
        #<a href="https://www.google.com">click here</a>
    def test2(self):
        #link2=self.driver.find_element_by_xpath("/html/body/a[2]")
        link2=self.findbyxpath("//a[@href='https://www.google.com']")
        link2.click()
        time.sleep(5)
    def test3(self):
        #attribute perfect match
        firstobj=self.findbyxpath("//input[@type='password']")
        firstobj.send_keys("mahetha")
        time.sleep(5)
        secondobj=self.findbyxpath("//label[@id='error']")
        self.assertEqual("Enter values here",secondobj.text)
        time.sleep(5)
        thirdobj=self.findbyxpath("//input[@value='RESET']")
        thirdobj.clear()
        thirdobj.send_keys("mahetha")
        time.sleep(5)
    def test4(self):
        #attribute similar match
        self.findbyxpath("//a[contains(@href,'gmail')]").click()

    def test5(self):
        # attribute similar match
        self.findbyxpath("//a[contains(@href,'google')]").click()
    def test6(self):
        thirdobj = self.findbyxpath("//input[contains(@value,'RESET')]")
        thirdobj.clear()
        thirdobj.send_keys("mahetha")

    def test7(self):
         button1obj=self.findbyxpath("//input[@type='submit' and @name='btnLogin']")
         button1obj.click()
         alertObj = self.driver.switch_to.alert  # to get the alert obj
         msg = alertObj.text  # to get the alert msg
         self.assertEqual("button1 selected", msg, "invalid msg for alert1")
         time.sleep(5)

    def test8(self):
        button2obj = self.findbyxpath("//input[@name='email' or @placeholder='Work Email']")
        button2obj.send_keys("mahetha@gmail.com")
        time.sleep(5)
        labelobj=self.findbyxpath("//label[starts-with(@id,'message')]")
        self.assertEqual("Hello", labelobj.text)
        link1obj=self.findbyxpath("//a[starts-with(text(), 'START')]")
        link1obj.click()
        time.sleep(5)
    def test9(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email' or @placeholder='Work Email']")))
        element.send_keys("mahetha@gmail.com")
    def test10(self):
        self.driver.get("https://www.youtube.com")
        self.driver.execute_script("window.scrollTo(0, 1000);")













