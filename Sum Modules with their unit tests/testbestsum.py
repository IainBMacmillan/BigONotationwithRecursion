import unittest

from bestsum import best_sum


class MyTestCase(unittest.TestCase):
    def test_no_values_TypeError(self):
        with self.assertRaises(TypeError):
            best_sum()  # expecting TypeError

    def test_wrong_input_types_AssertionError(self):
        with self.assertRaises(AssertionError):
            best_sum(1, 1)  # Assertion Error

    def test_returns_empty_list_when_target_is_zero(self):
        self.assertEqual([], best_sum(0, [1, 2]))  # expected []

    def test_returns_None_as_numbers_cant_add_to_target(self):
        self.assertEqual(None, best_sum(6, [4, 5]))  # expected None
        self.assertEqual(None, best_sum(8, [3, 7]))  # expected None
        # self.assertEqual(None, best_sum(300, [7, 14]))  # expected None

    def test_returns_matched_list_when_sum_matched(self):
        self.assertEqual([1], best_sum(1, [1, 2]))
        self.assertEqual([2, 1], best_sum(3, [1, 2]))
        self.assertEqual([4, 4], best_sum(8, [2, 3, 4]))

    def test_perf_recursion_returns_None_as_numbers_cant_add_to_target(self):
        self.assertEqual(None, best_sum(300, [7, 14]))

    def test_perf_recursion_matched_list_to_sum_target(self):
        self.assertEqual([25, 25, 25, 25], best_sum(100, [1, 2, 5, 25]))


if __name__ == '__main__':
    unittest.main()
