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
            print(type(self.conn))
            return self.conn
        else:
            print("Была ошибка открытия базы SQLITE с именем", self.__name, self.conn.lastError().text())
            return


class WorkWithMyDB(WorkWithDB):
    def __init__(self, name, host, port, user, passw):
        WorkWithDB.__init__(self, name)
        self.__name = name
        self.__host = host
        self.__port = port
        self.__user = user
        self.__pass = passw

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def user(self):
        return self.__user

    def set_general_options(self):
        self.conn.setHostName(self.host)
        self.conn.setPort(self.port)
        # conn.setDatabaseName(self.name)
        self.conn.setUserName(self.user)
        self.conn.setPassword(self.__pass)

    def _output(self):
        print("Подробности: isOpen()", self.conn.isOpen(), "| isOpenError()", self.conn.isOpenError(),
              "| lastError()", self.conn.lastError(), "| lastError().text()", self.conn.lastError().text(),
              "| lastError().databaseText() - DB", self.conn.lastError().databaseText(),
              "| lastError().driverText() - Qt", self.conn.lastError().driverText(),
              "| connectionName()", self.conn.connectionName(), "Доступные драйверы", self.conn.drivers()
              )

    def open_db(self):
        self.add('QMYSQL')
        self.set_general_options()  # host, port, user, passw

        if self.conn.open():
            self._output()
            return self.conn
        else:
            print("Была ошибка открытия базы mysql с именем", self.name)
            self._output()
            print("Db and Qt errors with space / Ошибки Db и Qt через пробел", self.conn.lastError().text())
            return


class WorkWithODBC(WorkWithMyDB):
    def __init__(self, driver, name, host, port, user, passw):
        WorkWithMyDB.__init__(self, name, host, port, user, passw)
        self.__driver = driver
        self.__pass = passw

    @property
    def driver(self):
        return self.__driver

    def open_db(self):
        self.conn = QSqlDatabase.addDatabase("QODBC3")
        self.conn.setDatabaseName("{{Driver={0}}};DSN={1};UID={2};PWD={3}".format(self.driver, self.name, self.user,
                                                                                  self.__pass))
        if self.conn.open():
            self._output()
            return self.conn
        else:
            print("Была ошибка открытия базы через odbc с именем", self.name)
            self._output()
            print("Db and Qt errors with space / Ошибки Db и Qt через пробел", self.conn.lastError().text())
            return
