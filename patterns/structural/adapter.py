"""
Паттерн Адаптер (Adapter) предоставляет другой интерфейс для класса. Можно представить
его как адаптер для кабеля, который позволяет заряжать телефон в розетке с другой формой.
Следуя этой идее, паттерн Адаптер полезен для интеграции классов, которые не могли быть
интегрированы из-за несовместимых интерфейсов.

В данном примере присутствуют классы, представляющие сущности
(Собака, Кот, Человек, Автомобиль), которые издают разные звуки.
Класс Адаптер предоставляет другой интерфейс для оригинальных методов, создающих такие звуки.
Таким образом, оригинальные интерфейсы (например, bark и meow)
становятся доступными под другим именем: make_noise.

Паттерн Адаптер часто используется в практике для работы с объектами
через конкретный API без изменения самих объектов. Например, фреймворк
Grok использует адаптеры для интеграции объектов с определенным API без модификации самих объектов.

Ссылки:
- http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
- https://sourcemaking.com/design_patterns/adapter
- http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

TL;DR: Позволяет использовать интерфейс существующего класса как другой интерфейс.
"""

from typing import Callable, TypeVar

T = TypeVar("T")


class Dog:
    def __init__(self) -> None:
        self.name = "Dog"

    def bark(self) -> str:
        return "woof!"


class Cat:
    def __init__(self) -> None:
        self.name = "Cat"

    def meow(self) -> str:
        return "meow!"


class Human:
    def __init__(self) -> None:
        self.name = "Human"

    def speak(self) -> str:
        return "'hello'"


class Car:
    def __init__(self) -> None:
        self.name = "Car"

    def make_noise(self, octane_level: int) -> str:
        return f"vroom{'!' * octane_level}"


class Adapter:
    """Adapts an object by replacing methods.

    Usage
    ------
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj: T, **adapted_methods: Callable):
        """We set the adapted methods in the object's dict."""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__


def main():
    """
    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}

    >>> objects.append(Adapter(dog, make_noise=dog.bark))

    >>> objects[0].__dict__['obj'], objects[0].__dict__['make_noise']
    (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)

    >>> print(objects[0].original_dict())
    {'name': 'Dog'}

    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    >>> for obj in objects:
    ...    print("A {0} goes {1}".format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
