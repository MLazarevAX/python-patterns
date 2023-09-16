"""
*О чем этот шаблон?
Шаблон Борга (также известный как шаблон Monostate) представляет собой способ реализации поведения синглтона,
 но вместо одного экземпляра класса существует несколько экземпляров, которые разделяют одно и то же состояние.
Другими словами, основное внимание уделяется совместному использованию состояния,
  а не совместному использованию идентичности экземпляра.

*Что делает этот пример?
Для понимания реализации этого шаблона на Python важно знать, что в Python атрибуты экземпляра хранятся
 в словаре атрибутов, названном dict. Обычно у каждого экземпляра будет свой собственный словарь,
 но шаблон Борга изменяет это так, чтобы все экземпляры имели один и тот же словарь.
В этом примере атрибут __shared_state будет словарем, который разделяется между всеми экземплярами,
и это обеспечивается путем присвоения __shared_state переменной dict при инициализации нового экземпляра
(то есть в методе init). Другие атрибуты обычно добавляются в словарь атрибутов экземпляра, но,
поскольку сам словарь атрибутов разделяется (то есть __shared_state), все остальные атрибуты также будут разделяться.

*Где практически используется этот шаблон?
Совместное использование состояния полезно в приложениях, таких как управление соединениями с базой данных:
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py

*Ссылки:

    https://fkromer.github.io/python-pattern-references/design/#singleton
    https://learning.oreilly.com/library/view/python-cookbook/0596001673/ch05s23.html
    http://www.aleax.it/5ep.html

*Кратко
Предоставляет поведение, подобное синглтону, разделяя состояние между экземплярами.
"""
from typing import Dict


class Borg:
    _shared_state: Dict[str, str] = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state: str = None) -> None:
        super().__init__()
        if state:
            self.state = state
        else:
            # initiate the first instance with default state
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self) -> str:
        return self.state


def main():
    """
    >>> rm1 = YourBorg()
    >>> rm2 = YourBorg()

    >>> rm1.state = 'Idle'
    >>> rm2.state = 'Running'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Running
    >>> print('rm2: {0}'.format(rm2))
    rm2: Running

    # When the `state` attribute is modified from instance `rm2`,
    # the value of `state` in instance `rm1` also changes
    >>> rm2.state = 'Zombie'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie

    # Even though `rm1` and `rm2` share attributes, the instances are not the same
    >>> rm1 is rm2
    False

    # New instances also get the same shared state
    >>> rm3 = YourBorg()

    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie
    >>> print('rm3: {0}'.format(rm3))
    rm3: Zombie

    # A new instance can explicitly change the state during creation
    >>> rm4 = YourBorg('Running')

    >>> print('rm4: {0}'.format(rm4))
    rm4: Running

    # Existing instances reflect that change as well
    >>> print('rm3: {0}'.format(rm3))
    rm3: Running
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
