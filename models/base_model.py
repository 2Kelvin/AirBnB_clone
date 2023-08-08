#!/usr/bin/python3
"""Module contains the base class 'BaseModel'"""
import uuid
from datetime import datetime


class BaseModel():
    """Base class for all the other model classes

    Attributes:
        id: unique object id calculated thro UUID
        created_at: time object was created
        updated_at: time object was updated
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Custom __str__ method for BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        objDict = self.__dict__.copy()
        isoCreated = datetime.isoformat(self.created_at)
        isoUpdated = datetime.isoformat(self.updated_at)

        objDict["created_at"] = isoCreated
        objDict["updated_at"] = isoUpdated
        objDict["__class__"] = self.__class__.__name__
        return objDict
