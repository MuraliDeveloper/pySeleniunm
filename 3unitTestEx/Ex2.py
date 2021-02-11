import unittest
"""
method override for 
setUp()  
-> is called before every test method
-> any common prerequisite steps can be written here

tearDown() 
-> is called after every test method
-> any post test case clean up activities can be taken care here.

"""
class MyTest(unittest.TestCase):

    def setUp(self):
        print("setUp executed")

    def tearDown(self):
        print("tearDown executed")

    def test1(self):
        print("testcase 1 executed")

    def test2(self):
        print("testcase 2 executed")

    def test3(self):
        print("testcase 3 executed")

    def test4(self):
        print("testcase 4 executed")

    def test5(self):
        print("testcase 5 executed")