"""
🌐 Что такое паттерн Состояние?

Паттерн Состояние – это способ организации кода, который позволяет объекту
изменять свое поведение в зависимости от внутреннего состояния.
Он основан на идее переноса состояний объекта в отдельные классы, которые называются состояниями.

🤔 Как это работает?

Представьте себе программу, которая имеет несколько состояний, например: "вкл.", "выкл."
и "режим ожидания". Вместо того чтобы вручную проверять текущее состояние и выполнять
соответствующие действия в разных местах программы, мы можем использовать паттерн Состояние.
Он позволяет нам определить отдельные классы для каждого состояния и делегировать
выполнение действий соответствующим классам.

👍 Как это помогает?

Использование паттерна Состояние делает код более понятным и поддерживаемым.
Каждое состояние имеет свой собственный класс, что позволяет избежать множества
условных операторов и дает возможность добавлять новые состояния без изменения существующего кода.
Это особенно полезно при работе с большими программами или системами.

🔥Участники паттерна

State: определяет интерфейс состояния.
Классы ConcreteStateA и ConcreteStateB - конкретные реализации состояний.
Context: представляет объект, поведение которого должно динамически изменяться
в соответствии с состоянием. Выполнение же конкретных действий делегируется объекту состояния.
💡 Заключение

Паттерн Состояние помогает нам реализовывать гибкое и удобное поведение объектов в программе.
Он позволяет нам легко добавлять новые состояния и контролировать их переходы.
Использование этого паттерна может значительно улучшить архитектуру вашего кода и сделать его более чистым и читаемым.
"""

from __future__ import annotations


class State:
    """Base state. This is to share functionality"""

    def scan(self) -> None:
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Scanning... Station is {self.stations[self.pos]} {self.name}")


class AmState(State):
    def __init__(self, radio: Radio) -> None:
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self) -> None:
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio: Radio) -> None:
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self) -> None:
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio:
    """A radio.     It has a scan button, and an AM/FM toggle switch."""

    def __init__(self) -> None:
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self) -> None:
        self.state.toggle_amfm()

    def scan(self) -> None:
        self.state.scan()


def main():
    """
    >>> radio = Radio()
    >>> actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    >>> actions *= 2

    >>> for action in actions:
    ...    action()
    Scanning... Station is 1380 AM
    Scanning... Station is 1510 AM
    Switching to FM
    Scanning... Station is 89.1 FM
    Scanning... Station is 103.9 FM
    Scanning... Station is 81.3 FM
    Scanning... Station is 89.1 FM
    Switching to AM
    Scanning... Station is 1250 AM
    Scanning... Station is 1380 AM
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
