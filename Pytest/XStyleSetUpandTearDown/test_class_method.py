class TestClass:
    @classmethod
    def setup_class(cls):
        print("Before class")
    @classmethod
    def teardown_class(cls):
        print("After class")

    def setup_method(self, function):
        if function == self.test_test1:
            print("Before test1")
        elif function == self.test_test2:
            print("Before test 2")
        else:
            print("Before unknown function ")

    def teardown_method(self, function):
        if function == self.test_test1:
            print("After test1")
        elif function == self.test_test2:
            print("After test 2")
        else:
            print("After unknown function ")
    def test_test1(self):
        print("Executing test1")

    def test_test2(self):
        print("Executing test2")