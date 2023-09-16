"""
*What is this pattern about?*
Этот паттерн направлен на минимизацию количества объектов, которые необходимы
 программе во время выполнения. Flyweight (Легковес) - это объект, используемый
  несколькими контекстами и неотличимый от объекта, который не является общим.

Состояние Flyweight не должно зависеть от его контекста, это называется
его внутренним состоянием. Разделение состояния объекта от контекста
объекта позволяет Flyweight быть общим.

*What does this example do?*
Приведенный ниже пример настраивает "пул объектов", который хранит
инициализированные объекты. Когда создается "Card" (Карта), он сначала проверяет,
существует ли уже такой объект, вместо создания нового. Это направлено
на уменьшение количества объектов, инициализированных программой.

*References:*
http://codesnipers.com/?q=python-flyweights
https://python-patterns.guide/gang-of-four/flyweight/

*Examples in Python ecosystem:*
https://docs.python.org/3/library/sys.html#sys.intern

*TL;DR*
Минимизирует использование памяти путем совместного использования данных с другими похожими объектами.
"""

import weakref


class Card:
    """The Flyweight"""

    # Could be a simple dict.
    # With WeakValueDictionary garbage collection can reclaim the object
    # when there are no other references to it.
    _pool: weakref.WeakValueDictionary = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        # If the object exists in the pool - just return it
        obj = cls._pool.get(value + suit)
        # otherwise - create new one (and add it to the pool)
        if obj is None:
            obj = object.__new__(Card)
            cls._pool[value + suit] = obj
            # This row does the part we usually see in `__init__`
            obj.value, obj.suit = value, suit
        return obj

    # If you uncomment `__init__` and comment-out `__new__` -
    #   Card becomes normal (non-flyweight).
    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return f"<Card: {self.value}{self.suit}>"


def main():
    """
    >>> c1 = Card('9', 'h')
    >>> c2 = Card('9', 'h')
    >>> c1, c2
    (<Card: 9h>, <Card: 9h>)
    >>> c1 == c2
    True
    >>> c1 is c2
    True

    >>> c1.new_attr = 'temp'
    >>> c3 = Card('9', 'h')
    >>> hasattr(c3, 'new_attr')
    True

    >>> Card._pool.clear()
    >>> c4 = Card('9', 'h')
    >>> hasattr(c4, 'new_attr')
    False
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
