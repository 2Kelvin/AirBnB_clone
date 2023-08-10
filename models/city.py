#!/usr/bin/python3
"""Contains class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City: inherits from BaseModel

    Attributes:
        state_id: city's state_id
        name: city name
        args: BaseModel's args
        kwargs: BaseModel kwargs
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
