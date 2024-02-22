#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_01_auto_assign_id(self):
        """Test if Base() automatically assigns an ID"""
        base1 = Base()
        self.assertIsNotNone(base1.id, "ID should not be None")


if __name__ == '__main__':
    unittest.main()
