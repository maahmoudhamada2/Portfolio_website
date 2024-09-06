#!/usr/bin/python3
"""AdminPanel to control Portfolio website"""
import re
import cmd
from models.base import BaseModel
from models.projects import Project
from models.blogs import Blog
from models import storage

class AdminPanel(cmd.Cmd):
    """AdminPanel class inhert from Cmd class"""


    prompt = "(PFSITE) "
    __classes = {'BaseModel': BaseModel, 'Project': Project, 'Blog': Blog}

    # =============================== Bulit-in methods ==============================

    def do_EOF(self, line):
        print()
        return True

    # -------------------------------------

    def do_quit(self, line):
        """Cmd method to quit prompt"""
        return True

    # =============================== Static methods ==============================

    @staticmethod
    def stringFormat(key, value):
        """Static method to format string"""
        tmp = ""
        if key == 'technologies_used':
            value = value.replace(' ', ', ')

        for c in value:
            if c == '"':
                continue
            tmp += c
        return tmp

    # ------------------------------------------------------

    @staticmethod
    def attrSetter(obj, attributes):
        """Static method to set attributes to an object"""
        # skipKeys = ['id', 'created_at', 'updated_at'] --TODO
        attributes = re.split('\"\s', attributes)
        for attr in attributes:
            key, value = attr.split('="')
            value = AdminPanel.stringFormat(key, value)
            setattr(obj, key, value)

    # ------------------------------------------------------
    
    @staticmethod
    def inputChecker(line, flag):
        if not line:
            return "Error: No input"

        elif line.split()[0] not in AdminPanel.__classes:
            return "Error: Class not found"

        elif flag == 2:
            cls = line.split()[0]
            try:
                id = line.split()[1]
            except IndexError:
                return "Error: Missing id"
            else:
                key = "{}.{}".format(cls, id)
                if key not in storage.getRecords():
                    return "Erorr: Record not exists"

    # ------------------------------------------------------
    
    @staticmethod
    def printer(data, flag=None):
        if not flag:
            print(data)
        else:
            key = "{}.{}".format(data.__class__.__name__, data.id)
            print(key)
            print('------------------------------------------')
            for key, value in data.__dict__.items():
                if key == '_sa_instance_state':
                    continue
                print('\t {}: {}'.format(key, value))

    # =========================== Cmd methods ==================================

    def do_create(self, line):
        """Method to create new object"""
        error = AdminPanel.inputChecker(line, 1)
        if error:
            AdminPanel.printer(error)
            return
        else:
            cls = line if line in self.__classes else line.split()[0]
            obj = self.__classes[cls]()
            attributes = line[line.find(' ') + 1 :] if line.find(' ') != -1 else []
            if attributes != []:
                self.attrSetter(obj, attributes)
            obj.save()
            AdminPanel.printer("{}.{}".format(obj.__class__.__name__, obj.id))
    
    # ------------------------------------------------------------------------

    def do_all(self, line):
        if not line:
            records = storage.getRecords()
        elif line not in self.__classes:
            AdminPanel.printer("Error: Class not found")
            return
        else:
            cls = self.__classes[line]
            records = storage.getRecords(cls)

        for record in records.values():
            AdminPanel.printer(record, 1)

    # ------------------------------------------------------------------------

    def do_display(self, line):
        error = AdminPanel.inputChecker(line, 2)
        if error:
            AdminPanel.printer(error)
            return
        else:
            cls = self.__classes[line.split()[0]]
            id = line.split()[1]
            record = storage.getRecord(cls, id)
            AdminPanel.printer(record, 1)

    # ------------------------------------------------------------------------

    def do_delete(self, line):
        error = AdminPanel.inputChecker(line, 2)
        if error:
            AdminPanel.printer(error)
            return
        else:
            cls = self.__classes[line.split()[0]]
            id = line.split()[1]
            record = storage.getRecord(cls, id)
            record.delete()

    # ------------------------------------------------------------------------

    def do_edit(self, line):
        error = AdminPanel.inputChecker(line, 2)
        if error:
            AdminPanel.printer(error)
            return
        else:
            cls = self.__classes[line.split()[0]]
            id = line.split()[1]
            tmp = line.split()[0] + ' ' + id + ' '
            attributes = line.replace(tmp, "")
            if attributes + ' ' != tmp:
                record = storage.getRecord(cls, id)
                self.attrSetter(record, attributes)
                record.save()

    # ------------------------------------------------------------------------

if __name__ == '__main__':
    AdminPanel().cmdloop()
