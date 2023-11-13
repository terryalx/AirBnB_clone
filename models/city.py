#!/usr/bin/python3
""" city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """ city child class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializer """
        super().__init__(*args, **kwargs)
