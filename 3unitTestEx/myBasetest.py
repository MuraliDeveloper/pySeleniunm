import unittest
from basics.commons import getChromeDriver


BASE_URL = "http://localhost:8087/myapp/"

class BaseTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self. driver = getChromeDriver()


    def tearDown(self):
        self.driver.close()