from unittest import TestCase

'''
TEST DRIVEN DEVELOPMENT -> RED, GREEN, REFACTOR
'''
def fizzbuzz(value):
    if value%3==0:
        if value%5==0:
            return "fizzbuzz"
        return "fizz"
    if value%5==0:
        return "buzz"
    return str(value)


class Testing(TestCase):
    # def test_canCallFizzBuzz(self):
    #     fizzbuzz()

    def fizzbuzz_check(self, value, expected_value):
        getVal = fizzbuzz(value)
        return  self.assertEqual(getVal, expected_value)

    def test_get1ForPassedIn1(self):
        self.fizzbuzz_check(1,"1")

    def test_get2ForPassedIn2(self):
        self.fizzbuzz_check(2,"2")

    def test_getFizzForPassedIn3(self):
        self.fizzbuzz_check(3,"fizz")

    def test_getBuzzForPassedIn5(self):
        self.fizzbuzz_check(5,"buzz")

    def test_getFizzForPassedIn6(self):
        self.fizzbuzz_check(6,"fizz")

    def test_getBuzzForPassedIn10(self):
        self.fizzbuzz_check(10,"buzz")

    def test_getFizzBuzzForPassedIn15(self):
        self.fizzbuzz_check(15,"fizzbuzz")