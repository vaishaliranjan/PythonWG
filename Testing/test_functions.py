from unittest import TestCase
from Testing.functions import divide, multiply

class TestFunction(TestCase):
    def test_divide_result(self):
        dividend=15
        divisor=3
        expected_result= 5.0
        self.assertAlmostEqual(divide(dividend,divisor),expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 3
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        self.assertRaises(ValueError,lambda: divide(25,0))
        # with self.assertRaises(ValueError):
        #     divide(25,0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected =15
        self.assertEqual(multiply(15), expected)

    def test_multiply_zero(self):
        expected =0
        self.assertEqual(multiply(0), expected)

    def test_multiply_result(self):
        expected =15
        self.assertEqual(multiply(3,5), expected)

    def test_multiply_result_with_zero(self):
        expected =0
        self.assertEqual(multiply(3,5,0), expected)

    def test_multiply_negatives(self):
        expected =-30
        self.assertEqual(multiply(3,5,-2), expected)

    def test_multiply_float(self):
        expected =6.0
        self.assertEqual(multiply(3.0,2), expected)