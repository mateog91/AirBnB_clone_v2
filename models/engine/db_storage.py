#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""


class DBStorage:
    """Manage storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization of db"""
        __self.engine

