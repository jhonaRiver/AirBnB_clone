#!/usr/bin/python3
"""
Module holds FileStorage class
"""

from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
import os


class FileStorage:
    """ Storage Engine

    Args:
        __file_path (str): Name of file were objects are stored
        __objects (dict): A dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retunrs Dict objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        object_dictionary_save = {}

        for key, value in self.__objects.items():
            object_dictionary_save[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                object_dictionary_save[key] = value.to_dict()
            json.dump(object_dictionary_save, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, if it exists
        """
        object_dictionary_load = {}
        isFile = os.path.isfile(self.__file_path)
        if isFile:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                load = f.read()
                new_dictionary = json.loads(load)
                for key, value in new_dictionary.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
