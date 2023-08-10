#!/usr/bin/python3
"""Contains class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State: inherits from BaseModel

    Attributes:
        name: state name
        args: BaseModel's args
        kwargs: BaseModel kwargs
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
