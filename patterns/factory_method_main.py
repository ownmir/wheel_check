from __future__ import annotations
from abc import ABC, abstractmethod


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Creator(ABC):
    """
    Класс Creator объявляет фабричный метод, который должен возвращать
    объект класса Product (Card). Подклассы Создателя обычно предоставляют
    реализация этого метода.
    """
    @abstractmethod
    def factory_method(self, *args):
        """
        Обратите внимание, что Создатель может также предоставить некоторую реализацию по умолчанию
        фабричного метода.
        :return:
        """
        pass

    def some_operation(self, *args) -> str:
        """
        Также обратите внимание, что, несмотря на название, основная обязанность Создателя
        не создавать продукты. Обычно он содержит основную бизнес-логику.
        которая полагается на объекты Card (Product), возвращаемые фабричным методом.
        Подклассы могут косвенно изменить эту бизнес-логику, переопределив
        factory и возвращая из него другой тип продукта.
        :return: result
        """
        # Вызовите фабричный метод, чтобы создать объект Card (Product).
        card = self.factory_method(*args)
        # Теперь воспользуйтесь продуктом.
        result = f"Создатель: тот же код создателя только работает с {card.operation()}"
        return result

    # def add_life(self, life):
    #     card = self.factory_method(life)
    #     print(f"add_life: жизнь до: {card.life}")
    #     card.life += life
    #     print(f"add_life: жизнь после: {card.life}")


# Конкретные Создатели переопределяют фабричный метод, чтобы изменить результирующий тип карты (продукта).
class HeroCreator(Creator):  # ConcreteCreator1
    """
    Обратите внимание, что в сигнатуре метода по-прежнему используется абстрактный тип продукта,
    даже если конкретный продукт фактически возвращается из метода. это
    способ, которым Создатель может оставаться независимым от конкретных классов продуктов.
    """

    def factory_method(self, *args) -> Hero:  # ConcreteProduct1
        return Hero()


class MinionCreator(Creator):

    def __init__(self, *args):
        pass
    
    def factory_method(self, *args) -> Minion:  # ConcreteProduct2
        return Minion(args[0], args[1])


class Card(ABC):  # Product
    """
    Выполняет роль класса Продукт
    Интерфейс продукта объявляет операции, которые все конкретные продукты
    должны реализовать.
    """
    def __init__(self):
        self.life = 0

    @abstractmethod
    def operation(self) -> str:
        pass

    @abstractmethod
    def draw(self) -> Picture:
        pass


# Конкретные продукты предоставляют различные реализации интерфейса продукта.
class Hero(Card):

    def __init__(self):
        self.life = 30

    def operation(self) -> str:
        return "{Результат of the Hero (ConcreteProduct1)}"

    def draw(self):
        print("Рисуем героя")


class Minion(Card):

    def __init__(self, life, cost):
        self.life = life
        self.cost = cost

    def operation(self) -> str:
        return "{Результат of the Minion ConcreteProduct2}"

    def draw(self):
        print("Рисуем существо")

    def add_life(self, life: int):
        print(f"add_life: жизнь до: {self.life}")
        self.life += life
        print(f"add_life: жизнь после: {self.life}")


def client_code(creator: Creator) -> None:
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать с создателем через
    базовый интерфейс, вы можете передать ему любой подкласс создателя.
    :param creator:
    :return:
    """
    print(f"Клиент: Я не знаю класс создателя, но он все еще работает.\n"
          f"{creator.some_operation(0,0)}", end="")


if __name__ == "__main__":
    print("App: Запущен с HeroCreator (ConcreteCreator1).")
    client_code(HeroCreator())
    print("\n")

    print("App: Запущен с MinionCreator (ConcreteCreator2).")
    client_code(MinionCreator(1,1))
