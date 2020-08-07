import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

class Card:
    def __init__(self):
        self.life = 0

    

class Hero(Card):
    def __init__(self):
        self.life = 30


class Minion(Card):
    """
    Python предоставляет свой собственный интерфейс Prototype через `copy.copy`
    и     Функции copy.deepcopy. И любой класс, который хочет реализовать
    собственный     реализации должны переопределять члены `__copy__` и`
    __deepcopy__`     функции.
    """
    def __init__(self, life, cost, some_list_of_objects=[], some_circular_ref=None):
        self.life = life
        self.cost = cost
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref


    def __copy__(self):
        """
        Создает поверхностную копию. Этот метод будет вызываться всякий раз, когда
        кто-то вызывает copy.copy с этим объектом, и возвращаемое значение возвращается как
         новая поверхностная копия.
        """
        #Сначала создадим копии вложенных объектов.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        # Затем давайте клонируем сам объект, используя подготовленные клоны
        # вложенных объекта
        new_object = self.__class__(self.life, self.cost, some_list_of_objects, some_circular_ref
        )
        new_object.__dict__.update(self.__dict__)
        return new_object

    def __deepcopy__(self, memo={}):
        """
        Создает глубокую копию. Этот метод будет вызываться всякий раз, когда кто-то вызывает
        copy.deepcopy с этим объектом, и возвращаемое значение возвращается как новая глубокая копия.
        Какая польза от аргумента «memo»? Memo - это словарь, который используется библиотекой
        deepcopy для предотвращения бесконечных рекурсивных копий в
        экземпляры циклических ссылок. Передайте его всем вызовам `deepcopy`         вы делаете в
        реализации `__deepcopy__`, чтобы предотвратить бесконечные  рекурсии.
        """
        #Сначала создадим копии вложенных объектов.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        # Затем давайте клонируем сам объект, используя подготовленные клоны
        # вложенных объекта
        new_object = self.__class__(self.life, self.cost, some_list_of_objects, some_circular_ref
        )
        new_object.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new_object


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    hero = Hero()
    minion = Minion(1, 1)
    minion_with_list_ref = Minion(1, 1, list_of_objects, circular_ref)
    circular_ref.set_parent(minion_with_list_ref)

    shallow_copied_card = copy.copy(minion_with_list_ref)
    shallow_copied_card.some_list_of_objects.append("another object")
    if minion_with_list_ref.some_list_of_objects[-1] == "another object":
        print("adds")
    else:
        print("does not add")
    # Изменим набор в списке объектов
    minion_with_list_ref.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_card.some_list_of_objects[1]:
        print("4 y")
    else:
        print("4 n")
    deep_copied_card = copy.deepcopy(minion_with_list_ref)
    # Давайте изменим список в deep_copied_card и посмотрим, изменится ли он в card
    deep_copied_card.some_list_of_objects.append("one more object")
    if minion_with_list_ref.some_list_of_objects[-1] == "one more object":
        print("adds")
    else:
        print("does not")
    # Изменим набор в списке объектов.
    minion_with_list_ref.some_list_of_objects[1].add(10)
    if 10 in deep_copied_card.some_list_of_objects[1]:
        print("10 in")
    else:
        print("10 not in")
    print(
        f"id(deep_copied_card.some_circular_ref.parent): "
        f"{id(deep_copied_card.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_card.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_card.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print("Это показывает, что глубоко скопированные объекты содержат одну и ту же ссылку, они не клонируются повторно")
