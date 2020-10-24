import unittest
from unittest_dataprovider import data_provider
"""
for working with data provide
use unittest_dataprovider package


1.execute the same Test case but with different data 
ex: search in google , but every time with different data

solution: 
- use data provider
providing the custom data to the test-case

impact:
----------
the test case will run based on the no of data you provide
   
changes:
-----------

1.write a lambda method that provides the data
    data = lambda: (
        (1000),
        (2000),
        (3000),
        (4000)
    )
2.How to pass data to the test case        

@data_provider(data)
    def testEx2(self, id):
        print(id)

"""

class PythonOrgSearch(unittest.TestCase):
    data = lambda: (
        (1000),
        (1001),
        (1002),
        (1003)
      )

    @data_provider(data)
    def testEx2(self, num):
        print(num)