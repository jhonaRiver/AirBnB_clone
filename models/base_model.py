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

    def __init__(self):
        ''' class initializer '''
        self.id = str(uuid.uuid4())
        self.created_at = _iso8601_format(datetime.now())
        self.updated_at = _iso8601_format(datetime.now())

    def __str__(self):
        ''' string representation of a class '''
        return ('[BaseModel] ({}) {}'.format(self.id, self.__dict__))

    def save(self):
        ''' saves an object to JSON file '''
        self.updated_at = _iso8601_format(datetime.now())

    def to_dict(self):
        ''' returns dictionary containing key value of dictionary '''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
