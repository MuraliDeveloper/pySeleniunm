#unittest1

import unittest
from basics import commons
from selenium import webdriver
import time
from basics.basetest import BaseTest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time


class MyTest(BaseTest):     # Create a class which is a childclass of unittest.testcase

    def test2(self):

        # open google.com
        self.driver.get(commons.App_URL + "frames.html")
        time.sleep(5)
        iFrames = self.driver.find_elements_by_tag_name('iframe')

        print("No of frames : ", len(iFrames))
        self.driver.switch_to_default_content()
        self.driver.find_element_by_tag_name('input').send_keys('hello welcome')



        for index in range(len(iFrames)):
            self.driver.switch_to_default_content()

            iframe = self.driver.find_elements_by_tag_name('iframe')[index]

            self.driver.switch_to.frame(iframe)

            # highlight the contents of the selected iframe

            self.driver.find_element_by_tag_name('input').send_keys('hello' + str(index))

            time.sleep(2)

        self.driver.switch_to_default_content()
        iframe = self.driver.find_element_by_id('fr1')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_name('data1').send_keys('bye1' )
        time.sleep(2)

        self.driver.switch_to_default_content()
        iframe = self.driver.find_element_by_id('fr2')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_tag_name('input').send_keys('bye2')
        time.sleep(2)

        self.driver.switch_to_default_content()
        iframe = self.driver.find_element_by_id('fr3')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_tag_name('input').send_keys('bye3')
        time.sleep(2)

        self.driver.switch_to_default_content()
        iframe = self.driver.find_element_by_id('fr4')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_tag_name('input').send_keys('bye4')
        time.sleep(2)



"""
        ########Section-2

        # switch to a specific iframe (First frame) using Id as locator

       

        time.sleep(2)

        driver.find_element_by_id('s').send_keys("Selected")

        driver.switch_to.default_content()

        ########Section-3

        # switch to a specific iframe (Second frame) using name as locator

        iframe = driver.find_element_by_name('frame2')

        driver.switch_to.frame(iframe)

        time.sleep(2)

        driver.find_element_by_tag_name('a').send_keys(Keys.CONTROL, 'a')
"""

