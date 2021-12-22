#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import (create_engine)
from sqlalchemy.sql.schema import MetaData
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
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
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                             pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query to DB to bring all objects (optional Class)"""
        if cls is None:
            classes = [Amenity, City, Place, Review, State, User]
            dic = {}
            for cls in classes:
                lst_objs = self.__session.query(cls).all()

                dic.update({obj.__class__.__name__ + '.' +
                           obj.id: obj for obj in lst_objs})

            return dic
        else:
            if type(cls) is str:
                cls = eval(cls)
            lst_objs = self.__session.query(cls).all()

            return {obj.__class__.__name__ + '.' + obj.id: obj for obj in lst_objs}

    def new(self, obj):
        """Add obj to DB"""
        self.__session.add(obj)

    def save(self):
        """Commits the changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete and object from  the session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        session_secure = scoped_session(session_factory)
        self.__session = session_secure

    def close(self):
        self.__session.close()
