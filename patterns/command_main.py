from __future__ import annotations
from abc import ABC, abstractmethod
import factory_method_main


class Command(ABC):
    """
    Командный интерфейс объявляет метод выполнения команды.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Некоторые команды могут самостоятельно выполнять простые операции.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload  # полезная нагрузка

    def execute(self) -> None:
        print(f"SimpleCommand: видите, я могу делать простые вещи, например, печатать"
              f"({self._payload})")


class HeartstoneCommand(SimpleCommand):
    """
    Простая команда для боевого клича или предсмертного хрипа, которая переопределяет метод  execute (меняет сообщение)
    """

    def __init__(self, payload: str):
        super().__init__(payload)

    def execute(self) -> None:
        print(f"HeartstoneCommand: печатаю"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    Однако некоторые команды могут делегировать более сложные операции другим
     объектам, называемым «приемниками (получателями)».
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Сложные команды могут принимать один или несколько объектов-получателей вместе с
         любыми данными контекста через конструктор.
        :param receiver:
        :param a:
        :param b:
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Команды можно делегировать любым методам получателя.
        :return:
        """

        print("ComplexCommand: Сложные вещи должны выполняться объектом-приемником", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class AddLifeCardCommand(Command):
    """
    Команда добавления жизни
    """

    def __init__(self, receiver: Card, life: int) -> None:
        self._receiver = receiver
        self._a = life
        # print(f"AddLifeCardCommand: жизнь до: {card.life}")
        # card.life += life
        # print(f"AddLifeCardCommand: жизнь после: {card.life}")

    def execute(self) -> None:
        """
        Команды можно делегировать любым методам получателя.
        :return:
        """

        print("AddLifeCard: Сложные вещи должны выполняться объектом-приемником", end="")
        self._receiver.add_life(self._a)


class Receiver:
    """
    Классы Receiver содержат важную бизнес-логику. Они умеют
     выполнять всевозможные операции, связанные с выполнением запроса.
     Фактически, любой класс может служить Приемником.
    """

    def do_something(self, a: str) -> None:
        print(f"\nПриемник: работает над ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nПриемник: Также работает над ({b}.)", end="")


class Invoker:
    """
    Invoker связан с одной или несколькими командами. Отправляет запрос
     к команде.
    """

    _on_start = None
    _on_finish = None

    """
    Инициализирует команды.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        Invoker не зависит от конкретной команды или классов получателя.
         Invoker передает запрос получателю косвенно, выполняя
         команду.
        :return:
        """

        print("Invoker: Кто-нибудь хочет, чтобы что-то было сделано до того, как я начну?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ... делаю что-то действительно важное ...")

        print("Invoker: Кто-нибудь хочет, чтобы что-то было сделано после того, как я закончу?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    Клиентский код может параметризовать вызывающего с любыми командами.
    """

    invoker = Invoker()
    # invoker.set_on_start(SimpleCommand("Передай привет!"))
    invoker.set_on_start(HeartstoneCommand("Я готов выступать!!"))
    # receiver = Receiver()
    receiver = factory_method_main.MinionCreator(1,1).factory_method(1,1)

    invoker.set_on_finish(AddLifeCardCommand(
        receiver, 1))

    invoker.do_something_important()
