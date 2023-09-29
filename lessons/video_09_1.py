#9. Свойства property. Декоратор @property
# Это более удобный Способ Работы с Приватными Атрибутами

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old
    # Для упрощения обращений к данному Атрибуту
    # old = property(get_old, set_old) # альтернативно коду ниже
    old = property()
    old = old.getter(get_old)
    old = old.setter(set_old)

person = Person('Sergey', 27)

# Если НЕ прописан в Классе: old = property(get_old, set_old)
# Тогда так оращаемся
person.set_old(35)
print(person.get_old())

# Если Прописан в Классе: old = property(get_old, set_old)
person.__dict__['old'] = '.old in exemplar' # создает Локальный атрибут с именем old
ooo = person.old
person.old = 45 # При записи имеет приоритет ОБЩИX перед Локальными атрибутами (см принт ниже)
print(person.old)
print(person.__dict__) # Проверяем действительно ли Изменилось Приватное Св-во