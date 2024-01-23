import pytest


@pytest.fixture(autouse=True)
def setup():
    print()
    print("SETUPPP")

#def test1(setup):

def test1():
    print("test 1")

#@pytest.mark.usefixtures("setup")
def test2():
    print("test 2")