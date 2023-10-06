#37. Введение в Python Data Classes (часть 1)
# Для "Информативных" Классов часто приходится делать так: (см. Пример 1)

from dataclasses import dataclass, field
from pprint import pprint


# Пример 1
class Thing:
    def __init__(self, name, weight, price=1000, dims=[]):
        self.name = name
        self.weght = weight
        self.price = price
        self.dims = dims # В случае list (Списка) -эти Значения будут ОБЩИМИ для всех объектов данного Класса см. t2, t3 ниже

    # Для информативности вывода информации
    def __repr__(self):
        return f'Thing: {self.__dict__}'

# c v. Python 3.7+ возможно это сделать так (см. Пример 2)
@dataclass
class ThingData:
    name: str # анотация обязательно иначе Декоратор не отработает как нам надо
    weight: int
    price: float = 1000 # 1000 значение по умолчанию
    # dims: list = [] # так нельзя - тк список - это изменяемый объект. см также t2, t3
    dims: list = field(default_factory=list) # td5, td6




# --- RUN -------------------------------------

t1 = Thing('Учебник по Python', 120, 1450)
print(t1)
td1 = ThingData('Учебник по Java', 105, 1350)
print(td1)
# Перебрал Данные класса
# for key, value in td1.__dict__.items():
#     print(f'{key}: {value}')
# pprint(ThingData.__dict__) # Вывод Атрибутов
td2 = ThingData('Учебник по C#', 125, 1560)
td3 = ThingData('Учебник по C#', 125, 1560)
print(td2)
print(td1 == td2) # Сравнивает именно Кортежи Данных тк для Классов Данных переопределен метод __eq__
print(td3 == td2) # (sname, weight, price) == (name, weight, price)
td4 = ThingData('Самоучитель Python ООП', 125)
print(td4)
t2 = Thing('Занимательная Математика', 85, 870)
t2.dims.append(10)
print(t2)
t3 = Thing('Занимательная Физика', 95, 890)
print(t3)
td5 = ThingData('Python: Parsing', 78, 1200)
td5.dims.append(12)
print(td5)
td6 = ThingData('Python: Telegram Bots', 98, 965)
print(td6)
