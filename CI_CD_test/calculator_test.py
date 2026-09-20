#adding unit test cases for calculator.py   
from calculator import add, multiply, subtract, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5
    ##assert subtract(5, 0) == 8  simply to understand the test case will fail if the expected value is wrong
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 2) == -3
    assert divide(0, 1) == 0
#how to run the test cases
#To run the test cases, you can use a testing framework like pytest.
#pytest test_calculator.py
