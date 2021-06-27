
import pytest
@pytest.mark.parametrize("num1, num2, output",[
    (5,5,10),
    (3,5,12)])
def test_add(num1, num2, output):
	assert num1+num2 == output,"failed"

