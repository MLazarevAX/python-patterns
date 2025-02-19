from typing import Dict


class RegistryHolder(type):
    REGISTRY: Dict[str, "RegistryHolder"] = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        """
            Here the name of the class is used as key but it could be any class
            parameter.
        """
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    """
    Любой класс, который будет наследоваться от BaseRegisteredClass,
    будет включен в dict RegistryHolder.REGISTRY, где ключом является
    имя класса и связанное с ним значение, то есть сам класс.
    """


def main():
    """
    Before subclassing
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass']

    >>> class ClassRegistree(BaseRegisteredClass):
    ...    def __init__(self, *args, **kwargs):
    ...        pass

    After subclassing
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass', 'ClassRegistree']
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
