#23. Наследование. Атрибуты private и protected

# .attribute - реж. доступа (public) - Публичный Атрибут
# ._attribute - реж. доступа (protected) - Для обращения ВНУТРИ Класса и Дочерних Класссах
# .__attribute - реж. доступа (private) - Для обращения ТОЛЬКО внутри Класса

class Geom:
    name = 'Geom'
    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Класса "Geom" для: {self.__class__}')
        self.__x1 = x1 # private
        self.__y1 = y1
        self._x2 = x2 # protected
        self._y2 = y2

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        print('Инициализатор Класса "Rect"')
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

    def get_coords_protected(self):
        print('Выполняется get_coords_protected')
        return (self._x2, self._y2)

    def get_coords_private(self):
        print('Выполняется get_coords_private')
        return (self.__x1, self.__y1) # так не получится. Выдаст Ошибку
        # return super().__x1, super().__y1 # так не получится. Выдаст Ошибку
        # return Geom.__x1, Geom.__y1 # так не получится. Выдаст Ошибку

    def get_coords(self):
        print('Выполняется get_coords')
        return self.__fill # получится. Тк это Приватный Аргумент ЭТОГО Класса


# ---- RUN --------------------------------------

r1 = Rect(2, 5, 11, 22, 'Blue')
print(r1.__dict__)
# Обрати внпимание
# x1, y1, x2, y2 - имена имеют названия _Geom__ (назв Базового Класса для Rect) - статус private
# x2, y2 - имена имеют названия _ (без привязки к Классу) - тк они прописаны _ - и имеют статус protected (см. выше)
# fill - название текущ Класса _Rect__ - также статус private
# {'_Geom__x1': 2, '_Geom__y1': 5, '_x2': 11, '_y2': 22, '_Rect__fill': 'Blue'}
# private Атрибуты НЕдоступны через self.__ххх в Дочерних Классах

print(r1.get_coords())
print(r1.get_coords_protected())
print(r1.get_coords_private())

