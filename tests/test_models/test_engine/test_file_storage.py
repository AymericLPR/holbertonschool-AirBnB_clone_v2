#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import pep8
import unittest
import json

""" Module for FileStorage unit tests """

class TestFileStorage(unittest.TestCase):
    """ contains all unit tests """

    def test__file_path(self):
        """ tests the presence of file.json name """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """ tests that __objects is a dictionary """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_reload(self):
        """ test that an exception is raised """
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_all(self):
        """ tests 'all' method """
        self.assertEqual(FileStorage._FileStorage__objects, storage.all())

    def test_save(self):
        """ tests the 'save' method """
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            self.assertEqual(dict, type(json.load(f)))

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
