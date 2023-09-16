"""
*О чем этот шаблон?
Этот шаблон направлен на уменьшение числа классов, необходимых для приложения.
Вместо того чтобы полагаться на подклассы, он создает объекты путем
копирования прототипного экземпляра во время выполнения.

Это полезно, так как это упрощает создание новых видов объектов, когда
экземпляры класса имеют всего несколько различных комбинаций состояния,
и когда создание экземпляров затратно.

*Что делает этот пример?
Когда количество прототипов в приложении может меняться, полезно иметь Диспетчера
(также известного как Реестр или Менеджер). Это позволяет клиентам запрашивать
у Диспетчера прототип перед клонированием нового экземпляра.

Ниже предоставлен пример такого Диспетчера, который содержит
три копии прототипа: 'default', 'objecta' и 'objectb'.

*Кратко
Создает новые экземпляры объектов путем клонирования прототипа."""
from __future__ import annotations

from typing import Any


class Prototype:
    def __init__(self, value: str = "default", **attrs: Any) -> None:
        self.value = value
        self.__dict__.update(attrs)

    def clone(self, **attrs: Any) -> Prototype:
        """Клонировать прототип и обновить словарь внутренних атрибутов."""
        # Python in Practice, Mark Summerfield
        # copy.deepcopy Может использоваться вместо следующей строки.
        obj = self.__class__(**self.__dict__)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self) -> dict[str, Prototype]:
        """Get all objects"""
        return self._objects

    def register_object(self, name: str, obj: Prototype) -> None:
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        """Unregister an object"""
        del self._objects[name]


def main() -> None:
    """
    >>> dispatcher = PrototypeDispatcher()
    >>> prototype = Prototype()

    >>> d = prototype.clone()
    >>> a = prototype.clone(value='a-value', category='a')
    >>> b = a.clone(value='b-value', is_checked=True)
    >>> dispatcher.register_object('objecta', a)
    >>> dispatcher.register_object('objectb', b)
    >>> dispatcher.register_object('default', d)

    >>> [{n: p.value} for n, p in dispatcher.get_objects().items()]
    [{'objecta': 'a-value'}, {'objectb': 'b-value'}, {'default': 'default'}]

    >>> print(b.category, b.is_checked)
    a True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
