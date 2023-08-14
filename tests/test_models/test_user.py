#!/usr/bin/python3
"""Contains User unittests"""
from models import user
from models.user import User
from models.base_model import BaseModel
import unittest
import os
from time import sleep
from models.engine.file_storage import FileStorage
from datetime import datetime


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

    def testTypes(self):
        """Check attribute types"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.email = "airbnb@holbertonshool.com"
        my_user.password = "root"

        self.assertEqual(type(my_user.email), str)
        self.assertEqual(type(my_user.password), str)
        self.assertEqual(type(my_user.first_name), str)
        self.assertEqual(type(my_user.first_name), str)

    def testSave2(self):
        """Test save method"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.email = "airbnb@holbertonshool.com"
        my_user.password = "root"

        my_user.save()
        self.assertNotEqual(my_user.created_at, my_user.updated_at)

    def testDict(self):
        """Test to_dict"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.email = "airbnb@holbertonshool.com"
        my_user.password = "root"
        self.assertEqual('to_dict' in dir(my_user), True)

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

    def testClsInstantiation(self):
        """Using the class"""
        user1 = User()
        user1.first_name = "Betty"
        user1.last_name = "Holberton"
        user1.email = "airbnb@holbertonshool.com"
        user1.password = "root"

    def testDatetime2(self):
        """Tests datetime"""
        usr = User()
        uDict = usr.to_dict()
        self.assertTrue(type(uDict["id"]) == str)
        self.assertTrue(type(uDict["created_at"]) == str)
        self.assertTrue(type(uDict["updated_at"]) == str)

    def testClassAttributes2(self):
        """check class attributes"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.email = "airbnb@holbertonshool.com"
        my_user.password = "root"

        self.assertTrue('email' in my_user.__dict__)
        self.assertTrue('id' in my_user.__dict__)
        self.assertTrue('created_at' in my_user.__dict__)
        self.assertTrue('updated_at' in my_user.__dict__)
        self.assertTrue('password' in my_user.__dict__)
        self.assertTrue('first_name' in my_user.__dict__)
        self.assertTrue('last_name' in my_user.__dict__)

    def testErrorDict(self):
        """Tests error dict"""
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def testOut(self):
        """Test dict output"""
        tdy = datetime.today()
        myUser = User()
        myUser.id = "123456"
        myUser.created_at = myUser.updated_at = tdy
        outDict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': tdy.isoformat(),
            'updated_at': tdy.isoformat(),
        }
        self.assertDictEqual(myUser.to_dict(), outDict)

    def renameFile(self):
        """IO tests"""
        try:
            os.rename("file.json", "changed")
        except IOError:
            pass

    def testIO(self):
        """IO tests 2"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("changed", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def testFileSave(self):
        """Tests file save"""
        aUser = User()
        aUser.save()
        usid = f"User.{aUser.id}"
        with open("file.json", "r") as readF:
            self.assertIn(usid, readF.read())

    def testsaveUser(self):
        """Test save()"""
        usr = User()
        sleep(0.10)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)

    def testErrorSave(self):
        """Test error save"""
        my_user = User()
        with self.assertRaises(TypeError):
            my_user.save(None)

    def testHasAtts(self):
        """Check attributes"""
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def testTypeDict(self):
        """Tests dict type"""
        self.assertTrue(type(User().to_dict()) == dict)

    def testAddedAtts(self):
        """Test attributes added after"""
        myUser = User()
        myUser.school = "Holberton"
        myUser.my_number = 98
        self.assertEqual("Holberton", myUser.school)
        self.assertIn("my_number", myUser.to_dict())

    def testErrorDict(self):
        """Test error dictionary"""
        my_user = User()
        with self.assertRaises(TypeError):
            my_user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
