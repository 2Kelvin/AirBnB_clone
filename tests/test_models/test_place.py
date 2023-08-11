#!/usr/bin/python3
"""Contains Place unittests"""
from models import place
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Unittest testcases for Place"""

    def testUserModuleDocs(self):
        """Check if module contains docs"""
        self.assertTrue(len(place.__doc__) >= 1)

    def testClassContainsDocstring(self):
        """Check if class contains docs"""
        self.assertTrue(len(Place.__doc__) >= 1)

    def testMethodContainsDocs(self):
        """Check if class methods contain docs"""
        self.assertTrue(len(Place.to_dict.__doc__) >= 1)

    def testGotToDict(self):
        """Check class has method to_dict()"""
        self.assertTrue(Place().to_dict)

    def testGotSave(self):
        """Check class has method save()"""
        self.assertTrue(Place().save)

    def testGotStrMethod(self):
        """Check class has method __str__()"""
        self.assertTrue(Place().__str__)

    def testIsBaseModel(self):
        """Check if inherits from BaseModel"""
        self.assertTrue(issubclass(type(Place()), BaseModel))

    def testIsObject(self):
        """Check if inherits from object class"""
        self.assertTrue(isinstance(Place(), object))

    def testTypeAttributeName(self):
        """Check type of attribute name"""
        self.assertEqual(type(Place().name), str)

    def testTypeAttributeDescription(self):
        """Check type of attribute description"""
        self.assertEqual(type(Place().description), str)

    def testTypeAttributeNumberOfRooms(self):
        """Check type of attribute number_rooms"""
        self.assertEqual(type(Place().number_rooms), int)

    def testTypeAttributeNumberOfBathrooms(self):
        """Check type of attribute number_bathrooms"""
        self.assertEqual(type(Place().number_bathrooms), int)

    def testTypeAttributeMaxGuest(self):
        """Check type of attribute max_guest"""
        self.assertEqual(type(Place().max_guest), int)

    def testTypeAttributePriceByNight(self):
        """Check type of attribute price_by_night"""
        self.assertEqual(type(Place().price_by_night), int)

    def testTypeAttributeCityId(self):
        """Check type of attribute city_id"""
        self.assertEqual(type(Place().city_id), str)

    def testTypeAttributeUserId(self):
        """Check type of attribute user_id"""
        self.assertEqual(type(Place().user_id), str)

    def testTypeAttributeLatitude(self):
        """Check type of attribute latitude"""
        self.assertEqual(type(Place().latitude), float)

    def testTypeAttributeLongitude(self):
        """Check type of attribute longitude"""
        self.assertEqual(type(Place().longitude), float)

    def testTypeAttributeAmenityIds(self):
        """Check type of attribute amenity_ids"""
        self.assertEqual(type(Place().amenity_ids), list)


if __name__ == "__main__":
    unittest.main()