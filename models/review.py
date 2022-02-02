#!/usr/bin/python3
""" Review module for the HBNB project """
import imp
import os
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
if HBNB_TYPE_STORAGE == 'db':
    from models.base_model import Base

    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
else:
    class Review(BaseModel):
        """ Review classto store review information """
        text = ""
        user_id = ""
        place_id = ""
