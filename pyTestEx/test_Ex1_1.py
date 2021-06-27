def add(a, b):
    return a + b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a * 1.0 / b


def maximum(a, b):
    return a if a >= b else b


def minimum(a, b):
    return a if a <= b else b

import pytest


NUMBER_1 = 3.0
NUMBER_2 = 2.0

def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0

def test_subtract():
    value = subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0

def test_subtract_negative():
    value = subtract(NUMBER_2, NUMBER_1)
    assert value == -1.0

def test_multiply():
    value = multiply(NUMBER_1, NUMBER_2)
    assert value == 6.0


def test_divide():
    value = divide(NUMBER_1, NUMBER_2)
    assert value == 1.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(5, 0)
    assert "division by zero" in str(e.value)