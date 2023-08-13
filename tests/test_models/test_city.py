#!/usr/bin/python3
"""Contains City unittests"""
from models import city
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Unittest testcases for City"""

    def testUserModuleDocs(self):
        """Check if module contains docs"""
        self.assertTrue(len(city.__doc__) >= 1)

    def testClassContainsDocstring(self):
        """Check if class contains docs"""
        self.assertTrue(len(City.__doc__) >= 1)

    def testMethodContainsDocs(self):
        """Check if class methods contain docs"""
        self.assertTrue(len(City.to_dict.__doc__) >= 1)

    def testGotToDict(self):
        """Check class has method to_dict()"""
        self.assertTrue(City().to_dict)

    def testGotSave(self):
        """Check class has method save()"""
        self.assertTrue(City().save)

    def testGotStrMethod(self):
        """Check class has method __str__()"""
        self.assertTrue(City().__str__)

    def testIsBaseModel(self):
        """Check if inherits from BaseModel"""
        self.assertTrue(issubclass(type(City()), BaseModel))

    def testIsObject(self):
        """Check if inherits from object class"""
        self.assertTrue(isinstance(City(), object))

    def testTypeAttributeName(self):
        """Check type of attribute name"""
        self.assertEqual(type(City().name), str)

    def testTypeAttributeStateId(self):
        """Check type of attribute state_id"""
        self.assertEqual(type(City().name), str)

    def testHasStateId(self):
        """Check if has its attribute"""
        self.assertEqual(City().state_id, "")

    def testHasName(self):
        """Check if has its attribute"""
        self.assertEqual(City().name, "")


if __name__ == "__main__":
    unittest.main()
