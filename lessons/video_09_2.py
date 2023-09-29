#9. Свойства property. Декоратор @property
# Это более удобный Способ Работы с Приватными Атрибутами
# То же что и в video_09_1 только Используем Декораторы

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    # Для упрощения обращений к данному Атрибуту
    @property
    def old(self): # Это Геттер get_
        return self.__old
    @old.setter
    def old(self, old): # Это Сеттер set_
        self.__old = old

    @old.deleter
    def old(self): # Это Делитер del_
        del self.__old



person = Person('Sergey', 27)
person.old = 35
print(person.old)
print(person.__dict__) # Проверяем действительно ли Изменилось Приватное Св-во

# Удаляем Св-во
del person.old
print(person.__dict__)

# Возвращаем Св-во
person.old = 18
print(person.__dict__)


