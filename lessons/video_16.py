#16. Магические методы __eq__ и __hash__

# hash - только для НЕИЗМЕНЯЕМЫХ Объектов (Например: число. строка, кортеж)
# Если Хеши Не равны - То объекты ТОЧНО не равны
# Если Хеши Равны - Не оязательно что и Объекты Равны (но в подавляющ большинстве случаев Равны)
# Если Объекты Равны То Равны и их Хеши

# print(hash('Python'))
# print(hash(555))
# print(hash((1, 5, 12)))
# # hash([12, 55 ,72]) # Не хешируем тк изменяемый объект

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        result = (self.x == other.x and self.y == other.y)
        return result

    def __hash__(self):
        print('Подменили вычисление Хэша Ссылок Класса на Хеш Аргументов (в данн. случ. координат) Класса')
        return hash((self.x, self.y))


# ---- RUN ------------------------------------------

p1 = Point(5, 12)
p2 = Point(5, 12)
# print(hash(p1), hash(p2), sep='\n')
print(hash(p1))
print(hash(p2))
print(p1 == p2)

# не смотря на то что вроде определяем 2й элемент Словаря
# На самом деле мы Переприсваиваем Значение Одному Элементу, тк мы переопределили Хэш
# и теперь для пайтона р1 и р2 - Один и тот же Ключ
dict1 = {}
dict1[p1] = 1
dict1[p2] = 4
print(dict1)