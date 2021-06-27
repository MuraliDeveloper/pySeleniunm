"""

<a href="https://www.youtube.com" id="ytUrl">Click here for Youtube</a> <br/><br/>
<a href="https://www.google.com">Click here for Google</a> <br/><br/>
<a href="https://www.fb.com">Click here for Facebook</a><br/><br/>

<a href="form.html">Click here for form</a><br/><br/>
<a href="alert.html">Click here for alert</a><br/><br/>
<a href="styles.html">Click here for styles</a><br/><br/>

<br/> <br/> <br/>
 <a href="https://www.gmail.com" target="_blank">Click Here for Gmail</a>

1.How to get all the links ?
ans)
 links = self.driver.find_elements_by_tag_name("a")

2.How to get single web element obj for a link
ans)
Use methods
- find_element_by_link_text()
- find_element_by_partial_link_text()

3.How to click on link?
ans)
Use click() method

"""
from seleniumEx.myBasetest import BaseTest
import time

class FormTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("http://localhost:8087/myapp/links.html")
        time.sleep(2)

    def testNoOfLinks(self):
        links = self.driver.find_elements_by_tag_name("a")
        self.assertEqual(8, len(links))

    def testClickUsingLinkText(self):
        link1 = self.driver.find_element_by_link_text("Click here for Youtube")
        #self.assertEqual(link2.get_attribute("href"), "https://www.gmail.com")
         #link1
        link1.click()
        time.sleep(3)

        self.driver.back()
        time.sleep(3)

        # link2
        link2 = self.driver.find_element_by_link_text("Click here for Google")
        link2.click()
        time.sleep(3)

        self.driver.back()
        time.sleep(3)

        # link3
        link3 = self.driver.find_element_by_link_text("Click here for Facebook")
        link3.click()
        time.sleep(3)

        self.driver.back()
        time.sleep(3)

    def testClickUsingPartialLinkText(self):
        link1 = self.driver.find_element_by_partial_link_text("Youtube")
        # self.assertEqual(link2.get_attribute("href"), "https://www.gmail.com")
        # link1
        link1.click()
        time.sleep(3)

        self.driver.back()
        time.sleep(3)

        # link2
        link2 = self.driver.find_element_by_partial_link_text("Google")
        link2.click()
        time.sleep(3)

        self.driver.back()
        time.sleep(3)

        # link3
        link3 = self.driver.find_element_by_partial_link_text("Facebook")
        link3.click()
        time.sleep(3)

        self.driver.back()
        time.sleep(3)


        """
        
        images =  self.driver.find_elements_by_tag_name("img")
        self.assertEqual(len(images), 3, "invlaid no of images")
        time.sleep(3)
        """

