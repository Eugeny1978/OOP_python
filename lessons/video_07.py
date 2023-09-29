#7. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__
#  Атрибуты (Значения) и Методы (Функции) = Это Свойства Класса
# Атримбуты класса ОБЩИЕ для Всех его Экземпляров

#  __setattr__(self, key, value) || автоматич. вызывается при изменении свойства key класса
#  __getattribute__(self, item) || автоматич. вызывается при получении св-в Класса с именемм item
#  __getattr__(self, item) || автоматич. вызывается при получении несуществующего св-ва item Класса
#  __delattr__(self, item) || автоматич. вызывается при удалении Св-ва item (сущ. / несущ. - не важно)
class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    # Данный Метод Создаст Локальый Атрибут Не повлияв на Атрибут Класса
    def set_bount_local(self, min_coord):
        self.MIN_COORD = min_coord

    # Вот так можно поменять Значение Атрибута Класса
    @classmethod
    def set_bount(cls, min_coord):
        cls.MIN_COORD = min_coord

    def __getattribute__(self, item):
        print(f'Вызван метод: __getattribute__ для Атрибута: {item}')
        if item == 'x':
            raise ValueError('Доступ к Х запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print(f'Вызван метод: __setattr__ для Атрибута: {key}')
        if key != 'z':
            object.__setattr__(self, key, value)
            #  self.__dict__[key] = value # Альтернативно Строке выше
        else:
            raise AttributeError(f'Недопустимое Имя Атрибута: {key}')

    # Может пригодится Если НЕ хотим чтобы в таких случаях возвращалась Ошибка
    def __getattr__(self, item):
        print(f'Вызван метод: __getattr__ для Несуществующего Атрибута: {item}')
        # return False

    def __delattr__(self, item):
        print(f'Вызван метод: __delattr__ для Атрибута: {item} / Атрибут будет Удален')
        object.__delattr__(self, item)
        print(f'Удален Атрибут: {item}')


# ------------------------------------------

pt1 = Point(10, 20)
pt2 = Point(40, 15)

# coord_x = pt1.x,
# print(coord_x)
# coord_y = pt1.y
# print(coord_y)

pt1.d = 44
# pt1.z = 77
print(pt1.f)

del pt1.d
print(pt1.__dict__)
