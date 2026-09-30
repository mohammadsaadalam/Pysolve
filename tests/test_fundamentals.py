import unittest
from pysolve import fundamentals as fd


class TestFundamentals(unittest.TestCase):
    def test_swap(self):
        self.assertEqual(fd.swap_with_temp(1, 2), (2, 1))
        self.assertEqual(fd.swap_without_temp(5, -3), (-3, 5))
        self.assertEqual(fd.swap_tuple("a", "b"), ("b", "a"))

    def test_sum_and_digits(self):
        self.assertEqual(fd.sum_natural(10), 55)
        self.assertEqual(fd.sum_natural(0), 0)
        self.assertEqual(fd.count_digits(0), 1)
        self.assertEqual(fd.count_digits(-12345), 5)
        self.assertEqual(fd.sum_of_digits(9875), 29)

    def test_factorial(self):
        self.assertEqual(fd.factorial(0), 1)
        self.assertEqual(fd.factorial(5), 120)
        self.assertEqual(fd.factorial(20), 2432902008176640000)
        with self.assertRaises(ValueError):
            fd.factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(fd.fibonacci_nth(0), 0)
        self.assertEqual(fd.fibonacci_nth(1), 1)
        self.assertEqual(fd.fibonacci_nth(10), 55)
        self.assertEqual(fd.fibonacci_series(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fd.fibonacci_series(0), [])
        with self.assertRaises(ValueError):
            fd.fibonacci_nth(-2)

    def test_reverse(self):
        self.assertEqual(fd.reverse_number(1234), 4321)
        self.assertEqual(fd.reverse_number(-120), -21)
        self.assertTrue(fd.is_palindrome_number(1221))
        self.assertFalse(fd.is_palindrome_number(123))

    def test_base_conversion(self):
        self.assertEqual(fd.decimal_to_base(10, 2), "1010")
        self.assertEqual(fd.decimal_to_base(255, 16), "FF")
        self.assertEqual(fd.decimal_to_base(0, 8), "0")
        self.assertEqual(fd.base_to_decimal("1010", 2), 10)
        self.assertEqual(fd.base_to_decimal("ff", 16), 255)
        for n in range(0, 200):
            for base in (2, 8, 16):
                self.assertEqual(fd.base_to_decimal(fd.decimal_to_base(n, base), base), n)
        with self.assertRaises(ValueError):
            fd.decimal_to_base(5, 1)
        with self.assertRaises(ValueError):
            fd.base_to_decimal("102", 2)
        with self.assertRaises(ValueError):
            fd.decimal_to_base(-4, 2)

    def test_characters(self):
        self.assertEqual(fd.char_to_number("A"), 65)
        self.assertEqual(fd.number_to_char(97), "a")
        self.assertEqual(fd.text_to_numbers("Hi"), [72, 105])
        self.assertEqual(fd.digit_string_to_number("-4096"), -4096)
        with self.assertRaises(ValueError):
            fd.char_to_number("ab")
        with self.assertRaises(ValueError):
            fd.digit_string_to_number("12a")


if __name__ == "__main__":
    unittest.main()
