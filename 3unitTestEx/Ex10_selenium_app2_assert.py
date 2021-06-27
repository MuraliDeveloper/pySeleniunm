
"""
Write test cases for 
1.open driver
2.Open http://127.0.0.1:8000/htmls/ex1/
3.Open http://127.0.0.1:8000/htmls/ex2/
4.close driver

validate the title

How to validate/assert or compare the results?
ans)
use the assert functions available for "TestCase"

ex:
self.assertEqual() -> compares actual values , expected value


How to fail a test case?
ans):
  raise RuntimeError('Test error!')

 how to validate the title for a page?
validate: compare the expected value and actual value
          if expected is not matching with actual then test case should fail
ex:
self.assertEqual()
self.assertNotEqual()
self.assertFalse()
self.assertTrue()
self.assertGreater()
self.assertGreaterEqual()
self.assertLess()
self.assertLessEqual()
"""


import time
import unittest
from basics.commons import getChromeDriver, BASE_URL

driver = None

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global  driver
        driver = getChromeDriver()

    @classmethod
    def tearDownClass(cls):
        # close driver
        global driver
        driver.close()

    def test1(self):
        # open google.com
        driver.get(BASE_URL+"ex1/")
        expected = "Html application Ex1"
        self.assertEqual(expected, driver.title , "Invalid Title")
        time.sleep(5)

    def test2(self):
       # open google.com
        driver.get(BASE_URL+"ex2/")
        expected = "Html application Ex2"
        self.assertEqual(expected, driver.title) #assert for exact entire match
        self.assertIn( "application" , driver.title,) #assert for partial match
        time.sleep(5)

    def test3(self):
        # open google.com
        driver.get(BASE_URL + "alert/")
        expected = "Home Page"
        self.assertEqual(expected, driver.title, "Invalid Title")
        time.sleep(5)

  # How to fail test cases

    def testFail(self):
        a=12
        if(a<35):
            raise RuntimeError('Test error!')

    def testFail(self):
        a=90
        self.failIf(a<35)

"""
assertEqual(a,b)	a==b
assertNotEqual(a,b)	a != b
assertTrue(x)	(x) is True
assertFalse(x)	(x) is False
assertIs(a,b)	a is b
assertIs(a,b)	a is b
assertIsNot(a, b)	a is not b
assertIsNone(x)	x is None
assertIsNotNone(x)	x is not None
assertIn(a, b)	a in b
assertNotIn(a, b)	a not in b
assertIsInstance(a, b)	isinstance(a, b)
assertNotIsInstance(a, b)	not isinstance(a, b)

"""









