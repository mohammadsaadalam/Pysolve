import unittest
from pysolve import validators as vl


class TestValidators(unittest.TestCase):
    def test_parse_int(self):
        self.assertEqual(vl.parse_int(" 42 "), 42)
        self.assertEqual(vl.parse_int("-7"), -7)
        for bad in ("", "abc", "3.5"):
            with self.assertRaises(ValueError):
                vl.parse_int(bad)

    def test_non_negative(self):
        self.assertEqual(vl.parse_non_negative("0"), 0)
        with self.assertRaises(ValueError):
            vl.parse_non_negative("-1")

    def test_int_list(self):
        self.assertEqual(vl.parse_int_list("1 2, 3,4"), [1, 2, 3, 4])
        with self.assertRaises(ValueError):
            vl.parse_int_list("   ")
        with self.assertRaises(ValueError):
            vl.parse_int_list("1 x 3")

    def test_choice(self):
        self.assertEqual(vl.parse_choice("2", 0, 3), 2)
        with self.assertRaises(ValueError):
            vl.parse_choice("9", 0, 3)


if __name__ == "__main__":
    unittest.main()
