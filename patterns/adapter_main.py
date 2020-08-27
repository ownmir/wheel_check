# Также известен как: Wrapper
class Target:
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self) -> str:
        return "Target: поведение цели по умолчанию."


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_request(self) -> str:
        # Особое поведение адаптируемого.
        return ".огомеуритпада еинедевоп еобосО"


class Adapter(Target):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря агрегации.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (ПЕРЕВЕДЕН) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Клиент: Я могу нормально работать с целевыми объектами:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Клиент: у класса Adaptee странный интерфейс."
          "Видишь, я его не понимаю:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Клиент: Но я могу работать с ним через Адаптер:")
    adapter = Adapter(adaptee)
    client_code(adapter)
