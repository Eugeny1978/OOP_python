#26. Коллекция __slots__

import timeit
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

class Point2D:
    __slots__ = ('x', 'y') # Явно указываем, что локальные Св-ва могут быть только 'x' и 'y'
    # Остальных св-в - НЕТ в том числе и '__dict__'
    # Накладывает ограничения ТОЛЬКО на Локальные Св-ва Экземпляров.
    # на Атрибуты Класса ограничений нет
    # Также слотс - ускоряет работу с переменными
    MAX_COORD = 250
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

# --- RUN ---------------------------------------------
pt1 = Point(12, 25)
pt2 = Point2D(12, 25)
print(pt2.x, pt2.y)
# print(pt2.__dict__)
print(pt2.MAX_COORD)

# Сравним размеры Памяти, которые занимают объекты:
pt1_size = pt1.__sizeof__() + pt1.__dict__.__sizeof__()
pt2_size = pt2.__sizeof__()
print(f'Size {pt1}: {pt1_size}')
print(f'Size {pt2}: {pt2_size}')

# Скорость работы с данными
t1 = timeit.timeit(pt1.calc)
t2 = timeit.timeit(pt2.calc)
print(f' Time t1: {t1*10**3} || Time t2: {t2*10**3}')