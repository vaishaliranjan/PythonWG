import pytest


@pytest.fixture(scope="class", autouse=True)
def setup_class():
    print("Setup Class ")


@pytest.fixture(scope="module", autouse=True)
def setup_module2():
    print("Setup Module 2")


# @pytest.fixture(scope="session", autouse=True)
# def setup_session2():
#     print("Setup Session twice")

@pytest.fixture(scope="function", autouse=True)
def setup_function2():
    print("Setup FUnction twice")


def test1():
    print("Test 1")


def test2():
    print("Test 2")