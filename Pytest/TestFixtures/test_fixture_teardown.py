import pytest
@pytest.fixture()
def setup1():
    print()
    print("SETUP 1")
    yield
    print("TEARDOWN 1")

@pytest.fixture()
def setup2(request):
    print()
    print("SETUP 2")
    def teardown_A():
        print("TEARDOWN A")
    def teardown_B():
        print("TEARDOWN B")
    request.addfinalizer(teardown_A)
    request.addfinalizer(teardown_B)


def test1(setup1):
    print("test 1")

@pytest.mark.usefixtures("setup2")
def test2():
    print("test 2")