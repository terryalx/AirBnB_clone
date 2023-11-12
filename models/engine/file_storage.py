#!/usr/bin/python3
"""File Storage"""

import json
from models.base_model import BaseModel


class_list = {
        "BaseModel": BaseModel
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
                self.__objects[key] = class_list[obj[key]["__class"]](**obj[key])
        except:
            pass
