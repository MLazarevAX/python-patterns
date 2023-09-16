"""
*What is this pattern about?*
Паттерн Фасад представляет собой способ предоставления более простого унифицированного
интерфейса к более сложной системе. Он обеспечивает более простой способ
доступа к функциям базовой системы, предоставляя единую точку входа.
Такой вид абстракции встречается во многих реальных ситуациях.
Например, мы можем включить компьютер, просто нажав кнопку, но, фактически,
при этом выполняется множество процедур и операций
(например, загрузка программ с диска в память). В этом случае кнопка служит
унифицированным интерфейсом ко всем базовым процедурам включения компьютера.

*Where is the pattern used practically?*
Этот паттерн можно увидеть в стандартной библиотеке Python, когда мы
используем функцию isdir. Несмотря на то, что пользователь просто использует эту функцию,
чтобы узнать, является ли путь каталогом, система выполняет несколько операций
и вызывает другие модули (например, os.stat), чтобы дать результат.

*References:*
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade

*TL;DR*
Предоставляет более простой унифицированный интерфейс к сложной системе.
"""


# Complex computer parts
class CPU:
    """
    Simple CPU representation.
    """

    def freeze(self) -> None:
        print("Freezing processor.")

    def jump(self, position: str) -> None:
        print("Jumping to:", position)

    def execute(self) -> None:
        print("Executing.")


class Memory:
    """
    Simple memory representation.
    """

    def load(self, position: str, data: str) -> None:
        print(f"Loading from {position} data: '{data}'.")


class SolidStateDrive:
    """
    Simple solid state drive representation.
    """

    def read(self, lba: str, size: str) -> str:
        return f"Some data from sector {lba} with size {size}"


class ComputerFacade:
    """
    Represents a facade for various computer parts.
    """

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
    Jumping to: 0x00
    Executing.
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
