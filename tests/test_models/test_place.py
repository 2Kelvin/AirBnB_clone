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

    def testHasName(self):
        """Check if has its attribute"""
        self.assertEqual(Place().name, "")

    def testHasCityId(self):
        """Check if has its attribute"""
        self.assertEqual(Place().city_id, "")

    def testHasUserId(self):
        """Check if has its attribute"""
        self.assertEqual(Place().user_id, "")

    def testHasDescription(self):
        """Check if has its attribute"""
        self.assertEqual(Place().description, "")

    def testHasNumberRooms(self):
        """Check if has its attribute"""
        self.assertEqual(Place().number_rooms, 0)

    def testHasNumberBathrooms(self):
        """Check if has its attribute"""
        self.assertEqual(Place().number_bathrooms, 0)

    def testHasMaxGuest(self):
        """Check if has its attribute"""
        self.assertEqual(Place().max_guest, 0)

    def testHasPriceByNight(self):
        """Check if has its attribute"""
        self.assertEqual(Place().price_by_night, 0)

    def testHasLatitude(self):
        """Check if has its attribute"""
        self.assertEqual(Place().latitude, 0.0)

    def testHasLongitude(self):
        """Check if has its attribute"""
        self.assertEqual(Place().longitude, 0.0)

    def testHasAmenityIds(self):
        """Check if has its attribute"""
        self.assertEqual(Place().amenity_ids, [])

    def teststr(self):
        """__str__test"""
        plc = Place()
        cN = plc.__class__.__name__
        ss = f"[{cN}] ({str(plc.id)}) {plc.__dict__}"
        self.assertEqual(print(ss), print(plc))

    def testsave4(self):
        """Test save"""
        p = Place()
        p.save()
        self.assertTrue(hasattr(p, "updated_at"))

    def teststr(self):
        """__str__test"""
        pl = Place()
        cN = pl.__class__.__name__
        ss = f"[{cN}] ({str(pl.id)}) {pl.__dict__}"
        self.assertEqual(print(ss), print(pl))

    def testattr(self):
        """Class Attributes"""
        place = Place()
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertFalse(hasattr(place, "man"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "id"))
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def testClsInstantiation(self):
        """Using the class"""
        pl = Place()


if __name__ == "__main__":
    unittest.main()
