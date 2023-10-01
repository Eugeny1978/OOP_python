#11. Дескрипторы (data descriptor и non-data descriptor)

# Пример Задачи.
# Реализация С Дескрипторами

class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координаты должны быть заданы ЦЕЛЫМИ Числами')
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name) # Аналог: return self.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value) # Аналог: instance.__dict__[self.name] = value

class Point3D:

    x = Integer() # Дескриптор Данных
    y = Integer() # Дескриптор Данных
    z = Integer() # Дескриптор Данных
    xr = ReadIntX() # Дескриптор НЕ Данных тк Данные НЕ Создаем - см. ниже
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        # self.xr - НЕ Создаем!





# ---- RUN ----------------------------------------------------------------------

print('Пример ТОЛЬКО с Дескрипторами Данных ---------------- ')
point = Point3D(10, 27, 6)
print(point.__dict__)
point.x = 33
point.y = 17
point.z = -25
print(point.__dict__)
print('Пример Дескрипторы Данных и Дескрипторы НЕ Данных ---- ')
point2 = Point3D(12, 17, 33)
point2.__dict__['xr'] = 999
print(f'point2.xr = {point2.__dict__["xr"]}')
print(f'point2.xr = {point2.xr}. Происходит из-за того что в Дескрипторе ReadIntX указано name = _х')
print(point2.__dict__)