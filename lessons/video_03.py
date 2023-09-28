#3. Инициализатор __init__ и финализатор __del__

# __name_magic_method__ - "магические методы"
#
# __init__(self) - Инициализатор Объекта Класса
# __del__(self) - Финализатор Объекта Класса

class Point:
    color = 'red'
    circle = 2

    def __init__(self, ax=0, ay=0):
        print('Вызов __init__')
        # Создаем Локальные Свойства
        self.x = ax
        self.y = ay

    def __del__(self):
        # По завершению выполнения программы происходит автоматически удаление существующих  Объектов
        # в Коде это прописывать не надо
        print(f'Удаление Объекта {self}')

point_a = Point(12, 16)
point_b = Point(ay=20)
point_c = Point(56)
point_d = Point()

print(f'point A: {point_a.__dict__}')
print(f'point B: {point_b.__dict__}')
print(f'point C: {point_c.__dict__}')
print(f'point D: {point_d.__dict__}')


