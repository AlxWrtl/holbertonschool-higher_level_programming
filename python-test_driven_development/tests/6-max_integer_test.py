import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_with_positive_numbers(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_max_integer_with_negative_numbers(self):
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

    def test_max_integer_max_in_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_max_integer_with_no_args(self):
        self.assertEqual(max_integer(), None)

    def test_max_integer_with_integer(self):
        with self.assertRaises(TypeError):
            max_integer(12)

    def test_max_integer_with_float(self):
        with self.assertRaises(TypeError):
            max_integer(12.5)

    def test_max_integer_with_multiple_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], [4, 5, 6])

    def test_max_integer_with_bool(self):
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_max_integer_with_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
