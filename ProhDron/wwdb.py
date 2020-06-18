from PySide2.QtSql import QSqlDatabase
from abc import ABC, abstractmethod


class WorkWithDB(ABC):
    def __init__(self, name):
        self.__name = name
        self._conn = None

    @property
    def name(self):
        return self.__name

    @property
    def connect(self):
        return self._conn

    @connect.setter
    def connect(self, value):
        _conn = value
        return

    @abstractmethod
    def open_db(self):
        pass

    def add(self, kind):
        self.connect = QSqlDatabase.addDatabase(kind)
        self.connect.setDatabaseName(self.name)


class WorkWithLiteDB(WorkWithDB):
    
    def open_db(self):
        self.add('QSQLITE')
        
        if self.connect.open():
            return self.connect
        else:
            print("Была ошибка открытия базы SQLITE с именем", self.__name, self.connect.lastError().text())
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
        self.connect.setHostName(self.host)
        self.connect.setPort(self.port)
        # conn.setDatabaseName(self.name)
        self.connect.setUserName(self.user)
        self.connect.setPassword(self.__pass)

    def _output(self):
        print("Подробности: isOpen()", self.connect.isOpen(), "| isOpenError()", self.connect.isOpenError(),
              "| lastError()", self.connect.lastError(), "| lastError().text()", self.connect.lastError().text(),
              "| lastError().databaseText() - DB", self.connect.lastError().databaseText(),
              "| lastError().driverText() - Qt", self.connect.lastError().driverText(),
              "| connectectionName()", self.connect.connectectionName(), "Доступные драйверы", self.connect.drivers()
              )

    def open_db(self):
        self.add('QMYSQL')
        self.set_general_options()  # host, port, user, passw

        if self.connect.open():
            self._output()
            return self.connect
        else:
            print("Была ошибка открытия базы mysql с именем", self.name)
            self._output()
            print("Db and Qt errors with space / Ошибки Db и Qt через пробел", self.connect.lastError().text())
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
        self.connect = QSqlDatabase.addDatabase("QODBC3")
        self.connect.setDatabaseName("{{Driver={0}}};DSN={1};UID={2};PWD={3}".format(self.driver, self.name, self.user,
                                                                                  self.__pass))
        if self.connect.open():
            self._output()
            return self.connect
        else:
            print("Была ошибка открытия базы через odbc с именем", self.name)
            self._output()
            print("Db and Qt errors with space / Ошибки Db и Qt через пробел", self.connect.lastError().text())
            return
