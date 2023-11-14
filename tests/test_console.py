#!/usr/bin/python3
'''Test Console Module'''

from console import HBNBCommand
from unittest.mock import create_autospec
from uuid import UUID
import models
import unittest
import json
import sys
from os import remove
from models.base_model import BaseModel
from io import StringIO


class TestConsole(unittest.TestCase):
    '''Test Console Basic'''

    def setUp(self):
        '''Set up method'''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.out = StringIO()
        sys.stdout = self.out
        self.console = self.create()

    def tearDown(self):
        '''Tear down method'''
        sys.stdout = sys.__stdout__
        try:
            remove('file.json')
        except FileNotFoundError:
            pass
        models.storage._FileStorage__objects.clear()
        self.clearIO()

    def clearIO(self):
        '''Clear IO buffer'''
        self.out.truncate(0)
        self.out.seek(0)

    def create(self):
        """Create console instance"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)


if __name__ == '__main__':
    unittest.main()
