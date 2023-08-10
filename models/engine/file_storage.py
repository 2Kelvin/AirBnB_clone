#!/usr/bin/python3
"""Contains class FileStorage"""
import json
from .. import base_model
from user import User
from state import State
from city import City
from amenity import Amenity
from place import Place
from review import Review

class FileStorage():
    """Serializes Python objects to a JSON file and
    deserializes JSON file to Python objects

    Attributes:
        __file_path: private path to a JSON file
        __objects: private dictionary of python objects
    Methods:
        all(): returns __objects dictionary
        new(): inserts new objects to __objects dictionary
        save(): converts __objects to JSON and saves in file
        reload(): converts JSON string to Python object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds objects to __objects dictionary"""
        objKey = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[objKey] = obj

    def save(self):
        """Serializes __objects to the JSON file at '__file_path'"""
        objsDict = {}
        for ky, vl in FileStorage.__objects.items():
            objsDict[ky] = vl.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as wFile:
            wFile.write(json.dumps(objsDict))

    def reload(self):
        """Deserializes a JSON file to Python __objects

        Raises:
            FileNotFoundError: ignores this error
                if the json file is not found
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as rFile:
                fDict = json.load(rFile)
                for k, vlue in fDict.items():
                    fDict[k] = self.airbnbClasses()[vlue["__class__"]](**vlue)
                FileStorage.__objects = fDict
        except FileNotFoundError:
            return

    @classmethod
    def airbnbClasses(cls):
        """Dictionary of all airbnb clasess imported to solve import errors

        Returns: a dictionary of all the other classes
        """
        allClasses = {
            "BaseModel": base_model.BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return allClasses
