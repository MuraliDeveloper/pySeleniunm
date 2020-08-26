import unittest


from suit.ex11 import MyTest1
from suit.ex2 import MyTest2

ts1 = unittest.TestLoader().loadTestsFromTestCase(MyTest1)
ts2 = unittest.TestLoader().loadTestsFromTestCase(MyTest2)


mysuit = unittest.TestSuite([ts1,ts2])

unittest.TextTestRunner().run(mysuit)