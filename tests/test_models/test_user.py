#!/usr/bin/python3
"""Contains User unittests"""
from models import user
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Unittest testcases for User"""

    def testUserModuleDocs(self):
        """Check if module contains docs"""
        self.assertTrue(len(user.__doc__) >= 1)

    def testClassContainsDocstring(self):
        """Check if class contains docs"""
        self.assertTrue(len(User.__doc__) >= 1)

    def testMethodContainsDocs(self):
        """Check if class methods contain docs"""
        self.assertTrue(len(User.to_dict.__doc__) >= 1)

    def testGotToDict(self):
        """Check class has method to_dict()"""
        self.assertTrue(User().to_dict)

    def testGotSave(self):
        """Check class has method save()"""
        self.assertTrue(User().save)

    def testGotStrMethod(self):
        """Check class has method __str__()"""
        self.assertTrue(User().__str__)

    def testIsBaseModel(self):
        """Check if inherits from BaseModel"""
        self.assertTrue(issubclass(type(User()), BaseModel))

    def testIsObject(self):
        """Check if inherits from object class"""
        self.assertTrue(isinstance(User(), object))

    def testTypeAttributeEmail(self):
        """Check type of attribute email"""
        self.assertEqual(type(User().email), str)

    def testTypeAttributePassword(self):
        """Check type of attribute password"""
        self.assertEqual(type(User().password), str)

    def testTypeAttributeFirst_name(self):
        """Check type of attribute first_name"""
        self.assertEqual(type(User().first_name), str)

    def testTypeAttributeLast_name(self):
        """Check type of attribute last_name"""
        self.assertEqual(type(User().last_name), str)

    def testValueLastName(self):
        """Check value passed in"""
        user1 = User()
        user1.first_name = 22
        self.assertEqual(type(user1.first_name), int)

    def testHasEmail(self):
        """Check if has its attribute"""
        self.assertEqual(User().email, "")

    def testHasPassword(self):
        """Check if has its attribute"""
        self.assertEqual(User().password, "")

    def testHasFirstName(self):
        """Check if has its attribute"""
        self.assertEqual(User().first_name, "")

    def testHasLastName(self):
        """Check if has its attribute"""
        self.assertEqual(User().last_name, "")


if __name__ == "__main__":
    unittest.main()
