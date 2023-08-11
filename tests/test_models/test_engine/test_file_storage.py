#!/usr/bin/python3
"""Module contains unittest testcases for FileStorage"""
import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage


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


if __name__ == "__main__":
    unittest.main()
