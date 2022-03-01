#!/usr/bin/python3
"""
Module holds BaseModel class
"""
from datetime import datetime
import uuid
from xmlrpc.client import _iso8601_format
import json


class BaseModel:
    """
    class that holds the base of our Airbnb clone console
    """

    def __init__(self, *args, **kwargs):
        ''' class initializer '''
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                self.__dict__[key] = value
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time_format)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        ''' string representation of a class '''
        return ('[BaseModel] ({}) {}'.format(self.id, self.__dict__))

    def save(self):
        ''' saves an object to JSON file '''
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        ''' returns dictionary containing key value of dictionary '''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
