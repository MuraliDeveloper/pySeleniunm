import unittest

from unittest_dataprovider import data_provider


class MyTest(unittest.TestCase):

    data = lambda: (
        (1000,"user1",),
        (1001,"user2",),
        (1002,"user3",),
        (1003,"user4",),
        (1004,"user5",),
        (1005, "user65",),
        (1006,"user7", ),
        (1007,"user8", ),
        (1008, "user9",)
    )

    @data_provider(data)
    def testProvider(self,num, name):
        print("processing " , num , name)

