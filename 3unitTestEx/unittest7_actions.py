"""
Actions:
 --------
 -mouse operations
- keyboard opeartions

Action Class in Selenium is a built-in feature provided handling keyboard and mouse events.
 - It includes various operations such as multiple events clicking by control key, drag and drop events

  ex:
 ->KeyPress,key up, key down, enter, tab, pageup, page down and context menu interactions.
-> hover over and drag and drop.
->double click , right click'



 KEY:
-------------
sendKeys(keysToSend): Sends a series of keystrokes onto the element.
keyDown(theKey): Sends a key press without release it.
keyUp(theKey): Performs a key release.



Mouse:
--------------
click(): Clicks on the element.
doubleClick (): Double clicks on the element.
contextClick() : Performs a context-click (right-click) on the element.
clickAndHold(): Clicks at the present mouse location without releasing.
moveToElement(toElement):

How to move mouse over element?
------------------------------------------------------
use action obj to move the mouse over element


action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_id("mylabel")
action.move_to_element(firstLevelMenu).perform()



# or
ActionChains(driver).send_keys(Keys.SHIFT, Keys.TAB, Keys.SHIFT).perform()




"""
from selenium.webdriver.common.keys import Keys

"""
1.open google,.com
2.enter selenium
3.Press 'key_down' for 3 times
4.Press Enter key


How to create the actions obj?
ans)
action = ActionChains(self.driver)
 
 
"""

from seleniumEx.myBasetest import BaseTest
import time
from selenium.webdriver import ActionChains


class MultiWindowsTest(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("https://www.google.com")
        time.sleep(2)

    """
        1.Open google.com
        2.type selenium
        3.Press Enter key
    """

    def test2(self):
        textobj = self.driver.find_element_by_name("q")
        textobj.send_keys("selenium")
        time.sleep(5)
        textobj.send_keys(Keys.ENTER)
        time.sleep(5)

    #working
    """
    1.Open Google
    2.Enter selenium
    3.Press ARROW_DOWN
    4.Press ARROW_DOWN
    5.Press ARROW_DOWN
    6.Press Enter
    """
    def test3(self):
        textobj = self.driver.find_element_by_name("q")
        textobj.send_keys("selenium")
        time.sleep(2)
        textobj.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        textobj.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        textobj.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        textobj.send_keys(Keys.ENTER)
        time.sleep(2)

    def test4(self):
        textobj = self.driver.find_element_by_name("q")
        textobj.send_keys("selenium")
        time.sleep(2)
        moves = [Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_UP]

        textobj.send_keys(moves)
        time.sleep(5)

    """
    Enter data "selenium" using Actions
    for entering text --> send_keys_to_element() method
    """
    def testGoogle1(self):
        element = self.driver.find_element_by_name("q")
        time.sleep(3)
        action = ActionChains(self.driver)
        action.send_keys_to_element(element, "selenium").perform()
        time.sleep(3)

    """
          Enter the data "selenium" in capital by performing "shift" key using Actions
          For long press  -> key_down()  method
          For releasing key  ->key_up() method
    """
    def testGoogele2(self):
        textobj = self.driver.find_element_by_name("q")
        action = ActionChains(self.driver)

        action.key_down(Keys.SHIFT)
        action.send_keys_to_element(textobj, "selenium")
        action.key_up(Keys.SHIFT)
        action.send_keys_to_element(textobj, "web driver")
        action.send_keys_to_element(textobj, Keys.ENTER)
        action.perform()

    """
       Enter the data "selenium" in capital by performing "shift" key using Actions
       For long press  -> key_down()  method
       For releasing key  ->key_up() method
    """
    def testGoogle22(self):
        element = self.driver.find_element_by_name("q")
        action = ActionChains(self.driver)

        action.key_down(Keys.SHIFT).send_keys_to_element(element, "selenium").key_up(Keys.SHIFT).perform()

        time.sleep(3)

    """
    Enter data "selenium" and double click using Actions
    for double click use: double_click(element)
    """
    def testGoogle3(self):
        element = self.driver.find_element_by_name("q")
        time.sleep(3)
        action = ActionChains(self.driver)
        action.send_keys_to_element(element, "selenium").double_click(element).perform()
        time.sleep(3)

    """
        Enter data "selenium" and right click using Actions
        for right click use: context_click(element)
    """

    def testGoogle4(self):
        element = self.driver.find_element_by_name("q")
        time.sleep(3)
        action = ActionChains(self.driver)
        action.send_keys_to_element(element, "selenium").context_click(element).perform()
        time.sleep(3)

    """
           Enter data "selenium"  + double click + right click using Actions
           for right click use: context_click(element)
    """
    def testGoogle5(self):
        element = self.driver.find_element_by_name("q")
        time.sleep(3)
        action = ActionChains(self.driver)
        action.send_keys_to_element(element, "selenium").double_click(element).context_click(element).perform()
        time.sleep(3)

    def testGoogle56(self):
        textField = self.driver.find_element_by_name("q")
        action = ActionChains(self.driver)
        action.move_to_element(textField)

        action.click()

        action.send_keys_to_element(textField, "selenium")

        action.double_click(textField)

        action.context_click(textField)

        action.perform()
        time.sleep(2)

    def testGoogle6(self):
        element = self.driver.find_element_by_name("q")
        time.sleep(3)
        action = ActionChains(self.driver)

        time.sleep(3)








