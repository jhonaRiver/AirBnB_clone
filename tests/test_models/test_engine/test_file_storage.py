#!/usr/bin/python3
"""
Unittest module for FileStorage Class
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorageClass(unittest.TestCase):
    """ 
    Test FileStorage Class
    """

    __file_path = None


if __name__ == "__main__":
    unittest.main()
