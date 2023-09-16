Список паттернов проектирования и идиом в Python.

__Порождающие паттерны__:

| Паттерн | Описание |
|:-------:| ----------- |
| [abstract_factory](patterns/creational/abstract_factory.py) | использует обобщенную функцию с конкретными фабриками |
| [borg](patterns/creational/monostate.py) | синглтон с общим состоянием между экземплярами |
| [builder](patterns/creational/builder.py) | вместо использования нескольких конструкторов, объект-строитель принимает параметры и возвращает созданные объекты |
| [factory](patterns/creational/factory.py) | делегирует специализированную функцию/метод для создания экземпляров |
| [lazy_evaluation](patterns/creational/lazy_evaluation.py) | шаблон "ленивого вычисления" свойств в Python |
| [pool](patterns/creational/pool.py) | предварительно создает и поддерживает группу экземпляров одного типа |
| [prototype](patterns/creational/prototype.py) | использует фабрику и клонирование прототипа для создания новых экземпляров (если создание дорого) |

__Структурные паттерны__:

| Паттерн | Описание |
|:-------:| ----------- |
| [3-tier](patterns/structural/3-tier.py) | разделение данных <-> бизнес-логика <-> представление (строгие отношения) |
| [adapter](patterns/structural/adapter.py) | адаптирует один интерфейс к другому с использованием белого списка |
| [bridge](patterns/structural/bridge.py) | посредник между клиентом и поставщиком для смягчения изменений интерфейса |
| [composite](patterns/structural/composite.py) | позволяет клиентам обращаться к отдельным объектам и композициям одинаково |
| [decorator](patterns/structural/decorator.py) | оборачивает функциональность другой функциональностью для изменения результатов |
| [facade](patterns/structural/facade.py) | использует один класс в качестве API к нескольким другим |
| [flyweight](patterns/structural/flyweight.py) | прозрачно повторно использует существующие экземпляры объектов с похожим/одинаковым состоянием |
| [front_controller](patterns/structural/front_controller.py) | один обработчик запросов, поступающих в приложение |
| [mvc](patterns/structural/mvc.py) | модель <-> представление <-> контроллер (нестрогие отношения) |
| [proxy](patterns/structural/proxy.py) | объект направляет операции на что-то другое |

__Поведенческие паттерны__:

| Паттерн | Описание |
|:-------:| ----------- |
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility.py) | применяет цепочку последовательных обработчиков для обработки данных |
| [catalog](patterns/behavioral/catalog.py) | общие методы будут вызывать различные специализированные методы на основе параметра конструкции |
| [chaining_method](patterns/behavioral/chaining_method.py) | продолжает обратный вызов следующего метода объекта |
| [command](patterns/behavioral/command.py) | объединяет команду и аргументы для последующего вызова |
| [iterator](patterns/behavioral/iterator.py) | обход контейнера и доступ к элементам контейнера |
| [iterator](patterns/behavioral/iterator_alt.py) (альтернативная реализация) | обход контейнера и доступ к элементам контейнера |
| [mediator](patterns/behavioral/mediator.py) | объект, который умеет соединять другие объекты и действовать как прокси |
| [memento](patterns/behavioral/memento.py) | создает непрозрачный маркер, который можно использовать для возврата к предыдущему состоянию |
| [observer](patterns/behavioral/observer.py) | предоставляет обратный вызов для уведомления о событиях/изменениях данных |
| [publish_subscribe](patterns/behavioral/publish_subscribe.py) | источник рассылает события/данные 0+ зарегистрированным слушателям |
| [registry](patterns/behavioral/registry.py) | отслеживает все подклассы данного класса |
| [specification](patterns/behavioral/specification.py) | бизнес-правила можно повторно комбинировать, объединяя их логическими операциями |
| [state](patterns/behavioral/state.py) | логика организована в нескольких потенциальных состояниях и следующем состоянии, в которое можно перейти |
| [strategy](patterns/behavioral/strategy.py) | выборочные операции над теми же данными |
| [template](patterns/behavioral/template.py) | объект налагает структуру, но принимает компоненты как плагины |
| [visitor](patterns/behavioral/visitor.py) | вызывает обратный вызов для всех элементов коллекции |

__Паттерны проектирования для обеспечения тестируемости__:

| Паттерн | Описание |
|:-------:| ----------- |
| [dependency_injection](patterns/dependency_injection.py) | 3 варианта внедрения зависимостей |

__Основные паттерны__:

| Паттерн | Описание                                                             |
|:-------:|----------------------------------------------------------------------|
| [delegation_pattern](patterns/fundamental/delegation_pattern.py) | объект обрабатывает запрос, делегируя его второму объекту (делегату) |

__Другие паттерны__:

| Паттерн | Описание |
|:-------:| ----------- |
| [blackboard](patterns/other/blackboard.py) | архитектурная модель, сбор различных знаний подсистем для создания решения, подход ИИ - не паттерн "банда четырех" |
| [graph_search](patterns/other/graph_search.py) | алгоритмы работы с графами - не паттерн "банда четырех" |
| [hsm](patterns/other/hsm/hsm.py) | иерархическая конечная автоматная машина - не паттерн "банда четырех" |

## Видеоматериалы
[Паттерны проектирования на Python от Петера Ульриха](https://www.youtube.com/watch?v=bsyjSW46TDg)

[Себастьян Бучински - Почему вам не нужны паттерны проектирования в Python?](https://www.youtube.com/watch?v=G5OeYHCJuv0)

[Вам это не нужно!](https://www.youtube.com/watch?v=imW-trt0i9I)

[Подключаемые библиотеки через паттерны проектирования](https://www.youtube.com/watch?v=PfgEU3W0kyU)
