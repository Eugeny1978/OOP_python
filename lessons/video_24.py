#24. Полиморфизм и абстрактные методы
# Полиморфизм - возможность работы с совершенно разными объектами (языка Python) единым образом
# Абстракты - это методы, которые обязательно нужно переопределять в дочерних классах
# и которые не имеют своей собственной реализации

class Geom:
    def get_perimetr(self):
        # return 0 # Заглушка на случай если такого метода нет в конкретном дочернем Классе
        raise NotImplementedError('В Дочернем Классе необходимо переопределить метод get_perimetr(self)')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_perimetr(self): # Для полиморфизма называем ОДИНАКОВО # def get_rect_perimetr(self):
        return 2*(self.w + self.h)

class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_perimetr(self): # Для полиморфизма называем ОДИНАКОВО # def get_square_perimetr(self):
        return 4*self.a

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_perimetr(self): # Для полиморфизма называем ОДИНАКОВО # def get_triangle_perimetr(self):
        return self.a + self.b + self.c

class Circle(Geom):
    def __init__(self, r):
        self.r = r


# --- RUN -------------------------------

r1 = Rectangle(3, 6)
r2 = Rectangle(5, 8)
r3 = Rectangle(7, 9)
s1 = Square(6)
s2 = Square(12)
s3 = Square(4)
t1 = Triangle(3, 7, 9)
t2 = Triangle(5, 7, 12)
t3 = Triangle(2, 4, 5)
c1 = Circle(4)
c2 = Circle(8)
c3 = Circle(12)

figures = [r1, r2, r3, s1, s2, s3, t1, t2, t3, c1, c2, c3]
# for f in figures:
#     if isinstance(f, Rectangle):
#         print(f'Периметр Прямоугольника {f}: {f.get_rect_perimetr()}')
#     if isinstance(f, Square):
#         print(f'Периметр Квадрата {f}: {f.get_square_perimetr()}')
#     if isinstance(f, Triangle):
#         print(f'Периметр Треугольника {f}: {f.get_triangle_perimetr()}')

for f in figures:
    print(f'Периметр {f}: {f.get_perimetr()}')
