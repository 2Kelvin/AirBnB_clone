#!/usr/bin/python3
"""Contains State unittests"""
from models import state
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """Unittest testcases for State"""

    def testUserModuleDocs(self):
        """Check if module contains docs"""
        self.assertTrue(len(state.__doc__) >= 1)

    def testClassContainsDocstring(self):
        """Check if class contains docs"""
        self.assertTrue(len(State.__doc__) >= 1)

    def testMethodContainsDocs(self):
        """Check if class methods contain docs"""
        self.assertTrue(len(State.to_dict.__doc__) >= 1)

    def testGotToDict(self):
        """Check class has method to_dict()"""
        self.assertTrue(State().to_dict)

    def testGotSave(self):
        """Check class has method save()"""
        self.assertTrue(State().save)

    def testGotStrMethod(self):
        """Check class has method __str__()"""
        self.assertTrue(State().__str__)

    def testIsBaseModel(self):
        """Check if inherits from BaseModel"""
        self.assertTrue(issubclass(type(State()), BaseModel))

    def testIsObject(self):
        """Check if inherits from object class"""
        self.assertTrue(isinstance(State(), object))

    def testTypeAttributeName(self):
        """Check type of attribute name"""
        self.assertEqual(type(State().name), str)


if __name__ == "__main__":
    unittest.main()
