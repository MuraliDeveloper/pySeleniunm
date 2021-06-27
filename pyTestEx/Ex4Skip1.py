"""

Pytest Xfail / Skip Tests
There will be some situations where we don't want to execute a test, or a test case is not relevant for a particular time. In those situations, we have the option to Xfail the test or skip the tests

Skipping a test means that the test will not be executed. We can skip tests using
@pytest.mark.skip.

"""
import pytest
@pytest.mark.skip
def test_add_1():
	assert 100+200 == 400,"failed"

@pytest.mark.skip
def test_add_2():
	assert 100+200 == 300,"failed"

def test_add_2():
	assert 100 + 200 == 300, "success"
