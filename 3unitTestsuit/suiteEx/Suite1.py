import unittest

from suiteEx import Test1

#create the testObjs using the test classes
ts1 = unittest.TestLoader().loadTestsFromTestCase(Test1.MyTest1)

#add to the suite
mysuit = unittest.TestSuite([ts1])

#run the suite
unittest.TextTestRunner().run(mysuit)



