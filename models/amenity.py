#!/usr/bin/python3
""" Amenity class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity child class """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializer """
        super().__init__(*args, **kwargs)
