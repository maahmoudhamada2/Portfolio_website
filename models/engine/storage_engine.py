#!/usr/bin/python3
from models.base import Base
from models.projects import Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None
    __db_url = 'mysql+mysqldb://root:root@localhost:5000/portfolio_website'

    def settingDB(self):
        from models.base import BaseModel
        from models.projects import Project
        self.__engine = create_engine(self.__db_url)
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(session_factory)

    def addingRecord(self, obj):
        self.__session.add(obj)

    def savingRecord(self):
        self.__session.commit()
