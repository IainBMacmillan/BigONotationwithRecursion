import unittest

from howsum import how_sum


class MyTestCase(unittest.TestCase):
    def test_no_values_TypeError(self):
        with self.assertRaises(TypeError):
            how_sum()  # expecting TypeError

    def test_wrong_input_types_AssertionError(self):
        with self.assertRaises(AssertionError):
            how_sum(1, 1)  # Assertion Error

    def test_returns_empty_list_when_target_is_zero(self):
        self.assertEqual([], how_sum(0, [1, 2]))

    def test_returns_matched_list_when_sum_matched(self):
        self.assertEqual([1], how_sum(1, [1, 2]))
        self.assertEqual([1, 1, 1], how_sum(3, [1, 2]))
        self.assertEqual([4, 3], how_sum(7, [3, 4]))

    def test_returns_None_as_numbers_cant_add_to_target(self):
        self.assertEqual(None, how_sum(6, [4, 5]))  # expected None
        self.assertEqual(None, how_sum(8, [3, 7]))  # expected None
        self.assertEqual(None, how_sum(300, [7, 14]))  # expected None

    # def test_returns_None_as_numbers_cant_add_to_target(self):
    #     self.assertEqual(None, how_sum(6, [2, 5]))  # expected None


if __name__ == '__main__':
    unittest.main()
