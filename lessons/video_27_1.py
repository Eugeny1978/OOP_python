#27. Как работает __slots__ с property и при наследовании

class Point2D:
    __slots__ = ('x', 'y', '__length')
    MAX_COORD = 250
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x**2 + y**2) ** 0.5
    @property
    def length(self): # Это Атрибут класса поэтому отрабатывает без ошибок
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

# --- RUN --------------------------------------

pt1 = Point2D(10, 20)
print(pt1.length)
pt1.length = 30
print(pt1.length)