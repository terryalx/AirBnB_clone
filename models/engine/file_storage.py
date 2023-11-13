#!/usr/bin/python3
"""File Storage"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_list = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }


class FileStorage:
    """Serialize & Deserialize"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return __dict__"""
        return self.__objects

    def new(self, obj):
        """sets __objects"""
        name = obj.__class__.__name__
        self.__objects[f"{name}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """Deserialize JSON"""
        try:
            with open(self.__file_path, 'r') as f:
                obj = json.load(f)
            for key in obj:
                class_name = None
                if "__class" in obj[key]:
                    class_name = obj[key]["__class"]
                if class_name in class_list:
                    object_data = obj[key]
                    class_instance = class_list[class_name](**object_data)
                    self.__objects[key] = class_instance
        except FileNotFoundError:
            pass
