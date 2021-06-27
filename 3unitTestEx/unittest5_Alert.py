


from seleniumEx.myBasetest import BaseTest
import time
"""

how to get the alert object?
-----------------------
alertObj = self.driver.switch_to.alert


How to get the alert message?
----------------------------
msg=alertObj.text
 
 
How to click on OK button alert?
------------------------------
alertObj.accept()

How to click on cancel button alert?
------------------------------
alertObj.dismiss()


How to enter data to the alert?
 -------------------------------
alertObj.send_keys("https://www:facebook.com")


"""
class AlertTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("http://localhost:8087/myapp/alerts.html")
        time.sleep(2)

    """
    <input type="button" name="alert1" onclick="check1()" value="alert1"><br><br>
    """
    def testButton1(self):
        buttonObj = self.driver.find_element_by_name("alert1")
        buttonObj.click()

        time.sleep(3)
        alertObj = self.driver.switch_to.alert

        #validate the alert message
        self.assertEqual("Hello",alertObj.text, "invalid msg for alert1")


        #Click on OK
        alertObj.accept()
        time.sleep(3)



    """
      <input type="button" name="alert2" onclick="check2()" value="alert2"><br><br>
    """
    def testButton2Ok(self):
        buttonObj = self.driver.find_element_by_name("alert2")
        buttonObj.click()

        time.sleep(3)
        alertObj = self.driver.switch_to.alert

        # validate the alert message
        self.assertEqual("do you want to continue?", alertObj.text, "invalid msg for alert1")

        # Click on OK
        alertObj.accept()
        time.sleep(3)

        self.assertEqual("Google", self.driver.title)

    def testButton2Cancel(self):
        buttonObj = self.driver.find_element_by_name("alert2")
        buttonObj.click()

        time.sleep(3)
        alertObj = self.driver.switch_to.alert

        # validate the alert message
        self.assertEqual("do you want to continue?", alertObj.text, "invalid msg for alert1")

        # Click on cancel
        alertObj.dismiss()
        time.sleep(3)

        self.assertEqual("Gmail", self.driver.title)


    """
      <input type="button" name="alert3" onclick="check3()" value="alert3"><br><br>
    """
    def testButton3Ok(self):
        buttonObj = self.driver.find_element_by_name("alert3")
        buttonObj.click()

        time.sleep(3)
        alertObj = self.driver.switch_to.alert

        # validate the alert message
        self.assertEqual("enter page", alertObj.text, "invalid msg for alert1")

        # enter page name
        alertObj.send_keys("ex1.html")

        # Click on cancel
        alertObj.accept()
        time.sleep(3)

    def testButton3Cancel(self):
        buttonObj = self.driver.find_element_by_name("alert3")
        buttonObj.click()

        time.sleep(3)
        alertObj = self.driver.switch_to.alert

        # validate the alert message
        self.assertEqual("enter page", alertObj.text, "invalid msg for alert1")

        # enter page name
        alertObj.send_keys("ex1.html")

        # Click on cancel
        alertObj.dismiss()
        time.sleep(3)




