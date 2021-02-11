"""
unittest:
--------------
- test framework / test engine
- using unit test we will run the test cases
- write one function for every test case
- every  test function is independent.

Steps:
----------
1.import the unittest package
import unittest

2.create a class that extends unittest.TestCase

3.inside the class write the functions

4.run the class using the test framework .i.r. unitest

or use
if __name__ == "__main__":
    unittest.main()



"""
import unittest

class MyTest(unittest.TestCase):

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