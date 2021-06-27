"""
The xfailed test will be executed, but it will not be counted as part failed or passed tests.
There will be no traceback displayed if that test fails. We can xfail tests using
@pytest.mark.xfail.

"""

import pytest

def test_add_2():
	assert 100 + 200 == 300, "success"

@pytest.mark.xfail
def test_add_3():
	assert 15+13 == 28,"failed"

@pytest.mark.xfail
def test_add_4():
	assert 15+13 == 100,"failed"

def test_add_5():
	assert 3+2 == 5,"failed"

def test_add_6():
	assert 3+2 == 6,"failed"