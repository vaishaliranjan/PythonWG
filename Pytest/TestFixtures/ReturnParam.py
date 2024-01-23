import pytest


@pytest.fixture(params=[1,2,3])
def setup(request):
    return request.param

def test1(setup):
    print("{}".format(setup))