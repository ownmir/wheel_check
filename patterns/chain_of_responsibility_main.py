from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Handler объявляет метод построения цепочки обработчиков.
    Он также объявляет метод выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри класса базового обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит нам связать обработчики
        # удобным способом вот так:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> None:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
Все конкретные обработчики либо обрабатывают запрос, либо передают его следующему обработчику в цепь.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Банан":
            return f"Обезьяна: Я съем {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Орех":
            return f"Белка: Я съем {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Фрикаделька":
            return f"Dog: Я съем {request}"
        else:
            return super().handle(request)


class BattleCryHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Боевой клич":
            return "Я готов выступать!"
        else:
            return super().handle(request)


class LifeHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Жизнь":
            return "Жду приказаний."
        else:
            return super().handle(request)


class DeathRattleHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Смерть":
            return "За мной придут другие!"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    Клиентский код обычно подходит для работы с одним обработчиком. В большинстве
    случаев он даже не знает, что обработчик является частью цепочки.
    :param handler:
    :return:
    """

    # for food in ["Орех", "Банан", "Чашка кофе"]:
    #     print(f"\nКлиент: Кто хочет {food}?")
    #     result = handler.handle(food)
    #     if result:
    #         print(f"  {result}", end="")
    #     else:
    #         print(f"  {food} осталась нетронутой.", end="")
    for part in ["Боевой клич", "Жизнь", "Побег", "Смерть"]:
        print(f"Клиент: часть - {part}")
        result = handler.handle(part)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"Какая-то непонятная часть: '{part}'", end="")


if __name__ == "__main__":
    # monkey = MonkeyHandler()
    # squirrel = SquirrelHandler()
    # dog = DogHandler()
    #
    # monkey.set_next(squirrel).set_next(dog)
    # # Клиент должен иметь возможность отправить запрос любому обработчику, а не только
    # # первому в цепочке.
    # print("Цепочка: Обезьяна> Белка> Собака")
    # client_code(monkey)
    # print("\n")
    #
    # print("Подцепочка: Белка> Собака")
    # client_code(squirrel)
    # print("\n")

    cry = BattleCryHandler()
    life = LifeHandler()
    death = DeathRattleHandler()

    cry.set_next(life).set_next(death)
    print("Цепочка: Боевой клич > Жизнь > Смерть")
    client_code(cry)
    print("\n")

    print("Подцепочка: Жизнь > Смерть")
    client_code(life)
    print("\n")
