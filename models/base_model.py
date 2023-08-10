#!/usr/bin/python3
"""Module contains the base class 'BaseModel'"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Base class for all the other model classes

    Attributes:
        id: unique object id calculated thro UUID
        created_at: time object was created
        updated_at: time object was updated
        args: unnamed arguments
        kwargs: named arguments
    Methods:
        __str__: custom BaseModel __str__ method
        save(): updates 'update_at'
        to_dict(): converts object to a dictionary
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0 and kwargs is not None:
            for dKey in kwargs.keys():
                if dKey == "created_at":
                    self.created_at = datetime.fromisoformat(kwargs[dKey])
                elif dKey == "updated_at":
                    self.updated_at = datetime.fromisoformat(kwargs[dKey])
                elif dKey == "id":
                    self.id = str(kwargs[dKey])
                elif dKey == "__class__":
                    continue
                else:
                    self.__dict__[dKey] = kwargs[dKey]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Custom __str__ method for BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        objDict = self.__dict__.copy()
        isoCreated = self.created_at.isoformat()
        isoUpdated = self.updated_at.isoformat()

        objDict["created_at"] = isoCreated
        objDict["updated_at"] = isoUpdated
        objDict["__class__"] = self.__class__.__name__
        return objDict
