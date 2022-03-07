#!/usr/bin/python3
""" Module holds class that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ class that represents a User
    Args:
        email (str): User email
        password (str): User Password
        first_name (str): User name
        last_name (str): User last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
