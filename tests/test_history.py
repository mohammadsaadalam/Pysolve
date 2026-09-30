import unittest
from pysolve import history as hist


class TestHistory(unittest.TestCase):
    def setUp(self):
        hist.clear_history()

    def test_add_and_get(self):
        rec = hist.add_record("Arrays", "Reverse array", [1, 2], [2, 1])
        self.assertEqual(rec["id"], 1)
        self.assertEqual(len(hist.get_history()), 1)

    def test_counts_and_sets(self):
        hist.add_record("F", "Factorial", 5, 120)
        hist.add_record("F", "Factorial", 6, 720)
        hist.add_record("A", "Kth smallest", "x", 3)
        self.assertEqual(hist.count_by_operation(), {"Factorial": 2, "Kth smallest": 1})
        self.assertEqual(hist.unique_operations(), {"Factorial", "Kth smallest"})
        self.assertEqual(hist.most_used_operation(), ("Factorial", 2))
        tried, not_tried = hist.coverage(["Factorial", "Fibonacci"])
        self.assertEqual(tried, {"Factorial"})
        self.assertEqual(not_tried, {"Fibonacci"})

    def test_empty(self):
        self.assertIsNone(hist.most_used_operation())
        self.assertEqual(hist.get_history(), [])


if __name__ == "__main__":
    unittest.main()
