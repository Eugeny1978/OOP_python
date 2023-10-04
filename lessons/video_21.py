#21. Функция issubclass(). Наследование от встроенных типов и от object
# Все встронные Типы данных (python) - это Классы

class Geom:
    pass

class Line(Geom):
    pass

# Расширим встроенный Класс list
class VectorA(list):
    def __str__(self):
        return ' | '.join(map(str, self))

class VectorB(list):
    pass
#--- RUN ---------------------------------

# g1 = Geom()
# l1 = Line()
# print(g1, l1, sep=' || ')
# print(g1.__class__, l1.__class__, sep=' || ')
# print(issubclass(Line, Geom)) # Истина (Дочерний, Базовый Класс) # функция работает только с Классами
# print(issubclass(Geom, Line))
# print(issubclass(Geom, object))
# print(isinstance(l1, Geom)) # Аналогично предыдущ функции, только шире, распространяется и на Экзепляры
# print(issubclass(int, object))
# print(issubclass(list, object))

v1 = VectorA([1, 3, 7, 3, 8])
v2 = VectorB([1, 3, 7, 3, 8])
print(v1, type(v1), sep=' || ')
print(v2, type(v2), sep=' || ')