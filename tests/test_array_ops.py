import unittest
from pysolve import array_ops as ao


class TestArrayOps(unittest.TestCase):
    def test_reverse_does_not_modify_input(self):
        original = [1, 2, 3, 4]
        self.assertEqual(ao.reverse_array(original), [4, 3, 2, 1])
        self.assertEqual(original, [1, 2, 3, 4])
        self.assertEqual(ao.reverse_array([]), [])
        self.assertEqual(ao.reverse_array([7]), [7])

    def test_counting(self):
        self.assertEqual(ao.count_occurrences([1, 2, 2, 3, 2], 2), 3)
        self.assertEqual(ao.count_occurrences([], 5), 0)
        self.assertEqual(ao.frequency_table([1, 1, 2]), {1: 2, 2: 1})

    def test_max_min(self):
        self.assertEqual(ao.find_max([3, -1, 9, 4]), 9)
        self.assertEqual(ao.find_min([3, -1, 9, 4]), -1)
        with self.assertRaises(ValueError):
            ao.find_max([])
        with self.assertRaises(ValueError):
            ao.find_min([])

    def test_sort(self):
        self.assertEqual(ao.insertion_sort([5, 2, 9, 1, 5]), [1, 2, 5, 5, 9])
        self.assertTrue(ao.is_sorted([1, 2, 2, 3]))
        self.assertFalse(ao.is_sorted([2, 1]))

    def test_remove_duplicates(self):
        self.assertEqual(ao.remove_duplicates_sorted([1, 1, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(ao.remove_duplicates_sorted([]), [])
        self.assertEqual(ao.remove_duplicates_set([3, 1, 3, 2, 1]), [3, 1, 2])
        with self.assertRaises(ValueError):
            ao.remove_duplicates_sorted([3, 1, 2])

    def test_partition(self):
        self.assertEqual(ao.partition([5, 1, 8, 5, 3], 5), ([1, 3], [5, 5], [8]))

    def test_kth_smallest(self):
        data = [7, 10, 4, 3, 20, 15]
        ordered = ao.insertion_sort(data)
        for k in range(1, len(data) + 1):
            self.assertEqual(ao.kth_smallest(data, k), ordered[k - 1])
        self.assertEqual(ao.kth_smallest([2, 2, 2], 3), 2)
        with self.assertRaises(ValueError):
            ao.kth_smallest(data, 0)
        with self.assertRaises(ValueError):
            ao.kth_smallest(data, 7)
        with self.assertRaises(ValueError):
            ao.kth_smallest([], 1)


if __name__ == "__main__":
    unittest.main()
