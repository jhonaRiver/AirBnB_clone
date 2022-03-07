#!/usr/bin/python3
""" Module to test BaseModel class """

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Method to test init of said class """
        cls.base_1 = BaseModel("My_First_Model")
        cls.base_2 = BaseModel(89)

    def test_name(self):
        """ Method to test name """
        self.assertEqual(self.base_1.name, "My_First_Model")

    def test_my_number(self):
        """ Method to test my_number """
        self.assertEqual(self.base_2.my_number, 89)
