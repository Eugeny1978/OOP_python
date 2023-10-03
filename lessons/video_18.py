#18. Магические методы __getitem__, __setitem__ и __delitem__

# __getitem__(self, item) / Получение Значения по ключу item
# __setitem__(self, key, value) / Запись Значения value по ключу key
# __delitem__(self, key) / Удаление Элемента по ключу key

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def verify_index(self, index):

        if not isinstance(index, int):
            raise TypeError('Индекс должен быть Целым Числом')

        range_index = len(self.marks)
        max_index = range_index - 1
        min_index = - range_index
        if index > max_index or index < min_index:
            raise IndexError(f'Индекс ВНЕ Диапазона || + Индексы Макс: {max_index} || - Индексы Мин: {min_index}')


    def __getitem__(self, item):
        print('__getitem__')
        self.verify_index(item)
        return self.marks[item]

    def __setitem__(self, key, value):
        print('__setitem__')
        self.verify_index(key)
        self.marks[key] = value

    def __delitem__(self, key):
        print('__delitem__')
        self.verify_index(key)
        del self.marks[key]

# --- RUN -----------------------------------------------

s1 = Student('Sergey', [5, 5, 4, 3, 3, 4, 5, 4, 5])
print(s1[5])
# print(s1[15])
s1[6] = 1
print(s1.marks)
del s1[6]
print(s1.marks)
