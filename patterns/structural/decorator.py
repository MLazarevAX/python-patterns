"""
*What is this pattern about?*
Паттерн Декоратор используется для динамического добавления новой функциональности
к объекту без изменения его реализации. Он отличается от наследования тем,
что новая функциональность добавляется только к этому конкретному объекту, а не ко всему подклассу.

*What does this example do?*
Этот пример показывает способ добавления опций форматирования
 (жирный и курсив) к тексту, добавляя соответствующие теги (<b> и <i>).
Кроме того, можно видеть, что декораторы могут быть применены один за другим,
так как исходный текст передается обертке для жирного текста,
которая в свою очередь передается обертке для курсива.

*Where is the pattern used practically?*
Фреймворк Grok использует декораторы для добавления функциональности к методам,
 таким как управление доступом или подписка на событие:
http://grok.zope.org/doc/current/reference/decorators.html

*References:*
https://sourcemaking.com/design_patterns/decorator

*TL;DR*
Добавляет поведение к объекту без изменения его класса.
"""


class TextTag:
    """Represents a base text tag"""

    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"


def main():
    """
    >>> simple_hello = TextTag("hello, world!")
    >>> special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    >>> print("before:", simple_hello.render())
    before: hello, world!

    >>> print("after:", special_hello.render())
    after: <i><b>hello, world!</b></i>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
