import unittest

from unittest_dataprovider import data_provider


class MyTest(unittest.TestCase):


    #lambda method
    data = lambda: (
        (1000,),
        (1001,),
        (1002,),
        (1003,),
        (1004,),
        (1005, ),
        (1006, ),
        (1007, ),
        (1008, )
    )

    #test method
    @data_provider(data)
    def testProvider(self,num):
        print( num)

