#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.expression import delete
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
    if HBNB_TYPE_STORAGE == 'db':
        cities = relationship('City', backref='state', cascade='delete')

    else:
        @property
        def cities(self):
            """Getter of the cities"""
            cities = models.storage.all(City)
            return [value for value in cities.values() if self.id == value.state_id]
