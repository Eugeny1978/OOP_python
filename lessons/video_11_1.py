#11. Дескрипторы (data descriptor и non-data descriptor)

# Пример Задачи.
# Реализация БЕЗ Дескрипторов (иммем Функциональное дублирование)
# В данном случае набор из 3х одинаковых геттеров и сеттеров.

class Point3D:

    def __init__(self, x, y, z):
        # self._x = x
        # self._y = y
        # self._z = z
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координаты должны быть заданы ЦЕЛЫМИ Числами')

    @property #getter
    def x(self):
        return  self._x
    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property #getter
    def y(self):
        return  self._y
    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property #getter
    def z(self):
        return  self._z
    @y.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord

# ---- RUN ----------------------------------------------------------------------

point = Point3D(10, 22, 6)
print(point.__dict__)