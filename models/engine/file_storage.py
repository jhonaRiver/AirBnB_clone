#!/usr/bin/python3
""" Module holds FileStorage class """
from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review


class FileStorage:
    """ Storage Engine

    Args:
        __file_path (str): Name of file were objects are stored
        __objects (dict): A dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Retunrs Dict objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        object_dictionary_save = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                object_dictionary_save[key] = value.to_dict()
            json.dump(object_dictionary_save, f)

    def reload(self):
        """ deserializes the JSON file to __objects, if it exists """
        try:
            with open(FileStorage.__file_path) as f:
                object_dictionary = json.load(f)
                for o in object_dictionary.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
