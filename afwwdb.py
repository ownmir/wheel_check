from abc import ABCMeta, abstractmethod


class Db(metaclass=ABCMeta):
    def __init__(self):
        self.__name = None
        self.__host = None
        self.__port = None
        self.__user = None
        self.__passw = None

    @abstractmethod
    def open_db(self):
        pass


class Lite(Db):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def open_db(self):
        print("Lite")

# python шаблон абстрактная фабрика
# https://refactoring.guru/ru/design-patterns/abstract-factory
# https://proglib.io/p/py-patterns