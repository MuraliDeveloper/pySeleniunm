#unittest2
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

    def test3(self):
        citizenshipdropdownobj = self.findbyname("citizen")
        all_options = citizenshipdropdownobj.find_elements_by_tag_name("option")
        self.assertEqual(4, len(all_options))
        print(len(all_options))
        expectedcitzenshiptext = ["India", "Pakistan", "AMERICA", "AUSTRLIA"]
        expectedcitzenshipvalues = ["IN", "PAK", "US", "AUS"]
        count = 0
        for option in all_options:
            self.assertEqual(expectedcitzenshipvalues[count], option.get_attribute("value"),
                             "invalid city found" + option.get_attribute("value"))
            self.assertEqual(expectedcitzenshiptext[count], option.text, "invalid city found" + option.text)
            count = count + 1
        selectObj = Select(self.findbyname('citizen'))
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

    def test4(self):
        maleradiobuttonobj = self.findbyid("mRadio")
        femaleradiobuttonobj = self.findbyid("fRadio")
        otherradiobuttonobj = self.findbyid("oRadio")

        self.driver.save_screenshot("test.png")
        self.checkradiobutton(maleradiobuttonobj,femaleradiobuttonobj,otherradiobuttonobj)
        self.assertTrue(maleradiobuttonobj.is_selected())
        self.assertFalse( femaleradiobuttonobj.is_selected())
        self.assertFalse( otherradiobuttonobj.is_selected())
        maleradiobuttonobj.click()
        time.sleep(5)
        femaleradiobuttonobj.click()
        time.sleep(5)
        otherradiobuttonobj.click()
        time.sleep(5)

    def test5(self):
        passportchechboxobj = self.findbyname("proof1")
        voterchechboxobj = self.findbyname("proof2")
        panchechboxobj = self.findbyname("proof3")
        self.checkcheckbox(passportchechboxobj,voterchechboxobj,panchechboxobj)
        self.assertFalse(passportchechboxobj.is_selected())
        self.assertFalse(voterchechboxobj.is_selected())
        self.assertTrue(panchechboxobj.is_selected())
        passportchechboxobj.click()
        time.sleep(5)
        voterchechboxobj.click()
        time.sleep(5)
        panchechboxobj.click()
        time.sleep(5)

    def test6(self):
        submitbuttonobj = self.findbyname("submit")
        textareaobj = self.findbyname("address")
        textareaobj.send_keys("19-12,bairagapatteda,Tirupathi,AP")
        submitbuttonobj.click()



    def test2(self):
        citydropdownobj = self.findbyname("city")
        all_options = citydropdownobj.find_elements_by_tag_name("option")
        self.assertEqual(4, len(all_options))
        print(len(all_options))
        for option in all_options:
            print("Value is: ", option.get_attribute("value"))
            print("text  is: ", option.text)
        selectObj = Select(self.findbyname('city'))
        selectObj.select_by_index(2)
        time.sleep(5)
        selectObj.select_by_value('hyd')
        time.sleep(5)
        selectObj.select_by_visible_text('Mumbai')
        time.sleep(5)

    def test1(self):
        # open google.com

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
    def test7(self):
        link1=self.findbylink("open for Next page")
        link1.click()
        self.driver.back()
        link2 = self.findbylink("click here for next link")
        link2.click()
        #verify the page contain two links

    def test8(self):

        all_links =self.driver.find_elements_by_tag_name("a")
        self.assertEqual(2, len(all_links))
        link1 = self.findbyplink("open for")
        link1.click()
        self.driver.back()
        link2 = self.findbyplink("click here")

        link2.click()

    """def test10(self):
        imageobj = self.driver.find_element_by_name("fileupload")
        self.checkdisplayandenabled(imageobj)"""

