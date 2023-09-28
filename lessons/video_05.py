#5. Методы класса (classmethod) и статические методы (staticmethod). Декораторы

# classmethod - Может работать ТОЛЬКО с Атрибутами Класса, но не может обращаться с атрибутами Экзепляра Класса

# staticmethod - не имеет доступа ни к Атрибутам Класса ни к Атрибутам Экземляра - те Независимый метод
# Фактически это функция, объявленная ВНУТРИ самого класса

# Прописывать Имя Класса внутри самого Класса можно - НО НЕ рекомендуется

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.validate(x): # Не рекомендуется: Vector.validate(x)
            self.x = x
        if self.validate(y):
            self.y = y
        print(f'Норма Вектора: {self.norm2(self.x, self.y)}')

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        res = x**2 + y**2
        return res


v = Vector(5, 8)
res1 = v.get_coords()
res2 = Vector.get_coords(v)
print(f'Координаты Экземляра "v": {res1} | через обращение от этого Экземляра')
print(f'Координаты Экземляра "v": {res2} | через обращение от Класса')

# При вызове classmethod автоматически 1м параметром Сам Класс
# Сравни с 24 строкой вызов обычного метода
print(Vector.validate(43))
print(Vector.validate(189))

v1 = Vector(10, 40)
v2 = Vector(110, 17)
v3 = Vector(40, 170)
v4 = Vector(740, 270)
print(f'Координаты v1: {v1.get_coords()}')
print(f'Координаты v2: {v2.get_coords()}')
print(f'Координаты v3: {v3.get_coords()}')
print(f'Координаты v4: {v4.get_coords()}')
