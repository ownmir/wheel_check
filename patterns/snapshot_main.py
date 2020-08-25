# Снимок поведенческий. Также известный как Memento
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Originator():  # создатель, инициатор
    """
    Создатель содержит некоторое важное состояние, которое может со временем
    меняться. Он также объявляет метод сохранения состояния внутри снимка и
    метод восстановления состояния из него.
    """

    _state = None
    """
    Для удобства состояние создателя хранится внутри одной переменной.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Создатель: Мое исходное состояние: {self._state}")

    def do_something(self) -> None:
        """
        Бизнес-логика Создателя может повлиять на его внутреннее состояние.
        Поэтому клиент должен выполнить резервное копирование состояния с
        помощью метода save перед запуском методов бизнес-логики.
        """

        print("Создатель: Я делаю что-то важное.")
        self._state = self._generate_random_string(30)
        print(f"Создатель: и мое состояние изменилось на: {self._state}")

    def _generate_random_string(self, length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        Сохраняет текущее состояние внутри снимка.
        """

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Восстанавливает состояние Создателя из объекта снимка.
        """

        self._state = memento.get_state()
        print(f"Создатель: Мое состояние изменилось на: {self._state}")


class Memento(ABC):  # Снимок
    """
        Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
        как дата создания или название. Однако он не раскрывает состояние Создателя.
        """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        Создатель использует этот метод, когда восстанавливает своё состояние.
        """
        return self._state

    def get_name(self) -> str:
        """
        Остальные методы используются Опекуном для отображения метаданных.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker():  # Опекун, смотритель
    """
    Опекун не зависит от класса Конкретного Снимка. Таким образом, он не имеет
    доступа к состоянию создателя, хранящемуся внутри снимка. Он работает со
    всеми снимками через базовый интерфейс Снимка.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print(f"Опекун: Сохранение состояния создателя ...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Опекун: Восстановление состояния на: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Опекун: Вот список снимков:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Супер-пупер")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nКлиент: А теперь давайте откатимся! \n")
    caretaker.undo()

    print("\nКлиент: еще раз! \n")
    caretaker.undo()
