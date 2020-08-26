import unittest

from Old.unitTestEx.Ex1 import MyTest

ts1 = unittest.TestLoader().loadTestsFromTestCase(MyTest)

mysuit = unittest.TestSuite([ts1])

unittest.TextTestRunner().run(mysuit)

ts1 = unittest.TestLoader().loadTestsFromTestCase(MyTest1)
ts2 = unittest.TestLoader().loadTestsFromTestCase(MyTest2)


mysuit = unittest.TestSuite([ts1,ts2])

unittest.TextTestRunner().run(mysuit)