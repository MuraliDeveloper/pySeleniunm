"""
setUpClass -> 1 time.   [before anything ]
tearDownClass -> 1 time. [ after everything]

setUp -> everytime for every test function.[before every test function]
tearDown ->  everytime for every test function.[after every test function]
"""

import unittest

 

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" perform before anything ")

    @classmethod
    def tearDownClass(cls):
        print(" perform after everything ")

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









