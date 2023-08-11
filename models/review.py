#!/usr/bin/python3
"""Contains class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review: inherits from BaseModel

    Attributes:
        place_id: Place.id
        user.id: User.id
        text: user's string text review
        args: BaseModel's args
        kwargs: BaseModel kwargs
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
