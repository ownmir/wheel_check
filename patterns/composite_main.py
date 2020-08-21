from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    Базовый класс Component объявляет общие операции как для простых, так и для
    сложных объектов композиции.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        При желании базовый Компонент может объявить интерфейс для настройки и
        доступ к родительскому элементу компонента в древовидной структуре. Он также может
        предоставить некоторую реализацию по умолчанию для этих методов.
        """

        self._parent = parent

    """
    В некоторых случаях было бы полезно определить операции управления детьми
    прямо в базовом классе Component. Таким образом, вам не нужно
    предоставлять клиентскому коду любые конкретные классы компонентов даже во время
    сборки дерева объектов. Обратной стороной является то, что эти методы будут пустыми для
    компонентов конечного уровня.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        Вы можете предоставить метод, который позволяет клиентскому коду выяснить,
        может ли компонент иметь детей.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        Базовый компонент может реализовать какое-то поведение по умолчанию или передать его
        конкретным классам (объявив метод, содержащий поведение, как абстрактный").
        """

        pass


class Leaf(Component):
    """
    Класс Leaf представляет конечные объекты композиции. Лист не может
    иметь никаких детей.

    Обычно основную работу выполняют объекты Leaf, тогда как Composite
    объекты только делегируют своим субкомпонентам.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    Класс Composite представляет сложные компоненты, которые могут иметь
    детей. Обычно объекты Composite делегируют фактическую работу своим
    детям, а затем «подводят итоги».
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    Составной объект может добавлять или удалять другие компоненты (как простые, так и
    сложные) в его дочерний список или из него.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        Composite определенным образом выполняет свою основную логику. Это
        рекурсивно проходит через всех своих потомков, собирая и суммируя
        их результаты. Поскольку дочерние элементы композита передают эти вызовы своим
        children и т. д., в результате выполняется обход всего дерева объектов.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

def client_code(component: Component) -> None:
    """
    Клиентский код работает со всеми компонентами через базовый интерфейс.
    """

    print(f"RESULT: {component.operation()}", end="")

def client_code2(component1: Component, component2: Component) -> None:
    """
    Благодаря тому, что операции дочернего управления объявлены в
    базовом классе Component, клиентский код может работать с любым компонентом, простым или
    сложным, вне зависимости от конкретных классов.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать простые листовые компоненты ...
    simple = Leaf()
    print("Клиент: У меня есть простой компонент:")
    client_code(simple)
    print("\n")

    #... а также сложные состовные.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Клиент: Теперь у меня есть составное дерево:")
    client_code(tree)
    print("\n")

    print("Клиент: Мне не нужно проверять классы компонентов даже при управлении деревом: ")
    client_code2(tree, simple)
