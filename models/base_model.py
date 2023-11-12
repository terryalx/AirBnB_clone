#!/usr/bin/python3
"BaseModel"


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """super class"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Format"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, 
                                        self.__dict__)

    def save(self):
        """set time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
