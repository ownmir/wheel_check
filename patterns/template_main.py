from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    Абстрактный Класс определяет шаблонный метод, содержащий скелет некоторого
    алгоритма, состоящего из вызовов (обычно) абстрактных примитивных операций.

    Конкретные подклассы должны реализовать эти операции, но оставить сам
    шаблонный метод без изменений.
    """

    def template_method(self) -> None:
        """
        Шаблонный метод определяет скелет алгоритма.
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # Эти операции уже имеют реализации.

    def base_operation1(self) -> None:
        print("AbstractClass говорит: я делаю основную часть работы")

    def base_operation2(self) -> None:
        print("AbstractClass говорит: Но я позволяю подклассам переопределять некоторые операции")

    def base_operation3(self) -> None:
        print("AbstractClass говорит: Но я все равно делаю большую часть работы")

    # А эти операции должны быть реализованы в подклассах.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # Это «хуки». Подклассы могут переопределять их, но это не обязательно,
    # поскольку у хуков уже есть стандартная (но пустая) реализация. Хуки
    # предоставляют дополнительные точки расширения в некоторых критических
    # местах алгоритма.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    Конкретные классы должны реализовать все абстрактные операции базового
    класса. Они также могут переопределить некоторые операции с реализацией по
    умолчанию.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 говорит: Реализована Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 говорит: Реализована Operation2")


class ConcreteClass2(AbstractClass):
    """
    Обычно конкретные классы переопределяют только часть операций базового
    класса.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 говорит: Реализована Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 говорит: Реализована Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 говорит: Переопределен Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    """
    Клиентский код вызывает шаблонный метод для выполнения алгоритма. Клиентский
    код не должен знать конкретный класс объекта, с которым работает, при
    условии, что он работает с объектами через интерфейс их базового класса.
    """

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":
    print("Один и тот же клиентский код может работать с разными подклассами:")
    client_code(ConcreteClass1())
    print("")

    print("Один и тот же клиентский код может работать с разными подклассами:")
    client_code(ConcreteClass2())
