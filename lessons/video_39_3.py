#39. Python Data Classes при наследовании
# Альтернативный метод создания Дата Класса через Функцию: make_dataclass
# Используется в случаях когдав необходимо создать класс в процессе выполнения Программы
# Иначе намного удобнее объявлять класс предыдущим методом (см. vodeo 37 - 39).

# make_dataclass()
# (cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False,
# unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False):

# cls_name - Название (имя) Дата Класса
# fields - Поля (локальные атрибуты) объектов Класса
# * - Произвольный Набор Позиционных Аргументов
# bases - Список Базовых Классов
# namespace - Словарь для определения Атрибутов самого класса (так можно определять методы класса)
# Добавляются спец методы как и в случ создания через Data Class

from dataclasses import make_dataclass, field

class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed

# С помощью Функции создаем класс аналогичный классу Car (см выше)
CarDate = make_dataclass('CarDate',
                         [('model', str), 'max_speed', ('price', float, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed} )

# --- RUN ------------------------------------------

c1 = CarDate('Volvo', 260, 4500000)
print(c1)
print(c1.get_max_speed())