#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
import models
from models import review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from models.review import Review
import os


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
    # amenity_ids = [] REVISAR!!!!!

    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
    if HBNB_TYPE_STORAGE == 'db':
        reviews = relationship('Review', backref='place', cascade='delete')

    else:
        @property
        def reviews(self):
            """Getter of reviews"""
            reviews = models.storage.all(Review)
            return [value for value in reviews in reviews.values if self.id == value.place_id]
