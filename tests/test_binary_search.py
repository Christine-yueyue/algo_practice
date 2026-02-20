import unittest
from algo_practice.arrays.binary_search import binary_search

# test_binary_search.py

import unittest
from algo_practice.arrays.binary_search import binary_search

# In unittest, test classes are required because the framework is class-based 
# and uses inheritance from TestCase to discover and manage tests.
class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 3, 5, 7, 9]
        self.test_empty_array_arr = []
        self.single_arr = [42]

    def test_found_middle(self):
        self.assertEqual(binary_search(self.arr, 5), 2)

    def test_found_first(self):
        self.assertEqual(binary_search(self.arr, 1), 0)

    def test_found_last(self):
        self.assertEqual(binary_search(self.arr, 9), 4)

    def test_not_found(self):
        self.assertEqual(binary_search(self.arr, 6), -1)

    def test_empty_array(self):
        self.assertEqual(binary_search(self.test_empty_array_arr, 10), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search(self.single_arr, 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search(self.single_arr, 7), -1)

    def test_duplicates_target_exists(self):
        # binary search may return any valid index with the target
        arr = [1, 2, 2, 2, 3]
        idx = binary_search(arr, 2)
        self.assertIn(idx, [1, 2, 3])

    def test_negative_numbers(self):
        arr = [-10, -3, 0, 5, 9]
        self.assertEqual(binary_search(arr, -3), 1)

    def test_float_values(self):
        arr = [0.1, 0.5, 1.2, 3.3]
        self.assertEqual(binary_search(arr, 1.2), 2)


if __name__ == "__main__":
    unittest.main()
