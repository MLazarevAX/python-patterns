"""
*О чем этот шаблон?
Этот шаблон используется, когда создание объекта затратно (и они создаются часто),
 но только несколько из них используются одновременно. С помощью пула мы можем управлять
 имеющимися экземплярами, кэшируя их. Теперь возможно пропустить затратное создание объекта,
 если в пуле есть доступный.
Пул позволяет "взять" неактивный объект и затем вернуть его.
Если нет доступных объектов, то пул создает новый, чтобы предоставить его без ожидания.

*Что делает этот пример?
В этом примере используется queue.Queue для создания пула (обернутого в пользовательский
 объект ObjectPool для использования с оператором with) и заполняется строками.
Как мы видим, первый объект строки, помещенный в "yam", ИСПОЛЬЗУЕТСЯ с помощью оператора with.
Но поскольку он возвращается обратно в пул после этого, его можно повторно
использовать при явном вызове sample_queue.get().
То же самое происходит с "sam", когда ObjectPool, созданный внутри функции,
удаляется (сборщиком мусора), и объект возвращается.

*Где это практически используется?

*Ссылки:
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool

*Кратко
Сохраняет набор инициализированных объектов, готовых к использованию."""


class ObjectPool:
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    """
    >>> import queue

    >>> def test_object(queue):
    ...    pool = ObjectPool(queue, True)
    ...    print('Inside func: {}'.format(pool.item))

    >>> sample_queue = queue.Queue()

    >>> sample_queue.put('yam')
    >>> with ObjectPool(sample_queue) as obj:
    ...    print('Inside with: {}'.format(obj))
    Inside with: yam

    >>> print('Outside with: {}'.format(sample_queue.get()))
    Outside with: yam

    >>> sample_queue.put('sam')
    >>> test_object(sample_queue)
    Inside func: sam

    >>> print('Outside func: {}'.format(sample_queue.get()))
    Outside func: sam

    if not sample_queue.empty():
        print(sample_queue.get())
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
