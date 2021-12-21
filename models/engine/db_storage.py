#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import (create_engine)
from sqlalchemy.sql.schema import MetaData
from models.base_model import Base
import os


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
