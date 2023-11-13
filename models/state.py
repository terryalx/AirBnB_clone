#!/usr/bin/python3
""" State class """

from models.base_model import BaseModel


class State(BaseModel):
    """ state child class """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializer"""
        super().__init__(*args, **kwargs)
