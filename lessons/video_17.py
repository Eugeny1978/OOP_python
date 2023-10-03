#17. Магический метод __bool__ определения правдивости объектов

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('Вызывается Метод: __len__')
        return int(math.sqrt(self.x**2 + self.y**2))

    def __bool__(self):
        print('Вызывается Метод: __bool__')
        return self.x == self.y


# --- RUN ----------------------------------

p1 = Point(3, 4)
p2 = Point(5, 5)
print(len(p1))
print(bool(p1))
print(bool(p2))

# На практике чаще всего встречаются конструкции типа:
if p2:
    print('Выполняется блок кода если Истина')
else:
    print('Выполняется блок кода если Ложь')


