#!/usr/bin/python3
"""This module checks all about BaseModel """
from models.base_model import BaseModel
import unittest
import os
from datetime import datetime
import pep8


class testBaseModel(unittest.TestCase):
    ''' Test of the model BaseModel '''

    @classmethod
    def setUpClass(cls):
        ''' test_inst up '''
        cls.test_inst = BaseModel()
        cls.test_inst.name = "Holberton"
        cls.test_inst.id = 89
        cls.test_inst.save()
        cls.test_inst_str = cls.test_inst.to_dict()

    def test_isInstance(self):
        ''' test if is a instance of BaseModel '''
        self.assertIsNot(self.test_inst, BaseModel)
        self.assertTrue(isinstance(self.test_inst, BaseModel))

    def test_attrib(self):
        ''' test the attributes created '''
        self.assertEqual(self.test_inst_str['name'], 'Holberton')
        self.assertEqual(self.test_inst_str['id'], 89)

    def test_typeAttrib(self):
        ''' test the type of the attributes in the dict '''
        self.assertEqual(type(self.test_inst_str['created_at']), str)
        self.assertEqual(type(self.test_inst_str['updated_at']), str)
        self.assertEqual(type(self.test_inst_str['name']), str)
        self.assertEqual(type(self.test_inst_str['id']), int)
        self.assertTrue(type(self.test_inst.id), str)

    def test_saveMethod(self):
        ''' test the method save works '''
        temp = self.test_inst.updated_at
        self.test_inst.save()
        self.assertNotEqual(temp, self.test_inst.updated_at)

    def test_isDictionary(self):
        ''' test if to_dict run well '''
        self.assertEqual(type(self.test_inst_str), dict)

    def test_typeAttribDateTime(self):
        ''' test if created_at and updated_at attributes are datetime '''
        self.assertEqual(type(self.test_inst.updated_at), datetime)
        self.assertEqual(type(self.test_inst.created_at), datetime)

    def test_hasMethods(self):
        ''' test the instance have the methods  '''
        self.assertTrue(hasattr(self.test_inst, '__str__'))
        self.assertTrue(hasattr(self.test_inst, '__init__'))
        self.assertTrue(hasattr(self.test_inst, 'to_dict'))
        self.assertTrue(hasattr(self.test_inst, 'save'))

    def test_hasDocumentation(self):
        ''' test the methods have documentation '''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(self.test_inst.__init__.__doc__)
        self.assertIsNotNone(self.test_inst.__str__.__doc__)
        self.assertIsNotNone(self.test_inst.save.__doc__)
        self.assertIsNotNone(self.test_inst.to_dict.__doc__)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
                                        'models/base_model.py',
                                        'tests/test_models/test_base_model.py'
                                        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def tearDownClass(cls):
        ''' test_inst Down '''
        del cls.test_inst
        try:
            os.remove("file.json")
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
