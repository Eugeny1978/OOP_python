#38. Введение в Python Data Classes (часть 2)
#  Функция field()
# repr - True/False - Использовать ли атрибут в методе __repr__ (по умолчанию True)
# compare - True/False - Использовать ли атрибут в при сравнении объектов (по умолчанию True)
# default - значение по умолчанию
# init - True/False - Использовать ли атрибут как Параметр при иницализации (по умолчанию True)
# default_factory - для использования Изменяемых Объеков (list, dict и др)  (см. video_37)


from dataclasses import dataclass, field, InitVar

class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x**2 + y**2 + z**2)**0.5 if calc_len else 0

# См параметры декоратора @dataclass
# @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
#            match_args=True, kw_only=False, slots=False, weakref_slot=False)
@dataclass
class VectorDate3D:
    x: int = field(repr=False) # НЕ использовать в методе __repr__
    y: int
    z: int = field(compare=False) # НЕ Использовать ли атрибут в при сравнении объектов
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0) # Определяю НЕ использовать как Параметр, НЕ использовать в методе __repr__

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

# --- RUN ----------------------------------------------------------

v1 = Vector3D(12, 15, 22)
v2 = VectorDate3D(12, 15, 22)
v3 = VectorDate3D(12, 15, 40)
print(v1.__dict__)
print(v2) # Не выведет x, тк не используем в методе __repr_
print(v2 == v3) # Сравнит только x, y
v4 = VectorDate3D(22, 33, 55, False)
print(v4)
