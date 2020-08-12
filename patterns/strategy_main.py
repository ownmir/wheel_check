from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from factory_method_main import HeroCreator


class Context():
    """
    Контекст определяет интерфейс, интересующий клиентов.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Обычно контекст принимает стратегию через конструктор, но
        также предоставляет сеттер для его изменения во время выполнения.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Контекст поддерживает ссылку на один из объектов стратегии.
        Контекст не знает конкретного класса стратегии. Он должен работать
        со всеми стратегиями через интерфейс Стратегии.
        """
    
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Обычно контекст позволяет заменять объект стратегии во время выполнения.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        Контекст делегирует некоторую работу объекту стратегии вместо
        реализация нескольких версий алгоритма самостоятельно.
        """
        
        # ...

        print("Контекст: манипулирование данными с использованием стратегии (не знаю, как она это сделает)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...



class Strategy(ABC):
    """
    Интерфейс стратегии объявляет операции, общие для всех поддерживаемых версий
    какого-то алгоритма.
    Контекст использует этот интерфейс для вызова алгоритма, определенного конкретными
    стратегиями.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Конкретные стратегии реализуют алгоритм, следуя базовой стратегии
интерфейса. Интерфейс делает их взаимозаменяемыми в контексте.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # Клиентский код выбирает конкретную стратегию и передает ее в контекст.
    # Клиент должен знать о различиях между стратегиями, чтобы
    # сделать правильный выбор.
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
    hero = HeroCreator().factory_method()
    hero.draw()
