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

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if kwargs:
            pass
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.categories = "uncategorized"

    def __str__(self):
        """Str method for debugging purpose"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
     
    def save(self):
        """Method to save object instance to database"""
        from models import storage
        self.updated_at = datetime.now()
        storage.addingRecord(self)
        storage.savingRecord()
        
    def delete(self):
        from models import storage
        storage.delRecord(self)

    def to_dict(self):
        outDict = self.__dict__.copy()
        if '_sa_instance_state' in outDict:
            outDict.pop('_sa_instance_state')
        outDict.update({"__class__": self.__class__.__name__})
        outDict.update({"created_at": datetime.isoformat(outDict['created_at'])})
        outDict.update({"updated_at": datetime.isoformat(outDict['updated_at'])})
        return outDict
