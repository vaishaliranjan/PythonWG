import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print("Setup Session")

@pytest.fixture(scope="module", autouse=True)
def setup_module1():
    print("Setup Module 1")

@pytest.fixture(scope="function", autouse=True)
def setup_function():
    print("Setup Function")

def test1():
    print("Test 1")
def test2():
    print("Test 2")