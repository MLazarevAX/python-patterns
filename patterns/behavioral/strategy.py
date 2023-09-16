"""
Паттерн Стратегия

Стратегия — это паттерн проектирования, который позволяет определить набор алгоритмов и
заменять их друг на друга во время выполнения программы. Это очень полезно,
когда у нас есть несколько способов решения одной и той же задачи, и мы хотим иметь
возможность выбрать наиболее подходящий способ в зависимости от ситуации.


Как он работает?
Представьте, что у вас есть приложение для оплаты и вы хотите предоставить
различные методы оплаты: кредитные карты, электронные кошельки, банковские трансферы.
Вместо того, чтобы иметь монолитный код, который работает со всеми этими способами,
мы можем использовать паттерн Стратегия. Мы определяем интерфейс "Оплата" и реализуем
несколько классов, соответствующих нашим способам оплаты. Затем мы можем легко
переключаться между ними во время выполнения приложения.


Преимущества использования паттерна Стратегия включают:
✅ Гибкость: мы можем легко добавлять новые стратегии или изменять существующие
без влияния на другие части системы.

✅ Читаемость и понимание кода: разделение алгоритмов на отдельные классы делает
код более читаемым и позволяет лучше понять, как работает каждый алгоритм отдельно.

✅ Тестируемость: мы можем легко тестировать каждую стратегию отдельно,
не затрагивая другие части системы.

✅ Удобное многопоточное использование: каждая стратегия может работать независимо,
что упрощает разработку многопоточных приложений.

Участники
- Интерфейс Strategy, который определяет метод algorithm(). Это общий интерфейс
для всех реализующих его алгоритмов. Вместо интерфейса здесь также можно было бы использовать абстрактный класс.

- Классы ConcreteStrategyA и ConcreteStrategyB, которые реализуют интерфейс Strategy,
предоставляя свою версию метода algorithm(). Подобных классов-реализаций может быть множество.

- Класс Context хранит ссылку на объект Strategy и связан с интерфейсом Strategy отношением агрегации.


В заключение
Паттерн Стратегия — мощный инструмент, который помогает нам организовать
и управлять различными алгоритмами в программе. Он позволяет создавать более гибкую
и расширяемую систему, а также повышает читаемость и переиспользуемость кода.
*TL;DR
Enables selecting an algorithm at runtime.
"""


from __future__ import annotations

from typing import Callable


class DiscountStrategyValidator:  # Descriptor class for check perform
    @staticmethod
    def validate(obj: Order, value: Callable) -> bool:
        try:
            if obj.price - value(obj) < 0:
                raise ValueError(
                    f"Discount cannot be applied due to negative price resulting. {value.__name__}"
                )
        except ValueError as ex:
            print(str(ex))
            return False
        else:
            return True

    def __set_name__(self, owner, name: str) -> None:
        self.private_name = f"_{name}"

    def __set__(self, obj: Order, value: Callable = None) -> None:
        if value and self.validate(obj, value):
            setattr(obj, self.private_name, value)
        else:
            setattr(obj, self.private_name, None)

    def __get__(self, obj: object, objtype: type = None):
        return getattr(obj, self.private_name)


class Order:
    discount_strategy = DiscountStrategyValidator()

    def __init__(self, price: float, discount_strategy: Callable = None) -> None:
        self.price: float = price
        self.discount_strategy = discount_strategy

    def apply_discount(self) -> float:
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self) -> str:
        return f"<Order price: {self.price} with discount strategy: {getattr(self.discount_strategy,'__name__',None)}>"


def ten_percent_discount(order: Order) -> float:
    return order.price * 0.10


def on_sale_discount(order: Order) -> float:
    return order.price * 0.25 + 20


def main():
    """
    >>> order = Order(100, discount_strategy=ten_percent_discount)
    >>> print(order)
    <Order price: 100 with discount strategy: ten_percent_discount>
    >>> print(order.apply_discount())
    90.0
    >>> order = Order(100, discount_strategy=on_sale_discount)
    >>> print(order)
    <Order price: 100 with discount strategy: on_sale_discount>
    >>> print(order.apply_discount())
    55.0
    >>> order = Order(10, discount_strategy=on_sale_discount)
    Discount cannot be applied due to negative price resulting. on_sale_discount
    >>> print(order)
    <Order price: 10 with discount strategy: None>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
