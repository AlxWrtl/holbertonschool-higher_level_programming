#!/usr/bin/python3
import unittest
import json
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    # Constructor tests
    def test_01_constructor_basic(self):
        """Test Rectangle with basic width and height"""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height), (1, 2))

    def test_02_constructor_with_x(self):
        """Test Rectangle with width, height, and x"""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.x), 3)

    def test_03_constructor_with_x_y(self):
        """Test Rectangle with width, height, x, and y"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.y), 4)

    def test_04_constructor_with_all_params(self):
        """Test Rectangle with all parameters"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    # Constructor error handling for string inputs
    def test_05_to_12_constructor_string_errors(self):
        """Test Rectangle constructor with string inputs for numeric parameters"""
        with self.assertRaises(ValueError):
            Rectangle("1", 2)
            Rectangle(1, "2")
            Rectangle(1, 2, "3")
            Rectangle(1, 2, 3, "4")

    # Constructor error handling for negative and zero values
    def test_13_to_18_constructor_negative_zero(self):
        """Test Rectangle constructor with negative and zero values for width and height"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
            Rectangle(1, -2)
            Rectangle(0, 2)
            Rectangle(1, 0)
            Rectangle(1, 2, -3)
            Rectangle(1, 2, 3, -4)

    # Method functionality tests
    def test_19_area(self):
        """Test area() method"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_20_str(self):
        """Test __str__ method"""
        r = Rectangle(1, 2, 3, 4)
        expected_str = "[Rectangle] ({}) {}/{} - {}/{}".format(r.id,
                        r.x, r.y, r.width, r.height)
        self.assertEqual(str(r), expected_str)

    def test_21_to_dictionary(self):
        """Test to_dictionary() method"""
        r = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r.to_dictionary(), dict)

    # Update method tests
    def test_22_to_31_update(self):
        """Test update() method with various arguments"""
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))
        r.update(89, 1, 2)
        self.assertEqual((r.width, r.height), (1, 2))
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

        # Keyword argument updates
        r.update(id=90)
        self.assertEqual(r.id, 90)
        r.update(width=2)
        self.assertEqual(r.width, 2)
        r.update(height=3)
        self.assertEqual(r.height, 3)
        r.update(x=4)
        self.assertEqual(r.x, 4)
        r.update(y=5)
        self.assertEqual(r.y, 5)

    # Create method test
    def test_32_to_36_create(self):
        """Test create() method with various arguments"""
        r = Rectangle.create(id=89)
        self.assertEqual(r.id, 89)
        r = Rectangle.create(id=89, width=1)
        self.assertEqual((r.id, r.width), (89, 1))
        r = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual((r.width, r.height), (1, 2))
        r = Rectangle.create(id=89, width=1, height=2, x=3)
        self.assertEqual(r.x, 3)
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.y, 4)


if __name__ == "__main__":
    unittest.main()
