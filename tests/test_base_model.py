#!/usr/bin/python3
"""BaseModel Test"""


import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from unittest import mock
import pep8 as pycodestyle
import time
import inspect
from io import StringIO
from os import remove
from os.path import isfile
import pycodestyle
import sys
import io
from console import HBNBCommand
from unittest.mock import create_autospec
from uuid import UUID
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


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

        data = {
                'id': '2468',
                'created_at': '2023-01-01T00:00:00',
                'updated_at': '2023-01-01T00:00:00',
                'name': 'User'
                }

        base_model = BaseModel(**data)

        self.assertEqual(base_model.id, '2468')
        self.assertEqual(base_model.name, 'User')

    def test_init_args(self):
        """Test args"""
        name = BaseModel(None)
        self.assertNotIn(None, name.__dict__.values())


class TestBaseModel(unittest.TestCase):
    """BaseModel class test 2"""

    @mock.patch('models.storage')
    def test_instantiation(self, mock_storage):
        """Test that object is correctly created"""
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "Holberton"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(inst.name, "Holberton")
        self.assertEqual(inst.number, 89)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at
        value."""
        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))


if __name__ == "__main__":
    unittest.main()
