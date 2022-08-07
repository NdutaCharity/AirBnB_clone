#!/usr/bin/python3
"""
Defines amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose from to offer at its place"""
    name = ""
  def __init__(self, *args, **kwargs):
        """Creates new instances of Amenity.
        """
        super().__init__(*args, **kwargs)
