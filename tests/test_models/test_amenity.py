#!/usr/bin/python3
"""Contains Amenity unittests"""
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Unittest testcases for Amenity"""

    def testUserModuleDocs(self):
        """Check if module contains docs"""
        self.assertTrue(len(amenity.__doc__) >= 1)

    def testClassContainsDocstring(self):
        """Check if class contains docs"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def testMethodContainsDocs(self):
        """Check if class methods contain docs"""
        self.assertTrue(len(Amenity.save.__doc__) >= 1)

    def testGotToDict(self):
        """Check class has method to_dict()"""
        self.assertTrue(Amenity().to_dict)

    def testGotSave(self):
        """Check class has method save()"""
        self.assertTrue(Amenity().save)

    def testGotStrMethod(self):
        """Check class has method __str__()"""
        self.assertTrue(Amenity().__str__)

    def testIsBaseModel(self):
        """Check if inherits from BaseModel"""
        self.assertTrue(issubclass(type(Amenity()), BaseModel))

    def testIsObject(self):
        """Check if inherits from object class"""
        self.assertTrue(isinstance(Amenity(), object))

    def testTypeAttributeName(self):
        """Check type of attribute name"""
        self.assertEqual(type(Amenity().name), str)

    def testHasName(self):
        """Check if has its attribute"""
        self.assertEqual(Amenity().name, "")

    def testsave4(self):
        """Test save"""
        amt = Amenity()
        amt.save()
        self.assertTrue(hasattr(amt, "updated_at"))

    def teststr(self):
        """__str__test"""
        at = Amenity()
        cN = at.__class__.__name__
        ss = f"[{cN}] ({str(at.id)}) {at.__dict__}"
        self.assertEqual(print(ss), print(at))

    def testClsInstantiation(self):
        """Using the class"""
        amt = Amenity()


if __name__ == "__main__":
    unittest.main()
