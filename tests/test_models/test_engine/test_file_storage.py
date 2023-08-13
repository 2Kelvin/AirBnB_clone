#!/usr/bin/python3
"""Module contains unittest testcases for FileStorage"""
import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import models
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Unittest testcases for FileStorage"""

    def testModuleContainsDocstring(self):
        """Check if module contains docs"""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def testClassContainsDocstring(self):
        """Check if class FileStorage contains docs"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def testMethodContainsDocs(self):
        """Check if FileStorage method contains docs"""
        self.assertTrue(len(FileStorage.new.__doc__) >= 1)

    def testFilePathisPrivate(self):
        """Check if __file_path attribute is private"""
        with self.assertRaises(AttributeError):
            newStorage = FileStorage()
            newStorage.__file_path

    def testObjectsisPrivate(self):
        """Check if __objects attribute is private"""
        with self.assertRaises(AttributeError):
            newStorage = FileStorage()
            newStorage.__objects

    def testFileStorageGotNew(self):
        """Check class has method new"""
        self.assertTrue(FileStorage().new)

    def testFileStorageGotSave(self):
        """Check class has method save"""
        self.assertTrue(FileStorage().save)

    def testFileStorageGotAll(self):
        """Check class has method all"""
        self.assertTrue(FileStorage().all)

    def testFileStorageGotReload(self):
        """Check class has method reload"""
        self.assertTrue(FileStorage().reload)

    def testPrivateAttributesinClass(self):
        """Check private attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def testInstantiation(self):
        """Check instantiation"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def testInstantiationArg(self):
        """Check instantiation with arg"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testTypeFilePath(self):
        """Check attribute type"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def testTypeObjects(self):
        """Check attribute type"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def testModelsStorage(self):
        """Check models.storage"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        """Check all()"""
        self.assertEqual(type(models.storage.all()), dict)

    def testMethodNew(self):
        """Test method new"""
        base = BaseModel()
        user1 = User()
        state1 = State()
        place1 = Place()
        city1 = City()
        amty1 = Amenity()
        rvw1 = Review()
        models.storage.new(base)
        models.storage.new(user1)
        models.storage.new(state1)
        models.storage.new(place1)
        models.storage.new(city1)
        models.storage.new(amty1)
        models.storage.new(rvw1)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())
        self.assertIn("User." + user1.id, models.storage.all().keys())
        self.assertIn(user1, models.storage.all().values())
        self.assertIn("State." + state1.id, models.storage.all().keys())
        self.assertIn(state1, models.storage.all().values())
        self.assertIn("Place." + place1.id, models.storage.all().keys())
        self.assertIn(place1, models.storage.all().values())
        self.assertIn("City." + city1.id, models.storage.all().keys())
        self.assertIn(city1, models.storage.all().values())
        self.assertIn("Amenity." + amty1.id, models.storage.all().keys())
        self.assertIn(amty1, models.storage.all().values())
        self.assertIn("Review." + rvw1.id, models.storage.all().keys())
        self.assertIn(rvw1, models.storage.all().values())

    def testMethodSave(self):
        """Test method save"""
        mod = BaseModel()
        usr = User()
        stt = State()
        plc = Place()
        cty = City()
        amty = Amenity()
        rvw = Review()
        models.storage.new(mod)
        models.storage.new(usr)
        models.storage.new(stt)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amty)
        models.storage.new(rvw)
        models.storage.save()
        dataSaved = ""
        with open("file.json", "r") as rfile:
            dataSaved = rfile.read()
            self.assertIn("BaseModel." + mod.id, dataSaved)
            self.assertIn("User." + usr.id, dataSaved)
            self.assertIn("State." + stt.id, dataSaved)
            self.assertIn("Place." + plc.id, dataSaved)
            self.assertIn("City." + cty.id, dataSaved)
            self.assertIn("Amenity." + amty.id, dataSaved)
            self.assertIn("Review." + rvw.id, dataSaved)

    def testMethodReload(self):
        """Test method reload"""
        bse = BaseModel()
        usrr = User()
        stte = State()
        plce = Place()
        cty = City()
        amty = Amenity()
        rvw = Review()
        models.storage.new(bse)
        models.storage.new(usrr)
        models.storage.new(stte)
        models.storage.new(plce)
        models.storage.new(cty)
        models.storage.new(amty)
        models.storage.new(rvw)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bse.id, objs)
        self.assertIn("User." + usrr.id, objs)
        self.assertIn("State." + stte.id, objs)
        self.assertIn("Place." + plce.id, objs)
        self.assertIn("City." + cty.id, objs)
        self.assertIn("Amenity." + amty.id, objs)
        self.assertIn("Review." + rvw.id, objs)

    def testMethodAllError(self):
        """AssertRaises test check"""
        with self.assertRaises(TypeError):
            storage.all(None)

    def testMethodNewError(self):
        """AssertRaises test check"""
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def testSsaveError(self):
        """AssertRaises test check"""
        with self.assertRaises(TypeError):
            storage.save(None)

    def testReloadError(self):
        """AssertRaises test check"""
        with self.assertRaises(TypeError):
            storage.reload(None)

    def testImportStorage(self):
        """Check type import"""
        self.assertEqual(type(models.storage), FileStorage)

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

    def testStorageObjectsDict(self):
        """Test dict type"""
        self.assertTrue(type(models.storage.all()) == dict)


if __name__ == "__main__":
    unittest.main()
