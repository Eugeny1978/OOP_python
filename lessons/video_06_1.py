#6. Режимы доступа public, private, protected. Сеттеры и геттеры
# Механизм ИНКАПСУЛЯЦИИ

# atribute / Публичный
# _atribute / Защищенный Обращаться можно. Служит для предостережения разработчикам что в дальнейшем может и быть убранным из класса и обращаться не стоит
# __atribute / Приватный Извне обратиться нельзя (Но Создать с таким именем вне класса можно!) - см. ниже комментарии

# Однако при желании ВСЕ ЖЕ можно Обращаться и к Приватным - см код НИЖЕ.
# Чтобы Более Надежно Защитить необходимо Воспользоваться Модулем "accessify" / pip install accessify
# Применение см. в файле video_06_2

from accessify import private, protected

class Point:
    def __init__(self, x=0, y=0):

        if not self.__check_value(x):
            x = 0
            print(f'Вводимые Координата X должна быть Числом | Присвоено Х = {x}')
        if not self.__check_value(y):
            y = 0
            print(f'Вводимые Координата Y должна быть Числом | Присвоено Y = {y}')

        self.x_public = x
        self.y_public = y
        self._x_protected = x
        self._y_protected = y
        self.__x_private = x
        self.__y_private = y

    # СЕТТЕР (Интерфейсный метод)
    def set_coords(self, x=0, y=0):
        # if type(x) in (int, float) and type(y) in (int, float):
        if self.__check_value(x) and self.__check_value(y):
            self.__x_private = x
            self.__y_private = y
        else:
            # raise ValueError('Вводимые Координаты должны быть Числами')
            print('Вводимые Координаты должны быть Числами')

    # ГЕТТЕР (Интерфейсный метод)
    def get_coords(self):
        return (self.__x_private, self.__y_private)

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float)



pt = Point(10, 12)
# pt.x_public = 100
# pt.y_public = 'public'
# pt._x_protected = 200
# pt._y_protected = 'protected'
# pt.__x_private = 300
# pt.__y_private = 'private'

print(pt.x_public, pt.y_public)
print(pt._x_protected, pt._y_protected)
# print(pt.__x_private, pt.__y_private) # Выдаст Ошибку

pt.set_coords('50', 70)
print(pt.get_coords())
pt.set_coords(50, 70)
print(pt.get_coords())

print(dir(pt)) # Посмотрю Свойства Объекта
# Пример как обратиться к приватному свойству
# Делать ТАК крайне НЕ рекомдуется
print(pt._Point__x_private)