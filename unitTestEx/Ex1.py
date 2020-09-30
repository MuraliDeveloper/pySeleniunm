import unittest


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("hello")

    @classmethod
    def tearDownClass(cls):
            print("bye")
    def setUp(self):
        print("Setup for every test case")

    def tearDown(self):
        print("tearDown for every test case")

    def test1(self):
        print("test1 - login")
        
    def test2(self):
        print("test2-register")

   # @unittest.skip("skipped")
    @unittest.SkipTest
    def test3(self):
        print("test2-register")

if __name__ == "__main__":
    unittest.main()