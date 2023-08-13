#!/usr/bin/python3
"""Contains Review unittests"""
from models import review
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """Unittest testcases for Review"""

    def testUserModuleDocs(self):
        """Check if module contains docs"""
        self.assertTrue(len(review.__doc__) >= 1)

    def testClassContainsDocstring(self):
        """Check if class contains docs"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def testMethodContainsDocs(self):
        """Check if class methods contain docs"""
        self.assertTrue(len(Review.to_dict.__doc__) >= 1)

    def testGotToDict(self):
        """Check class has method to_dict()"""
        self.assertTrue(Review().to_dict)

    def testGotSave(self):
        """Check class has method save()"""
        self.assertTrue(Review().save)

    def testGotStrMethod(self):
        """Check class has method __str__()"""
        self.assertTrue(Review().__str__)

    def testIsBaseModel(self):
        """Check if inherits from BaseModel"""
        self.assertTrue(issubclass(type(Review()), BaseModel))

    def testIsObject(self):
        """Check if inherits from object class"""
        self.assertTrue(isinstance(Review(), object))

    def testTypeAttributeText(self):
        """Check type of attribute text"""
        self.assertEqual(type(Review().text), str)

    def testTypeAttributeCityId(self):
        """Check type of attribute place_id"""
        self.assertEqual(type(Review().place_id), str)

    def testTypeAttributeUserId(self):
        """Check type of attribute user_id"""
        self.assertEqual(type(Review().user_id), str)

    def testHasText(self):
        """Check if has its attribute"""
        self.assertEqual(Review().text, "")

    def testHasPlaceId(self):
        """Check if has its attribute"""
        self.assertEqual(Review().place_id, "")

    def testHasUserId(self):
        """Check if has its attribute"""
        self.assertEqual(Review().user_id, "")

    def testClsInstantiation(self):
        """Using the class"""
        state1 = Review()

    def testsave4(self):
        """Test save"""
        rv = Review()
        rv.save()
        self.assertTrue(hasattr(rv, "updated_at"))

    def teststr(self):
        """__str__test"""
        rvw = Review()
        cN = rvw.__class__.__name__
        ss = f"[{cN}] ({str(rvw.id)}) {rvw.__dict__}"
        self.assertEqual(print(ss), print(rvw))

    def testattr(self):
        """Attributes test"""
        rvw = Review()
        self.assertTrue(hasattr(rvw, "created_at"))
        self.assertTrue(hasattr(rvw, "updated_at"))
        self.assertFalse(hasattr(rvw, "tone"))
        self.assertTrue(hasattr(rvw, "text"))
        self.assertTrue(hasattr(rvw, "id"))
        rvw.text = "fun"
        self.assertEqual(rvw.text, "fun")
        self.assertEqual(rvw.__class__.__name__, "Review")


if __name__ == "__main__":
    unittest.main()
