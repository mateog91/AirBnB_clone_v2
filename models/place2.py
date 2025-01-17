#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.review import Review
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
if HBNB_TYPE_STORAGE == 'db':
    from models.base_model import Base
    reviews = relationship('Review', backref='place', cascade='delete')
    # Asociative Table
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

    class Place(BaseModel, Base):
        """ Class Place that difines a place to stay """
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

        amenities = relationship(
            'Amenity', secondary='place_amenity', viewonly=False,
            overlaps='place_amenities'
        )

else:
    class Place(BaseModel):
        """ Class Place that difines a place to stay """
        __tablename__ = "places"
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0
        longitude = 0

        def __init__(self, *args, amenity_ids=None, **kwargs):
            """init method for the initialization"""
            super().__init__(*args, **kwargs)
            self.amenity_ids = [] if amenity_ids is None else amenity_ids

        @property
        def reviews(self):
            """Getter of reviews"""
            reviews = models.storage.all(Review)
            return [
                value for value in reviews in reviews.values()
                if self.id == value.place_id]

        @property
        def amenities(self):
            """Getter for amenities"""
            lst_obj_amenities = models.storage.all(Amenity)
            return PlaceAmenities(
                [value for value in lst_obj_amenities.values()
                    if value.id in self.amenity_ids],
                place=self
            )

    class PlaceAmenities(list):
        """intermidiate class for place amenities
            it is a list with instance attribute: place (instance object)
        """

        def __init__(self, *args, place):
            """new int method for initialitation"""
            super().__init__(*args)
            self.place = place

        def append(self, arg):
            """handle append method for setter"""
            if isinstance(arg, Amenity):
                self.place.amenity_ids.append(arg.id)
                super().append(arg)
