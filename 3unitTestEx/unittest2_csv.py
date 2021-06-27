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

    
    """
    validate and send data to firstname,lastname ,password
    
    """
    def testReadFromCSV(self):
        # open google.com
        # get web elements obj
        firstnameobj = self.driver.find_element_by_name("uName")#get we using field name
        lastnameobj = self.driver.find_element_by_name("LName")
        passwordobj = self.driver.find_element_by_name("password")

       
        self.checkdisplayandenabled(firstnameobj,lastnameobj, passwordobj)
        self.assertEqual(firstnameobj.get_attribute("type"), "text")
        self.assertEqual(lastnameobj.get_attribute("type"), "text")
        self.assertEqual(passwordobj.get_attribute("type"), "password")
        f = open("file.csv", 'r', newline='')
        csvFile = csv.reader(f)
        for row in csvFile:
            firstnameobj.send_keys(row[0])
            lastnameobj.send_keys(row[1])
            passwordobj.send_keys(row[2])
        time.sleep(5)


        f.close()

    def testReadFromCSV2(self):

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



    
    
  