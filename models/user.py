#!/usr/bin/python3
"""Contains class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User: Inherits from class BaseModel

    Attributes:
        email: user's email
        password: user's password
        first_name: user's first_name
        last_name: user's last name
        args: BaseModel's args
        kwargs: BaseModel kwargs
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
