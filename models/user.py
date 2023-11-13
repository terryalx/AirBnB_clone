#!/usr/bin/python
""" User Class """

from models.base_model import BaseModel


class User(BaseModel):
    """ User child of BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initializer """
        super().__init__(*args, **kwargs)
