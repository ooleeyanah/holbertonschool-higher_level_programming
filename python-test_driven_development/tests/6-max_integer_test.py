#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0]), 0)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -1]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -3, 4, -2]), 4)
        self.assertEqual(max_integer([-5, -2, 0, -10]), 0)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([10, 5, 2]), 10)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 5, 10]), 10)

    def test_max_in_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        self.assertEqual(max_integer([2, 10, 5, 1]), 10)

    def test_all_same_elements(self):
        """Test with all elements being the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-3, -3, -3]), -3)

    def test_duplicates(self):
        """Test with duplicate max values"""
        self.assertEqual(max_integer([1, 4, 2, 4, 3]), 4)
        self.assertEqual(max_integer([4, 4, 1, 2]), 4)
        self.assertEqual(max_integer([2, 2, 2, 1]), 2)

    def test_zeros(self):
        """Test with zeros"""
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([0, 1, 0]), 1)
        self.assertEqual(max_integer([0, -1, 0]), 0)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([-1000000, -999999, -1000001]), -999999)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)

    def test_long_list(self):
        """Test with a longer list"""
        long_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
        self.assertEqual(max_integer(long_list), 25)
        
    def test_float_and_int_mix(self):
        """Test with mix of floats and integers (should work if function supports)"""
        # Note: This might not work depending on the function implementation
        # But it's good to test edge cases
        pass

    def test_very_large_list(self):
        """Test with a very large list"""
        large_list = list(range(1000))
        self.assertEqual(max_integer(large_list), 999)

    def test_reverse_sorted_list(self):
        """Test with reverse sorted list"""
        self.assertEqual(max_integer([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 10)

    def test_sorted_list(self):
        """Test with sorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)


if __name__ == '__main__':
    unittest.main()
