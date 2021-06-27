import pytest

"""
Here
fixture : passes diff data to different test cases

Fixtures are pytests spiffy setup and
cleanup functions that can also do dependency injection.

We have a fixture named getData. This method will return a list of 3 values.
We have 3 test methods comparing against each of the values.

"""

@pytest.fixture
def getData():
	x=25
	y =35
	z=45
	return [x,y,z]

def test_Data1(getData):
	x=35
	assert getData[0]==x," comparison failed"

def test_Data2(getData):
	y=35
	assert getData[1]==y,"  comparison failed"

def test_Data3(getData):
	z=35
	assert getData[2]==z," comparison failed"

