import unittest
from unittest_dataprovider import data_provider


class PythonOrgSearch(unittest.TestCase):
    data = lambda: (
        (1000, "kumar1"),
        (1001, "kuma2"),
        (1002, "kumar3"),
        (1003, "kumar4"),
        (1004,"kumar6")
    )

    @data_provider(data)
    def testEx2(self, id, name):
        print(id, name)
