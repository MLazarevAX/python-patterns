"""
*What is this pattern about?
Прокси используется в случаях, когда вы хотите добавить функциональность
к классу без изменения его интерфейса. Основной класс называется
"Реальным объектом". Клиент должен использовать прокси или
реальный объект без изменения кода, поэтому оба должны иметь одинаковый интерфейс.
Примерами использования паттерна "прокси" являются логирование
и управление доступом к реальному объекту.

*References:
https://refactoring.guru/design-patterns/proxy/python/example
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Fronting.html

*TL;DR
Добавляет функциональность или логику (например, логирование, кэширование, авторизацию)
 к ресурсу без изменения его интерфейса.
"""

from typing import Union


class Subject:
    """
    As mentioned in the document, interfaces of both RealSubject and Proxy should
    be the same, because the client should be able to use RealSubject or Proxy with
    no code change.

    Not all times this interface is necessary. The point is the client should be
    able to use RealSubject or Proxy interchangeably with no change in code.
    """

    def do_the_job(self, user: str) -> None:
        raise NotImplementedError()


class RealSubject(Subject):
    """
    This is the main job doer. External services like payment gateways can be a
    good example.
    """

    def do_the_job(self, user: str) -> None:
        print(f"I am doing the job for {user}")


class Proxy(Subject):
    def __init__(self) -> None:
        self._real_subject = RealSubject()

    def do_the_job(self, user: str) -> None:
        """
        logging and controlling access are some examples of proxy usages.
        """

        print(f"[log] Doing the job for {user} is requested.")

        if user == "admin":
            self._real_subject.do_the_job(user)
        else:
            print("[log] I can do the job just for `admins`.")


def client(job_doer: Union[RealSubject, Proxy], user: str) -> None:
    job_doer.do_the_job(user)


def main():
    """
    >>> proxy = Proxy()

    >>> real_subject = RealSubject()

    >>> client(proxy, 'admin')
    [log] Doing the job for admin is requested.
    I am doing the job for admin

    >>> client(proxy, 'anonymous')
    [log] Doing the job for anonymous is requested.
    [log] I can do the job just for `admins`.

    >>> client(real_subject, 'admin')
    I am doing the job for admin

    >>> client(real_subject, 'anonymous')
    I am doing the job for anonymous
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
