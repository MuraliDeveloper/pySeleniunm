
"""
method override for 
setUpClass()  
-> is called before 1st test function
-> called one time

tearDownClass() 
-> is called after every the last function.
-> called one time

"""

import unittest

x = 10

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" perform before anything ")


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



    @classmethod
    def tearDownClass(cls):
        print(" perform after everything ")





