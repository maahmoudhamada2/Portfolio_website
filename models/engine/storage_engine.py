#!/usr/bin/python3
from models.base import Base
from models.projects import Project
from models.blogs import Blog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None
    __db_url = 'mysql+mysqldb://root:root@localhost:5000/PFSITE'

    @staticmethod
    def recordsFormating(records, flag):
        objsDict = {}
        if flag:
            for clsList in records:
                for record in clsList:
                    key = "{}.{}".format(record.__class__.__name__, record.id)
                    objsDict.update({key: record})
        else:
            for record in records:
                key = "{}.{}".format(record.__class__.__name__, record.id)
                objsDict.update({key: record})
        return objsDict

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

    def getRecords(self, cls=None):
        recordsList = []
        if cls:
            records = self.__session.query(cls).all()
            return self.recordsFormating(records, 0)
        else:
            classes = [Project, Blog]
            for cls in classes:
                recordsList.append(self.__session.query(cls).all())
            return self.recordsFormating(recordsList, 1)

    def getRecord(self, cls, id):
        classes = {'Project': Project, 'Blog': Blog}
        records = self.getRecords(cls)
        for k in classes.keys():
            if cls.__name__ == k:
                key = "{}.{}".format(k, id)
        if key in records:
            return records.get(key)

    def delRecord(self, record):
        self.__session().delete(record)
        self.savingRecord()

