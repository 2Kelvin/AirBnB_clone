#!/usr/bin/python3
"""Contains class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity: inherits from BaseModel

    Attributes:
        name: amenity name
        args: BaseModel's args
        kwargs: BaseModel kwargs
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
