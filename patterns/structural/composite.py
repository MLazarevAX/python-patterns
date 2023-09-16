"""
*What is this pattern about?*
Паттерн Composite описывает группу объектов, которая обрабатывается так же,
как один экземпляр того же типа объекта. Намерение использования
паттерна Composite заключается в "компоновке" объектов в структуры дерева
для представления иерархий "часть-целое". Реализация паттерна Composite
позволяет клиентам обрабатывать как отдельные объекты, так и композиции одинаково.

*What does this example do?*
Пример реализует класс Graphic, который может быть либо эллипсом,
либо композицией нескольких графических объектов.
Каждый графический объект может быть напечатан.

*Where is the pattern used practically?*
В графических редакторах фигура может быть простой или сложной.
Примером простой формы является линия, а сложной - прямоугольник,
состоящий из четырех линий. Поскольку у форм есть много общих операций,
таких как отображение формы на экране, и поскольку формы следуют
иерархии "часть-целое", паттерн Composite может быть использован
для обеспечения единообразной обработки всех форм в программе.

*References:*
https://en.wikipedia.org/wiki/Composite_pattern
https://infinitescript.com/2014/10/the-23-gang-of-three-design-patterns/

*TL;DR*
Описывает группу объектов, которая обрабатывается как один экземпляр.
"""

from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError("You should implement this!")


class CompositeGraphic(Graphic):
    def __init__(self) -> None:
        self.graphics: List[Graphic] = []

    def render(self) -> None:
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic: Graphic) -> None:
        self.graphics.append(graphic)

    def remove(self, graphic: Graphic) -> None:
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self) -> None:
        print(f"Ellipse: {self.name}")


def main():
    """
    >>> ellipse1 = Ellipse("1")
    >>> ellipse2 = Ellipse("2")
    >>> ellipse3 = Ellipse("3")
    >>> ellipse4 = Ellipse("4")

    >>> graphic1 = CompositeGraphic()
    >>> graphic2 = CompositeGraphic()

    >>> graphic1.add(ellipse1)
    >>> graphic1.add(ellipse2)
    >>> graphic1.add(ellipse3)
    >>> graphic2.add(ellipse4)

    >>> graphic = CompositeGraphic()

    >>> graphic.add(graphic1)
    >>> graphic.add(graphic2)

    >>> graphic.render()
    Ellipse: 1
    Ellipse: 2
    Ellipse: 3
    Ellipse: 4
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
