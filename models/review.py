#!/usr/bin/python3
""" Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review child class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initializer """
        super().__init__(*args, **kwargs)
