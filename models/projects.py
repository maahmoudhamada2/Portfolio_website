#!/usr/bin/python3
"""Project class module"""
from models.base import BaseModel


class Project(BaseModel):
    """Project class inherting from BaseModel"""
    title = ""
    description = ""
    technologies_used = ""
    github_url = ""
