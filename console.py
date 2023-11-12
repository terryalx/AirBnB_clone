#!/usr/bin/python3

"""HBnB python console"""

import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """HBnB console"""
    promt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(elsf, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
