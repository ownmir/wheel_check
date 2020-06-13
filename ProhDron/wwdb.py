from PySide2.QtSql import QSqlDatabase
from abc import ABC, abstractmethod

class WorkWithDB(ABC):
    def __init__(self, name):
        self.__name = name
        self.conn = None

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def open_db(self):
        pass

    def add(self, kind):
        self.conn = QSqlDatabase.addDatabase(kind)
        self.conn.setDatabaseName(self.name)

class WorkWithLiteDB(WorkWithDB):
    
    def open_db(self):
        self.add('QSQLITE')
        
        if self.conn.open():
            return self.conn
        else:
            print("Была ошибка открытия базы SQLITE с именем", self.__name)
            self.conn.lastError().text()
            return

class WorkWithMyDB(WorkWithDB):
    def __init__(self, name, host, user, passw):
        WorkWithDB.__init__(self, name)
        self.__name = name
        self.__host = host
        self.__user = user
        self.__pass = passw

    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    def open_db(self):
        self.add('QMYSQL')
        self.conn.setHostName(self.host)
        # conn.setDatabaseName(self.name)
        self.conn.setUserName(self.user)
        self.conn.setPassword(self.__pass)
        if self.conn.open():
            return self.conn
        else:
            print("Была ошибка открытия базы mysql с именем", self.name)
            self.conn.lastError().text()
            return
