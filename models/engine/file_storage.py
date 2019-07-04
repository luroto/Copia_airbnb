#!/usr/bin/python3
"""This module produces all about File storage """
from ..user import User
from ..base_model import BaseModel
from ..city import City
from ..amenity import Amenity
from ..state import State
from ..place import Place
from ..review import Review
import json
import os


class FileStorage:
    '''This class srtrializes instances to a JSON file and deserializes
    JSON file to instances'''

    __file_path = "file.json"
    __objects = {}
    clases = {'BaseModel': BaseModel, 'User': User, 'City': City,
              'Amenity': Amenity, 'State': State, 'Place': Place,
              'Review': Review}

    def all(self):
        """Returns the __object dictionary """
        return self.__objects

    def new(self, obj):
        """ Sets in objects the obj with a given key"""
        key = str(type(obj).__name__) + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects into json file """
        copy_dict = {}

        for key, value in self.__objects.items():
            copy_dict[key] = value.to_dict()
        if self.__objects is not None:
            with open(self.__file_path, 'w') as opening:
                json.dump(copy_dict, opening)

    def reload(self):
        """Deserializes JSON files to __objects """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as reading:
                temp = json.load(reading)
                for key, value in temp.items():
                    key = str(value["__class__"]) + "." + str(value["id"])
                    data = self.clases[value["__class__"]](**value)
                    self.__objects[key] = data
