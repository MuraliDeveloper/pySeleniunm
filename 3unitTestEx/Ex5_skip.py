"""
How to Ignore all test cases:
write @unittest.SkipTest before the class

How to skip the particular test case:
write  @unittest.skip("skip t3") before the test function.

"""

import unittest


#@unittest.SkipTest
class MyTest(unittest.TestCase):


    def test1(self):
        print("testcase 1 executed")

    @unittest.skip("skip t2")
    def test2(self):
        print("testcase 2 executed")

    @unittest.skip("skip t3")
    def test3(self):
        print("testcase 3 executed")


    def test4(self):
        print("testcase 4 executed")


    def test5(self):
        print("testcase 5 executed")









