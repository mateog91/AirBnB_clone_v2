#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import (create_engine)
from sqlalchemy.sql.schema import MetaData
import models
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
import os
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Manage storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization of db"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        self.__engine = create_engine(
            f"mysql+mysqldb://{os.getenv('HBNB_MYSQL_USER')}:{os.getenv('HBNB_MYSQL_PWD')}@{os.getenv('HBNB_MYSQL_HOST')}/{os.getenv('HBNB_MYSQL_DB')}", pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query to DB to bring all objects (optional Class)"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        session = Session()

        classes = [Amenity, City, Place, Review, State, User]

        if cls is None:
            dic = {}
            for cls in classes:
                lst_objs = self.__session.query(cls).all()

                dic.update({obj.__class__.__name__ + '.' +
                           obj.id: obj for obj in lst_objs})
            return dic
        else:
            lst_objs = session.query(cls).all()
            return {obj.__class__.__name__ + '.' + obj.id: obj for obj in lst_objs}
