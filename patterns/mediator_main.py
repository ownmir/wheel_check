from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    """
    Также известный как Intermediary,  Controller
    Интерфейс посредника объявляет метод, используемый компонентами для уведомления
     посредника по поводу различных событий. Посредник может реагировать на эти события и
     передать выполнение другим компонентам.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Посредник реагирует на A и запускает следующие операции:")
            self._component2.do_c()
        elif event == "D":
            print("Посредник реагирует на D и запускает следующие операции:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    Базовый компонент обеспечивает базовую функциональность по хранению данных экземпляра посредника
     внутри объектов компонентов.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Конкретные компоненты реализуют различные функции. Они не зависят от других
компонентов. Они также не зависят от каких-либо конкретных классов посредников.
"""


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Компонент 1 выполняет А.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Компонент 1 выполняет B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Компонент 2 выполняет C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Компонент 2 выполняет D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    # Клиентский код
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Клиент запускает операцию A.")
    c1.do_a()

    print("\n", end="")

    print("Клиент запускает операцию D.")
    c2.do_d()
