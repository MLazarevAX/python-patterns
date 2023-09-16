"""
Паттерн "Цепочка обязанностей" (Chain of Responsibility) - это
объектно-ориентированная версия идиомы `if ... elif ... elif ... else ...`,
с тем преимуществом, что блоки условие-действие могут быть
динамически пересматриваемы и переконфигурируемы во время выполнения.

Этот паттерн стремится разрывать связи между отправителями запроса и
их получателями, позволяя запросу проходить через цепочку получателей
до тех пор, пока он не будет обработан.

Получатель запроса в простой форме хранит ссылку на одного последователя.
Вариацией является то, что некоторые получатели могут отправлять запросы
в нескольких направлениях, образуя "дерево обязанностей".

Вкратце, паттерн "Цепочка обязанностей" позволяет запросу
проходить через цепочку получателей, пока он не будет обработан.
"""

from abc import ABC, abstractmethod
from typing import Optional, Tuple


class Handler(ABC):
    def __init__(self, successor: Optional["Handler"] = None):
        self.successor = successor

    def handle(self, request: int) -> None:
        """
        Handle request and stop.
        If can't - call next handler in chain.

        As an alternative you might even in case of success
        call the next handler.
        """
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abstractmethod
    def check_range(self, request: int) -> Optional[bool]:
        """Compare passed value to predefined interval"""


class ConcreteHandler0(Handler):
    """Each handler can be different.
    Be simple and static...
    """

    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        if 0 <= request < 10:
            print(f"request {request} handled in handler 0")
            return True
        return None


class ConcreteHandler1(Handler):
    """... With it's own internal state"""

    start, end = 10, 20

    def check_range(self, request: int) -> Optional[bool]:
        if self.start <= request < self.end:
            print(f"request {request} handled in handler 1")
            return True
        return None


class ConcreteHandler2(Handler):
    """... With helper methods."""

    def check_range(self, request: int) -> Optional[bool]:
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print(f"request {request} handled in handler 2")
            return True
        return None

    @staticmethod
    def get_interval_from_db() -> Tuple[int, int]:
        return (20, 30)


class FallbackHandler(Handler):
    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        print(f"end of chain, no handler for {request}")
        return False


def main():
    """
    >>> h0 = ConcreteHandler0()
    >>> h1 = ConcreteHandler1()
    >>> h2 = ConcreteHandler2(FallbackHandler())
    >>> h0.successor = h1
    >>> h1.successor = h2

    >>> requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    >>> for request in requests:
    ...     h0.handle(request)
    request 2 handled in handler 0
    request 5 handled in handler 0
    request 14 handled in handler 1
    request 22 handled in handler 2
    request 18 handled in handler 1
    request 3 handled in handler 0
    end of chain, no handler for 35
    request 27 handled in handler 2
    request 20 handled in handler 2
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
