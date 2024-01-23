def setup_module(module):
    print("Before module")

def teardown_module(module):
    print("After module")

def setup_function(function):
    if function == test_test1:
        print("Before test1")
    elif function == test_test2:
        print("Before test 2")
    else:
        print("Before unnown function ")

def teardown_function(function):
    if function == test_test1:
        print("After test1")
    elif function == test_test2:
        print("After test 2")
    else:
        print("After unknown function ")
def test_test1():
    print("Executing test1")

def test_test2():
    print("Executing test2")