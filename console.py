#!/usr/bin/python3
"""HBnB python console"""

import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBnB console"""
    promt = "(hbnb) "
    class_list = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(elsf, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, cls_name=None):
        """Creates a new instance of BaseModel"""
        if not cls_name:
            print('** class name missing **')
        elif not self.class_list.get(cls_name):
            print('** class doesn\'t exist **')
        else:
            obj = self.class_list[cls_name]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints string representation"""
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.class_list.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.class_list.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all """
        storage.reload()
        objects_dict = storage.all()
        my_json = []
        if not arg:
            for obj in objects_dict.values():
                my_json.append(str(obj))
            print(json.dumps(my_json))
            return
        token = shlex.split(arg)
        if token[0] in HBNBCommand.class_list.keys():
            for key, obj in objects_dict.items():
                if token[0] in key:
                    my_json.append(str(obj))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance"""
        clsname, objid, attrname, attrval = None, None, None, None
        updatetime = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if len(args) > 2:
            attrname = args[2]
        if len(args) > 3:
            attrval = list(shlex(args[3]))[0].strip('"')
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not attrname:
            print('** attribute name missing **')
        elif not attrval:
            print('** value missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                if hasattr(obj, attrname):
                    attrval = type(getattr(obj, attrname))(attrval)
                else:
                    attrval = self.getType(attrval)(attrval)
                setattr(obj, attrname, attrval)
                obj.updated_at = updatetime
                models.storage.save()

    def do_count(self, arg):
        """ Print  number of instances """
        counter = 0
        objects_dict = storage.all()
        for key, value in objects_dict.items():
            if (arg in key):
                counter += 1
        print(counter)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
