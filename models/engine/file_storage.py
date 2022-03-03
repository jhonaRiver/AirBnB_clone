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
        try:
            with open(FileStorage.__file_path) as f:
                object_dictionary = json.load(f)
                for o in object_dictionary.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
