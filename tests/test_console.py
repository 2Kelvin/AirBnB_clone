#!/usr/bin/python3
"""Contains Console unittests"""
import unittest
from console import HBNBCommand
from unittest.mock import create_autospec
import sys


class TestConsole(unittest.TestCase):
    """Unittest testcases for Console"""

    def test_docs(self):
        """Doc test"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    def testTheConsole(self, server=None):
        """Console test"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def testCommandQuit(self):
        """Test Console quit"""
        cmd = HBNBCommand()
        self.assertRaises(SystemExit, quit)


if __name__ == "__main__":
    unittest.main()
