from dataclasses import dataclass, field, InitVar
from typing import Any


@dataclass
class Goods:
    uid: Any
    price: Any = None
    weight: Any = None

@dataclass
class Books(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0

# --- RUN ------------------------------------

b0 = Books(1)
print(b0) # Books(uid=1, price=0, weight=0, title='', author='') # обрати внимание на порядок следования Параметров

b1 = Books(2, 980, 78, 'Парсим на Python', 'Глобальный В. С.')
print(b1)
