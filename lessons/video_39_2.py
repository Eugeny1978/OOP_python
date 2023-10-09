from dataclasses import dataclass, field, InitVar
from typing import Any

# В этом Классе будут содержаться все необходимы Прикладные Методы для Класса Goods
class GoodsMethodsFactory:
    @staticmethod
    def get_init_meashure():
        return list[0, 0, 0]


@dataclass
class Goods:
    current_uid = 0 # не аннотируем чтобы декораторо @dataclass его проигнорировал
    uid: int = field(init=False) # исключил из инициализации
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: __post_init__')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Books(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    meashure: list = field(default_factory=GoodsMethodsFactory.get_init_meashure)
    # Из текущего класса вызывать такие методы не получится


    def __post_init__(self):
        super().__post_init__() # если не припишу - выдаст ошибку
        print('Books: __post_init__')

# --- RUN ------------------------------------

b1 = Books(980, 78, 'Парсим на Python', 'Глобальный В. С.')
print(b1)
b2 = Books(1250, 105, 'Python OOP', 'Балакирев С. М.', [200, 100, 2])
print(b2)
b3 = Books(1250, 105, 'Python Telegram', 'Иванов В. Б.', [200, 80, 1])
print(b3)