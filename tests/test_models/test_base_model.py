#!/usr/bin/python3
import unittest
import datetime
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_str(self):
        model = BaseModel()
        model_dict = model.__dict__.copy()
        model_dict.pop('created_at', None)
        model_dict.pop('updated_at', None)
        expected_str = "[BaseModel] ({}) {}".format(model.id, model_dict)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        with patch('models.base_model.datetime') as mock_date:
            model.save()
            self.assertNotEqual(original_updated_at, model.updated_at)
            self.assertEqual(mock_date.now.call_count, 1)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertDictEqual(model_dict, {'id': model.id,
                                          'created_at': model.created_at.isoformat(),
                                          'updated_at': model.updated_at.isoformat(),
                                          '__class__': 'BaseModel'})
