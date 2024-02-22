#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_01_auto_assign_id(self):
        """Test if Base() automatically assigns an ID"""
        base1 = Base()
        self.assertIsNotNone(base1.id, "ID should not be None")

    def test_02_auto_increment_id(self):
        """Test if Base() automatically increments ID by 1"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1, "ID should increment by 1")

    def test_03_assign_specific_id(self):
        """Test if Base(89) saves the passed ID"""
        base = Base(89)
        self.assertEqual(
            base.id, 89, "ID should be the one passed to constructor")

    def test_04_to_json_string_none(self):
        """Test if to_json_string(None) works"""
        self.assertEqual(Base.to_json_string(None), "[]", "Should return '[]'")

    def test_05_to_json_string_empty_list(self):
        """Test if to_json_string([]) works"""
        self.assertEqual(Base.to_json_string([]), "[]", "Should return '[]'")

    def test_06_to_json_string_with_dict(self):
        """Test if to_json_string([{'id': 12}]) works"""
        self.assertEqual(Base.to_json_string(
            [{'id': 12}]), '[{"id": 12}]', "Should return '[{\"id\": 12}]'")

    def test_07_to_json_string_returns_string(self):
        """Test if to_json_string([{'id': 12}]) returns a string"""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str, "Should return a string")
