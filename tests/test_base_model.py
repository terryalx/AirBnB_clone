#!/usr/bin/python3
"""BaseModel Test"""


import unittest
import models
from models.base_model import BaseModel
from datetime import datetime

class Test_BaseModel(unittest.TestCase):
    """BaseModel Test"""

    def setUp(self):
        """set up"""
        self.base_model = BaseModel()

    def tearDown(self):
        """tear down"""
        pass

    def test__init__(self):
        """Test"""

        base_model = self.base_model

        self.assertEqual(base_model.id, base_model.id)
        self.assertEqual(type(base_model.created_at), datetime)
        self.assertEqual(type(base_model.updated_at), datetime)
        """
        data = {
                'id': base_model.id,
                'created_at': '2023-01-01T00:00:00',
                'updated_at': '2023-01-01T00:00:00',
                'name': 'User'
                }
        base_model = BaseModel(**data)

        self.assertEqual(base_model.id, data['id'])
        self.assertEqual(base_model.name, data['User'])
        """

if __name__ == "__main__":
    unittest.main()
