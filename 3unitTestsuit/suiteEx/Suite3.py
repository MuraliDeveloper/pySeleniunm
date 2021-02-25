import unittest

from suiteEx import Test1, Test2, Test3

#create the testObjs using the test classes
ts1 = unittest.TestLoader().loadTestsFromTestCase(Test1.MyTest1)
ts2 = unittest.TestLoader().loadTestsFromTestCase(Test2.MyTest2)
ts3 = unittest.TestLoader().loadTestsFromTestCase(Test3.MyTest3)
#add to the suite
mysuit = unittest.TestSuite([ts1,ts2,ts3])

#run the suite
unittest.TextTestRunner().run(mysuit)



