

""""
<iframe id="fr1" src="frame1.html">/</iframe>
<iframe id="fr2" src="frame2.html">/</iframe>
<iframe id="fr3" src="frame3.html">/</iframe>
<iframe id="fr4" src="frame4.html">/</iframe>
"""

from seleniumEx.myBasetest import BaseTest
import time

class FramesTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("http://localhost:8087/myapp/frames.html")
        time.sleep(2)


    def testNoOfFrames(self):
        framesList = self.driver.find_elements_by_tag_name("iframe")
        self.assertEqual(4, len(framesList))

    """
        How to switch to a frame?
        ans)
          driver.switch_to.frame(<index>)
          driver.switch_to.frame(<frame id>)

        How to switch to a parent frame?  
        ans)
          driver.switch_to.default_content()  

    """
    def testFramesUsingId(self):

        #switch to frame 1
        self.driver.switch_to.frame("fr1")
        #<input type="text" name="data1">
        self.driver.find_element_by_name("data1").send_keys("kumar")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 2
        self.driver.switch_to.frame("fr2")
        self.driver.find_element_by_name("data2").send_keys("varma")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 3
        self.driver.switch_to.frame("fr3")
        self.driver.find_element_by_name("data3").send_keys("abcdef")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 4
        self.driver.switch_to.frame("fr4")
        self.driver.find_element_by_name("data4").send_keys("bangalore")
        time.sleep(3)
        self.driver.switch_to.default_content()

        self.driver.find_element_by_name("id").send_keys("12345")
        time.sleep(3)

    def testFramesUsingIndex(self):
        # switch to frame 1
        self.driver.switch_to.frame(0)
        # <input type="text" name="data1">
        self.driver.find_element_by_name("data1").send_keys("kumar")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 2
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_name("data2").send_keys("varma")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 3
        self.driver.switch_to.frame(2)
        self.driver.find_element_by_name("data3").send_keys("abcdef")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 4
        self.driver.switch_to.frame(3)
        self.driver.find_element_by_name("data4").send_keys("bangalore")
        time.sleep(3)
        self.driver.switch_to.default_content()

        self.driver.find_element_by_name("id").send_keys("12345")
        time.sleep(3)

    """
    iframe = self.driver.find_element_by_id('fr1')
    self.driver.switch_to.frame(iframe)
    //driver.switch_to_frame("//iframe[@src='demo.html']")
    """

    def testFramesUsinglocatorWebelementObj(self):
        # switch to frame 1
        iframe = self.driver.find_element_by_id('fr1')
        self.driver.switch_to.frame(iframe)
        # <input type="text" name="data1">
        self.driver.find_element_by_name("data1").send_keys("kumar")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 2
        iframe = self.driver.find_element_by_id('fr2')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_name("data2").send_keys("varma")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 3
        iframe = self.driver.find_element_by_id('fr3')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_name("data3").send_keys("abcdef")
        time.sleep(3)
        self.driver.switch_to.default_content()

        # switch to frame 4
        iframe = self.driver.find_element_by_id('fr4')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_name("data4").send_keys("bangalore")
        time.sleep(3)
        self.driver.switch_to.default_content()

        self.driver.find_element_by_name("id").send_keys("12345")
        time.sleep(3)













    def testUsingLoop(self):
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



