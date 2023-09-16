"""
*О чем этот шаблон?
Он разделяет создание сложного объекта и его представление,
так что один и тот же процесс может быть повторно использован для построения
объектов из одной и той же семьи. Это полезно, когда необходимо отделить
описание объекта от его фактического представления (как правило, для абстракции).

*Что делает этот пример?
Первый пример достигает этого, используя абстрактный базовый класс для здания,
где конструктор (init метод) указывает необходимые шаги,
а конкретные подклассы реализуют эти шаги.

В других языках программирования иногда необходимо использовать более сложную организацию.
В частности, в C++ нельзя иметь полиморфное поведение в конструкторе - см.
 https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor,
что означает, что эта техника на Python не сработает.
Требуемое полиморфное поведение должно быть предоставлено внешним,
уже созданным экземпляром другого класса.

В целом, в Python это, как правило, не требуется, но также представлен второй пример,
 показывающий такого рода организацию.

*Где практически используется этот шаблон?
*Ссылки:
https://sourcemaking.com/design_patterns/builder

*Кратко
Разделяет создание сложного объекта и его представление.
"""


# Abstract Building
class Building:
    def __init__(self) -> None:
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return "Floor: {0.floor} | Size: {0.size}".format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self) -> None:
        self.floor = "One"

    def build_size(self) -> None:
        self.size = "Big"


class Flat(Building):
    def build_floor(self) -> None:
        self.floor = "More than One"

    def build_size(self) -> None:
        self.size = "Small"


# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)


class ComplexBuilding:
    def __repr__(self) -> str:
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self) -> None:
        self.floor = "One"

    def build_size(self) -> None:
        self.size = "Big and fancy"


def construct_building(cls) -> Building:
    building = cls()
    building.build_floor()
    building.build_size()
    return building


def main():
    """
    >>> house = House()
    >>> house
    Floor: One | Size: Big

    >>> flat = Flat()
    >>> flat
    Floor: More than One | Size: Small

    # Using an external constructor function:
    >>> complex_house = construct_building(ComplexHouse)
    >>> complex_house
    Floor: One | Size: Big and fancy
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
