from pytest import approx,raises
import pytest

@pytest.mark.test1
def test1():
    assert 1==1

@pytest.mark.test2

def test2():
    assert 1.0==1.0


def test3():
    assert "1"=="1"

def test4():
    assert {"1":1}=={"1":1}

def test5():
    assert (1.0+2.0)== approx(3.0)

def raiseException():
    raise ValueError

def test_raiseException():
    with raises(ValueError):
        raiseException()
