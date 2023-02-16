
from package1 import module1

"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""


# def inc(x):
#     return x + 1


def test_answer():
    assert module1.myReturn() == 4



def test_integer():
    assert module1.myInteger() == 8


def test_boolean():
    assert module1.myBoolean() == True



def test_string():
    assert module1.myString() == "Hello, world!"

