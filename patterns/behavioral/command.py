"""
Паттерн "Команда" (Command) разрывает связь между объектом, вызывающим операцию,
и объектом, знающим, как ее выполнить. Хорошим примером являются пункты меню.
У вас есть меню, в котором много элементов.
Каждый элемент отвечает за выполнение какой-то специфической операции, и вы хотите,
чтобы ваш элемент меню просто вызывал метод `execute`, когда его нажимают.
Для этого вы создаете объект команды с методом `execute` для каждого
элемента меню и передаете его.

В данном примере у нас есть меню, содержащее два элемента. Каждый элемент
принимает имя файла: один скрывает файл, а другой удаляет его. Оба элемента
имеют опцию отмены действия. Каждый элемент представлен классом `MenuItem`,
который принимает соответствующую команду и выполняет ее метод `execute`,
когда элемент меню нажимается.

Вкратце, паттерн "Команда" представляет объектно-ориентированный способ
реализации функций обратного вызова.

Пример в экосистеме Python: HttpRequest в Django (без метода `execute`):
https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""

from typing import List, Union


class HideFileCommand:
    """
    A command to hide a file given its name
    """

    def __init__(self) -> None:
        # an array of files hidden, to undo them as needed
        self._hidden_files: List[str] = []

    def execute(self, filename: str) -> None:
        print(f"hiding {filename}")
        self._hidden_files.append(filename)

    def undo(self) -> None:
        filename = self._hidden_files.pop()
        print(f"un-hiding {filename}")


class DeleteFileCommand:
    """
    A command to delete a file given its name
    """

    def __init__(self) -> None:
        # an array of deleted files, to undo them as needed
        self._deleted_files: List[str] = []

    def execute(self, filename: str) -> None:
        print(f"deleting {filename}")
        self._deleted_files.append(filename)

    def undo(self) -> None:
        filename = self._deleted_files.pop()
        print(f"restoring {filename}")


class MenuItem:
    """
    The invoker class. Here it is items in a menu.
    """

    def __init__(self, command: Union[HideFileCommand, DeleteFileCommand]) -> None:
        self._command = command

    def on_do_press(self, filename: str) -> None:
        self._command.execute(filename)

    def on_undo_press(self) -> None:
        self._command.undo()


def main():
    """
    >>> item1 = MenuItem(DeleteFileCommand())

    >>> item2 = MenuItem(HideFileCommand())

    # create a file named `test-file` to work with
    >>> test_file_name = 'test-file'

    # deleting `test-file`
    >>> item1.on_do_press(test_file_name)
    deleting test-file

    # restoring `test-file`
    >>> item1.on_undo_press()
    restoring test-file

    # hiding `test-file`
    >>> item2.on_do_press(test_file_name)
    hiding test-file

    # un-hiding `test-file`
    >>> item2.on_undo_press()
    un-hiding test-file
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
