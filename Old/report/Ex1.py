import unittest

import HtmlTestRunner


class MyTest(unittest.TestCase):

    def test1(self):
        print("test1 - login")
        
    def test2(self):
        print("test2-register")



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Murali/Training/pythonWork/PySelenium/report'))