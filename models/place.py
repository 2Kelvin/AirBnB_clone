#!/usr/bin/python3
"""Contains class Place that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place: inherits from BaseModel

    Attributes:
        city_id: City.id
        user_id: User.id
        name: place name
        description: place's description
        number_rooms: place's number of rooms
        number_bathrooms: place's number of bathrooms
        max_guest: place's maximum number of guests
        price_by_night: place's night cost
        latitude: place's latitude
        longitude: place's longitude
        amenity_ids: list of place's Amenity.ids
        args: BaseModel's args
        kwargs: BaseModel kwargs
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
