#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        object_dictionary_save = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                object_dictionary_save[key] = value.to_dict()
            json.dump(object_dictionary_save, f)

    def reload(self):
        pass
