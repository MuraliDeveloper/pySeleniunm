#unittest2
import unittest
from basics import commons
import csv
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from basics.basetest import BaseTest


class MyTest(BaseTest):  # Create a class which is a childclass of unittest.testcase

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(commons.app_url + "form.html")
        time.sleep(5)
        self.assertEqual("my form page", self.driver.title, "invalid title for form.html")


    def test6(self):
        submitbuttonobj = self.findbyname("submit")
        textareaobj = self.findbyname("address")
        textareaobj.send_keys("19-12,bairagapatteda,Tirupathi,AP")
        submitbuttonobj.click()


    def test1(self):

        firstnameobj = self.findbyname("uName")
        lastnameobj = self.findbyname("LName")
        passwordobj = self.findbyname("password")
        self.checktext(firstnameobj,lastnameobj)
        self.assertEqual(passwordobj.get_attribute("type"), "password")
        f = open("file.csv", 'r', newline='')
        csvFile = csv.reader(f)
        for row in csvFile:
            firstnameobj.send_keys(row[0])
            lastnameobj.send_keys(row[1])
            passwordobj.send_keys(row[2])
        time.sleep(5)

        f.close()




    """def test10(self):
        imageobj = self.driver.find_element_by_name("fileupload")
        self.checkdisplayandenabled(imageobj)"""

