#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
if HBNB_TYPE_STORAGE == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user', cascade='delete')
        reviews = relationship('Review', backref='user', cascade='delete')
else:
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
