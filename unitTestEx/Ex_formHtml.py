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

    def test3(self):
        citizenshipdropdownobj = self.driver.find_element_by_name("citizen")
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

    def test4(self):
        maleradiobuttonobj = self.driver.find_element_by_id("mRadio")
        femaleradiobuttonobj = self.driver.find_element_by_id("fRadio")
        otherradiobuttonobj = self.driver.find_element_by_id("oRadio")
        self.checkdisplayandenabled(maleradiobuttonobj,femaleradiobuttonobj,otherradiobuttonobj)
        self.assertTrue(maleradiobuttonobj.is_selected())
        self.assertFalse( femaleradiobuttonobj.is_selected())
        self.assertFalse( otherradiobuttonobj.is_selected())
        self.assertEqual(maleradiobuttonobj.get_attribute("type"), "radio")
        self.assertEqual( femaleradiobuttonobj.get_attribute("type"), "radio")
        self.assertEqual(otherradiobuttonobj.get_attribute("type"), "radio")
        maleradiobuttonobj.click()
        time.sleep(5)
        femaleradiobuttonobj.click()
        time.sleep(5)
        otherradiobuttonobj.click()
        time.sleep(5)

    def test5(self):
        passportchechboxobj = self.driver.find_element_by_name("proof1")
        voterchechboxobj = self.driver.find_element_by_name("proof2")
        panchechboxobj = self.driver.find_element_by_name("proof3")
        self.checkdisplayandenabled(passportchechboxobj,voterchechboxobj,panchechboxobj)
        self.assertFalse(passportchechboxobj.is_selected())
        self.assertFalse(voterchechboxobj.is_selected())
        self.assertTrue(panchechboxobj.is_selected())
        self.assertEqual(passportchechboxobj.get_attribute("type"), "checkbox")
        self.assertEqual(voterchechboxobj.get_attribute("type"), "checkbox")
        self.assertEqual(panchechboxobj.get_attribute("type"), "checkbox")

        passportchechboxobj.click()
        time.sleep(5)
        voterchechboxobj.click()
        time.sleep(5)
        panchechboxobj.click()
        time.sleep(5)

    def test6(self):
        submitbuttonobj = self.driver.find_element_by_name("submit")
        textareaobj = self.driver.find_element_by_name("address")
        self.checkdisplayandenabled(submitbuttonobj,textareaobj)
        textareaobj.send_keys("19-12,bairagapatteda,Tirupathi,AP")
        submitbuttonobj.click()



    def test2(self,):
        citydropdownobj = self.driver.find_element_by_name("city")
        all_options = citydropdownobj.find_elements_by_tag_name("option")
        self.checkdisplayandenabled(citydropdownobj)
        self.assertEqual(4, len(all_options))
        print(len(all_options))
        for option in all_options:
            print("Value is: ", option.get_attribute("value"))
            print("text  is: ", option.text)
        selectObj = Select(self.driver.find_element_by_name('city'))
        selectObj.select_by_index(2)
        time.sleep(5)
        selectObj.select_by_value('hyd')
        time.sleep(5)
        selectObj.select_by_visible_text('Mumbai')
        time.sleep(5)

    def test1(self):
        # open google.com

        firstnameobj = self.driver.find_element_by_name("uName")
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
    def test7(self):
        link1=self.driver.find_element_by_link_text("open for Next page"),
        self.checkdisplayandenabled(link1)
        link1.click()
        self.driver.back()
        link2 = self.driver.find_element_by_link_text("click here for next link")
        self.checkdisplayandenabled(link2)
        link2.click()
        #verify the page contain two links


    def test8(self):
        link1=self.driver.find_element_by_partial_link_text("open for")
        all_links = link1.find_elements_by_tag_name("a")

        self.assertEqual(2, len(all_links))

        self.checkdisplayandenabled(link1)
        link1.click()
        self.driver.back()
        link2 = self.driver.find_element_by_partial_link_text("click here")
        self.checkdisplayandenabled(link2)
        link2.click()
    """def test9(self):
        linkobj=self.driver.find_element_by_partial_link_text("open for")
        all_links = linkobj.find_elements_by_tag_name("a")
        self.assertEqual(2,len(all_links))
        linkobj.click()"""