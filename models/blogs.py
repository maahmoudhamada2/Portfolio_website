#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import Column, String, DateTime


class Blog(BaseModel, Base):
    __tablename__ = 'blogs'
    blog_title = Column(String(60), nullable=False)
    author = Column(String(60), nullable=False)
    intro = Column(String(1024), nullable=False)
    article = Column(String(2048), nullable=False)
    conclusion = Column(String(2048), nullable=False)
    # publish_date = Column(DateTime, nullable= Flase) -- TODO
    # img_url = Column(String(60))  -- TODO
