import unittest

from suiteEx import Test1, Test2

#create the testObjs using the test classes
ts1 = unittest.TestLoader().loadTestsFromTestCase(Test1.MyTest1)
ts2 = unittest.TestLoader().loadTestsFromTestCase(Test2.MyTest2)

#add to the suite
mysuit = unittest.TestSuite([ts1,ts2])

#run the suite
unittest.TextTestRunner().run(mysuit)



