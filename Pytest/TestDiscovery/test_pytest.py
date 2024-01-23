import pytest

def test_testcase():
    assert True

def mytest_testcase():
    assert True

def test_3_testcase():
    assert True

class TestClass:
    def test_something1(self):
        assert True

    def my_test_something1(self):
        assert True

#IN PYTEST
# function name must start with test
# file name must start or end with test
# class name must start with Test