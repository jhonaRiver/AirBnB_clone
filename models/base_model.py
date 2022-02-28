#!/usr/bin/python3
"""
...
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    ...
    """

    def __init__(self):
        ''''''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''''''
        return ('[BaseModel] ({}) {}'.format(self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__
