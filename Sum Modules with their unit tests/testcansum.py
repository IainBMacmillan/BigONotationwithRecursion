import unittest

from cansum import can_sum


class TestCanSum(unittest.TestCase):
    # can_sum checks if any combination of numbers in a list can be used
    # as often as required to match the target_number

    def test_no_values_TypeError(self):
        with self.assertRaises(TypeError):
            can_sum()  # expecting TypeError

    def test_wrong_input_types_AssertionError(self):
        with self.assertRaises(AssertionError):
            can_sum(1, 1)  # Assertion Error

    def test_returns_sum_equals_zero(self):
        self.assertTrue(can_sum(6, [2, 4]))  # expecting 'True'

    def test_returns_sum_not_equals_zero(self):
        self.assertFalse(can_sum(7, [2, 4]))  # expecting 'False'

    def test_returns_recursive_matched_true(self):
        self.assertTrue(can_sum(8, [2, 3, 5]))  # expecting 'True'

    def test_memoization_with_large_recursion_false(self):
        self.assertFalse(can_sum(300, [7, 14]))  # expecting 'False'


if __name__ == '__main__':
    unittest.main()
