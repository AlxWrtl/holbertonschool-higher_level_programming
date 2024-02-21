#!/usr/bin/python3
import unittest
import json
from models.square import Square


class TestSquare(unittest.TestCase):


    def test_01_constructor_basic(self):
        """Test Square with basic size"""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_02_constructor_with_x(self):
        """Test Square with size and x"""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_03_constructor_with_x_y(self):
        """Test Square with size, x, and y"""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_04_constructor_invalid_string(self):
        """Test Square with string inputs for numeric parameters"""
        with self.assertRaises(ValueError):
            Square("1")
            Square(1, "2")
            Square(1, 2, "3")

    def test_05_constructor_extra_param(self):
        """Test Square with more parameters than expected"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4)

    def test_06_constructor_negative_zero(self):
        """Test Square with negative and zero values for size"""
        with self.assertRaises(ValueError):
            Square(-1)
            Square(1, -2)
            Square(1, 2, -3)
            Square(0)

    def test_07_str_method(self):
        """Test __str__ method for Square"""
        s = Square(1, 2, 3)
        expected_str = "[Square] ({}) {}/{} - {}".format(s.id,
                        s.x, s.y, s.size)
        self.assertEqual(str(s), expected_str)

    def test_08_to_dictionary(self):
        """Test to_dictionary() method"""
        s = Square(1, 2, 3)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_09_to_18_update_methods(self):
        """Test update() method with various arguments"""
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)
        s.update(id=90)
        self.assertEqual(s.id, 90)
        s.update(size=2)
        self.assertEqual(s.size, 2)
        s.update(x=3)
        self.assertEqual(s.x, 3)
        s.update(y=4)
        self.assertEqual(s.y, 4)

    def test_19_to_22_create_methods(self):
        """Test create() method with various arguments"""
        s = Square.create(id=89)
        self.assertEqual(s.id, 89)
        s = Square.create(id=89, size=1)
        self.assertEqual(s.size, 1)
        s = Square.create(id=89, size=1, x=2)
        self.assertEqual(s.x, 2)
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.y, 3)

    def test_23_to_26_file_operations(self):
        """Test save_to_file and load_from_file methods"""
        Square.save_to_file(None)
        Square.save_to_file([])
        Square.save_to_file([Square(1)])
        result = Square.load_from_file()
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
