#!/usr/bin/python3
""" Place Module for HBNB project """
from typing import overload
from sqlalchemy.orm import relationship
import models
from models import review
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.review import Review
from models.amenity import Amenity
import os

# Asociative Table
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
    if HBNB_TYPE_STORAGE == 'db':
        reviews = relationship('Review', backref='place', cascade='delete')

        amenities = relationship(
            'Amenity', secondary='place_amenity', viewonly=False, overlaps='place_amenity')

    else:
        @property
        def reviews(self):
            """Getter of reviews"""
            reviews = models.storage.all(Review)
            return [value for value in reviews in reviews.values if self.id == value.place_id]

        @property
        def amenities(self):
            """Getter for amenities"""
            lst_obj_amenities = models.storage.all(Amenity)
            return [value for value in lst_obj_amenities.values if value.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, arg):
            """Setter for amenities"""
            if isinstance(arg, Amenity):
                # amenity_id.append(arg.id)
                self.amenity_ids.append(arg.id)
