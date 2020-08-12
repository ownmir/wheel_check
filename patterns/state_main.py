from __future__ import annotations
from abc import ABC, abstractmethod


class Context(ABC):
    """
    Контекст определяет интерфейс, интересующий клиентов. Он также поддерживает
    ссылку на экземпляр подкласса State, который представляет текущее
    состояние контекста.
    """

    _state = None
    """
    Ссылка на текущее состояние контекста.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        Контекст позволяет изменять объект состояния во время выполнения.
        """

        print(f"Контекст: переход к {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    Контекст делегирует часть своего поведения текущему объекту State.
    """

    def request_friend_turn(self):  # request1
        self._state.handle_friend_turn()  # handle1()

    def request_enemy_turn(self): # request2
        self._state.handle_enemy_turn()  # handle2()


class State(ABC):
    """
    Базовый класс State объявляет методы, которые должны реализовываться всеми Concrete State,
    а также предоставляет обратную ссылку на объект Context, связанный с State. Эта обратная ссылка может
    использоваться States для перевода контекста в другое состояние.
    """
    
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle_friend_turn(self) -> None:  # handle1
        pass

    @abstractmethod
    def handle_enemy_turn(self) -> None:  # handle2
        pass

"""
Конкретные состояния реализуют различные варианты поведения, связанные с состоянием Контекста.
"""
    
class FriendTurnState(State):  # ConcreteStateA
    def handle_friend_turn(self) -> None:  # handle1
        print("FriendTurnState обрабатывает запрос request_friend_turn")
        print("FriendTurnState хочет изменить состояние контекста")
        self.context.transition_to(EnemyTurnState())

    def handle_enemy_turn(self) -> None:  # handle2
        print("FriendTurnState обрабатывает запрос request_enemy_turn")
    

class EnemyTurnState(State):  # ConcreteStateB
    def handle_friend_turn(self) -> None:  # handle1
        print("EnemyTurnState обрабатывает запрос request_friend_turn")

    def handle_enemy_turn(self) -> None:  # handle2
        print("EnemyTurnState обрабатывает запрос request_enemy_turn")
        print("EnemyTurnState хочет изменить состояние контекста")
        self.context.transition_to(FriendTurnState())


if __name__ == "__main__":
    # Клиентский код.

    context = Context(FriendTurnState())
    context.request_friend_turn()
    context.request_enemy_turn()
