#13. Магические методы __str__, __repr__, __len__, __abs__

# __str__ / Для отображения инф-ции об Объекта Класса для Пользователей (функц.: print,str)
# __repr__ / Для отображения инф-ции об Объекта Класса для Разработчиков (в реж. Отладки)
# __len__ / Позволяет применять Функцию len() к Экземплярам Класса
# __abs__ / Позволяет применять Функцию abs() к Экземплярам Класса

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'

# ---- RUN ------------------------------------------------

# Выполнить в реж консоли.
cat1 = Cat('Абдурахманчик')
print(cat1)
str(cat1)
cat1