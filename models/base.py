#!/usr/bin/python3
"""BaseModel class module"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel:
    """BaseModel class"""
    id = Column(String(50), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    categories = Column(String(20), nullable=False, default='uncategorized')

    def __init__(self):
        """Constructor method"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.categories = "uncategorized"

    def __str__(self):
        """Str method for debugging purpose"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
