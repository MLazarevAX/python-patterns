"""*О чем этот шаблон?
Фабрика - это объект для создания других объектов.

*Что делает этот пример?
Код показывает способ локализации слов на двух языках:
 английском и греческом. "get_localizer" - это фабричная функция,
которая создает локализатор в зависимости от выбранного языка.
Объект локализатора будет экземпляром другого класса в соответствии с выбранным языком.
Однако основной код не должен беспокоиться о том, какой локализатор будет создан,
поскольку метод "localize" будет вызван таким же образом независимо от выбранного языка.

*Где практически можно использовать этот шаблон?
Шаблон Фабричного метода можно увидеть в популярном веб-фреймворке Django:
 https://docs.djangoproject.com/en/4.0/topics/forms/formsets/.
Например, различные типы форм создаются с использованием formset_factory.

*Ссылки:
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*Кратко
Создает объекты, не указывая точный класс.
"""
from typing import Dict
from typing import Protocol
from typing import Type


class Localizer(Protocol):
    def localize(self, msg: str) -> str:
        pass


class GreekLocalizer:
    """A simple localizer a la gettext"""

    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> Localizer:
    """Factory"""
    localizers: Dict[str, Type[Localizer]] = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }

    return localizers[language]()


def main():
    """
    # Create our localizers
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")

    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
