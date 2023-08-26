#!/usr/bin/python3
""" Test cases for the user model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest


class test_User(test_basemodel):
    """test user cases """

    def __init__(self, *args, **kwargs):
        """init instances tests """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test first name """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test last name """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test email """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.password), str)


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
