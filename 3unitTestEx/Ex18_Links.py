
"""
write test cases for
1.open driver
2.Open http://127.0.0.1:8000/htmls/links/
3.validate the links and images
5.close driver


"""


import time


from basics.basetest import BaseTest
from basics.commons import  BASE_URL



class MyTest(BaseTest):


    def setUp(self) :
        BaseTest.setUp(self)
        self.driver.get(BASE_URL+"links/")

        time.sleep(3)

    def testLink1(self):
        links = self.driver.find_elements_by_tag_name("a")
        self.assertEqual( len(links)  ,8,"invlaid no of links")
        time.sleep(3)


        images =  self.driver.find_elements_by_tag_name("img")
        self.assertEqual(len(images), 3, "invlaid no of images")
        time.sleep(3)
