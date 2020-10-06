import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from basics import commons
from basics.commons import getChromeDriver


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = getChromeDriver()

    def tearDown(self):
        self.driver.close()

    def test_search_in_python_org(self):
        self.driver.get(commons.App_URL + "2.html")
        self.assertEqual("my title", self.driver.title,"invalid title")
        self.assertIn("Python", self.driver.title)



    def test3(self):
        a=90
        if a<35:
            raise RuntimeError('Test error!')
    def testFail(self):
        a=90
        self.failIf(a<35)

if __name__ == "__main__":
    unittest.main()

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

    """
    stop test case:   raise RuntimeError('Test error!')
    
    """