"""
Parametrized Tests
What if we want to run the same test procedure with multiple input combos?
pytest has a decorator for that! Let’s write a new test for multiplication with parametrized inputs:
"""
import pytest
@pytest.mark.parametrize(
  "a,b,expected",
  [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)]
)
def test_Multiply(a, b, expected):
    print(a,b,expected)
    assert a * b == expected


import pytest
@pytest.mark.parametrize("num1, num2, output",[
    (5,5,10),
    (3,5,12)])
def test_add(num1, num2, output):
	assert num1+num2 == output,"failed"

