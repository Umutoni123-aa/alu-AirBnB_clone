#!/usr/bin/python3
"""Test BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases"""
    
    def test_create(self):
        """Test instance creation"""
        m = BaseModel()
        self.assertIsNotNone(m.id)
        self.assertIsNotNone(m.created_at)
    
    def test_to_dict(self):
        """Test to_dict"""
        m = BaseModel()
        d = m.to_dict()
        self.assertEqual(d['__class__'], 'BaseModel')
    
    def test_str(self):
        """Test __str__"""
        m = BaseModel()
        s = str(m)
        self.assertIn('BaseModel', s)


if __name__ == '__main__':
    unittest.main()
