#!/usr/bin/python3
"""
Module contains unittests for module
package init file
"""
import unittest
import models
from models import storage


class TestInit(unittest.TestCase):
    """Unittest testcases for init file"""

    def testModuleDocs(self):
        """Check if module init docs are available"""
        self.assertTrue(len(models.__init__.__doc__) >= 1)

    def testStorageImported(self):
        """Check if storage instance has been created"""
        self.assertTrue(storage)

    def testStorageReload(self):
        """Check if storage reload exists"""
        self.assertTrue(storage.reload)

    def testFileStorageImported(self):
        """Check if FileStorage class has been imported"""
        self.assertTrue(hasattr(models, "FileStorage"))


if __name__ == "__main__":
    unittest.main()
