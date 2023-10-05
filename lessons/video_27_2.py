#27. Как работает __slots__ с property и при наследовании

# Как отрабатывает при наследовании Классов

class Point:
    MAX_COORD = 250
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    __slots__ = ('x', 'y')
    MAX_COORD = 250
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    # Не наследует коллекцию __slots__ и можно создавать любые локальные переменные
    # также обрати внимание, тк в Базовом класчсе нет __dict__, то и локально тоже нет этих Атрибутов
    # __slots__ = () # Если так пропишем - у нас все равно останутся разрешенные св-ва x, y
    # __slots__ = 'z', # чтобы добавить разрешенную обязательно в виде кортежа! (см запятую после 'z')
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

class PointD(Point):
    # Дочерний Класс от класса где нет коллекции __slots__
     def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


# --- RUN --------------------------------------

pt1 = Point3D(44, 55, 77)
print(pt1.__dict__)
print(f'x: {pt1.x} || y: {pt1.y} || z: {pt1.z} || MAX_COORD: {pt1.MAX_COORD}')
print('\n')
pt2 = PointD(11, 22, 33)
print(pt2.__dict__)
print(f'x: {pt2.x} || y: {pt2.y} || z: {pt2.z} || MAX_COORD: {pt2.MAX_COORD}')



