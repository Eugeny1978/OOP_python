#20. Наследование в объектно-ориентированном программировании

class Geom: # Базовый или Родительский Класс
    name = 'Geom' # см стрелочка вниз на полях IDE

    def set_coords(self, x1, y1, x2, y2):
        print(f'__set_coord__ || {self}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def draw(self):
        print('Рисование Геометрической фигуры')

class Line(Geom): # Подкласс или Дочерний Класс
    name = 'Line' # переопределяю Аргумент (см на поляях IDE стрелочка вверх)
    def draw(self):
        print('Рисование Линии')

class Rect(Geom): # Подкласс или Дочерний Класс
    def draw(self):
        print('Рисование Прямоугольника')

# --- RUN ----------------------------

g1 = Geom()
l1 = Line()
r1 = Rect()
g1.draw()
l1.draw()
r1.draw()
print(g1.name)
print(l1.name)
print(r1.name)
g1.set_coords(5, 7, 12, 43)
l1.set_coords(2, 4, 11, 19)
r1.set_coords(1, 5, 13, 22)
print(l1.__dict__)
print(r1.__dict__)