import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from basics import commons
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path =commons.driver_url)

    def tearDown(self):
        self.driver.close()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertEqual("my title", driver.title,"invalid title")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


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