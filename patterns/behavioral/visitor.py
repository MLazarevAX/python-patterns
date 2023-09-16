"""
http://peter-hoffmann.com/2010/extrinsic-visitor-pattern-python-inheritance.html
*TL;ДР Отделяет алгоритм от структуры объекта, с которым он работает.

Интересный рецепт можно найти в Брайан Джонс, Дэвид Бизли
«Кулинарная книга Python» (2013): - «8.21. Реализация шаблона посетителя» -
«8.22. Реализация шаблона посетителя без рекурсии»

*Примеры в экосистеме Python: - Python
ast.NodeVisitor: https://github.com/python/cpython/blob/master/Lib/ast.py#L250
который затем используется, например, в таких инструментах, как `pyflakes`.
 - Инструмент форматирования `Black` реализует свой собственный: https://github.com/ambv/black/blob/master/black.py#L71
"""


class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = "visit_" + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print("generic_visit " + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print("visit_B " + node.__class__.__name__)


def main():
    """
    >>> a, b, c = A(), B(), C()
    >>> visitor = Visitor()

    >>> visitor.visit(a)
    generic_visit A

    >>> visitor.visit(b)
    visit_B B

    >>> visitor.visit(c)
    visit_B C
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
