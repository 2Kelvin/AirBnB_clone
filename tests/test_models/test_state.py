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

    def testsave4(self):
        """Test save"""
        state = State()
        state.save()
        self.assertTrue(hasattr(state, "updated_at"))

    def testGotToDict(self):
        """Check class has method to_dict()"""
        self.assertTrue(State().to_dict)

    def testGotSave(self):
        """Check class has method save()"""
        self.assertTrue(State().save)

    def testGotStrMethod(self):
        """Check class has method __str__()"""
        self.assertTrue(State().__str__)

    def teststr(self):
        """__str__test"""
        state = State()
        cN = state.__class__.__name__
        ss = f"[{cN}] ({str(state.id)}) {state.__dict__}"
        self.assertEqual(print(ss), print(state))

    def testIsBaseModel(self):
        """Check if inherits from BaseModel"""
        self.assertTrue(issubclass(type(State()), BaseModel))

    def testIsObject(self):
        """Check if inherits from object class"""
        self.assertTrue(isinstance(State(), object))

    def testTypeAttributeName(self):
        """Check type of attribute name"""
        self.assertEqual(type(State().name), str)

    def testHasName(self):
        """Check if has its attribute"""
        self.assertEqual(State().name, "")

    def testClsInstantiation(self):
        """Using the class"""
        state1 = State()

    def testattr(self):
        """Attributes test"""
        state = State()
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertFalse(hasattr(state, "tone"))
        self.assertTrue(hasattr(state, "name"))
        self.assertTrue(hasattr(state, "id"))
        self.assertEqual(state.name, "")
        state.name = "Kiambu"
        self.assertEqual(state.name, "Kiambu")
        self.assertEqual(state.__class__.__name__, "State")


if __name__ == "__main__":
    unittest.main()
