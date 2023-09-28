#4. Магический метод __new__. Пример паттерна Singleton
# cls - ссылка на Теущий Экземпляр
# self - ссылка на создаваемый Экземпляр

#  С верс. 3 Python все классы наследуются с встроенного Класса Object
#
#
#
class Point:

    def __new__(cls, *args, **kwargs):
        print(f'Вызов __new__ для {cls}')
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'Вызов __init__ для {self}')
        self.x = x
        self.y = y


pt = Point(5, 15)
print(pt)