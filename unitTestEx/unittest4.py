#unittest4

import unittest
import commons
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

    def test2(self,):
        citydropdownobj = self.driver.find_element_by_name("city")
        all_options = citydropdownobj.find_elements_by_tag_name("option")
        self.assertEqual(4, len(all_options))
        print(len(all_options))
        expectedcitytext=["Hyderabad","Bangalore","Chennai","Mumbai"]
        expectedcityvalues = ["hyd", "bang", "chen", "mum"]
        count=0
        for option in all_options:

            self.assertEqual(expectedcityvalues[count], option.get_attribute("value"),"invalid city found"+option.get_attribute("value"))
            self.assertEqual(expectedcitytext[count], option.text,"invalid city found"+option.text)
            count=count+1
        selectObj = Select(self.driver.find_element_by_name('city'))
        selectObj.select_by_index(2)
        time.sleep(5)
        selectObj.select_by_value('hyd')
        time.sleep(5)
        selectObj.select_by_visible_text('Mumbai')

        time.sleep(5)

        def test3(self):
            citizenshipdropdownobj = self.driver.find_element_by_name("citizen")
            all_options = citizenshipdropdownobj.find_elements_by_tag_name("option")
            self.assertEqual(4, len(all_options))
            print(len(all_options))
            for option in all_options:
                print("Value is: ", option.get_attribute("value"))
                print("text  is: ", option.text)

            selectObj = Select(self.driver.find_element_by_name('citizen'))
            selectObj.select_by_index(1)
            time.sleep(5)
            selectObj.select_by_value('IN')
            time.sleep(5)
            selectObj.select_by_visible_text('AMERICA')

            selectObj.deselect_by_index(2)
            time.sleep(5)
            selectObj.deselect_by_value('IN')
            time.sleep(5)
            selectObj.deselect_by_visible_text('AMERICA')

            time.sleep(5)
