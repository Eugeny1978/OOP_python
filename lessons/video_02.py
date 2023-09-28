#2. Методы классов. Параметр self

# Методы - это действия, Поэтому в Названиях методов - Глаголы
# Методы - это те же Атрибуты, но они ведут не на Данные а на функции

class Point:
    color = 'red'
    circle = 2

    # def set_coords(self): # Передается Объект. в данн. случ. экземляр класса Point
    #     print('Вызов метода "set_coords()" ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y) # возвращаем кортежем

point_a = Point()
point_b = Point()
point_a.set_coords(8,12)
point_b.set_coords(5,25)
print(f'Координаты точки А: {point_a.__dict__} || __dict__ ')
print(f'Координаты точки B: {point_b.__dict__} || __dict__ ')
print(f'Координаты точки А: {point_a.get_coords()} || get_coords()')
print(f'Координаты точки B: {point_b.get_coords()} || get_coords()')

# self Это Аргумент - ссылка на Экземляр класса из котрого был вызван Метод
point_c = Point()
point_c.set_coords(5, 7)
# И теперь если вызвать Данный метод непосредственно из Самого Класса, то
# необходимо явно указать Экземляр, к которому мы применим метод
Point.set_coords(point_c, 77, 99)