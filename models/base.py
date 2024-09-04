#!/usr/bin/python3
"""BaseModel class module"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    def __init__(self):
        """Constructor method"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.categories = ""

    def __str__(self):
        """Str method for debugging purpose"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
