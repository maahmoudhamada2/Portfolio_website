#!/usr/bin/python3
"""Project class module"""
from models.base import BaseModel, Base
from sqlalchemy import String, Column


class Project(BaseModel, Base):
    """Project class inherting from BaseModel"""

    __tablename__ = "projects"
    title = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=False)
    technologies_used = Column(String(100), nullable=False)
    github_url = Column(String(60))
