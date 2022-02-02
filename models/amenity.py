#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
if HBNB_TYPE_STORAGE == 'db':
    from models.base_model import Base

    class Amenity(BaseModel, Base):
        """Class for amenities from the Base Model
        """
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place', secondary='place_amenity')
else:
    class Amenity(BaseModel):
        """Class for amenities from the Base Model
        """
        name = ""
