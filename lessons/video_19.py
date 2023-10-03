#19. Магические методы __iter__ и __next__
# __iter__(self) / Получение Итератора для перебора Объекта
# __next__(self) / Переход к следующему Значению и его считывание
# range(start, stop, step) / Последовательноный Ряд

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        # self.value = start - step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        # print('__next__')
        if self.value + self.step < self.stop:
            self.value += self.step
            return round(self.value, 4)
        else:
            raise StopIteration

class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        if not isinstance(rows, int) or rows < 1:
            IndexError('Аргумент "rows" Должен быть Целым Положительным Числом')
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            StopIteration


# --- RUN -------------------------------------

fr1 = FRange(2, 12.7, 1.74)

# for i in range(7):
#     print(next(fr1)) # print(fr1.__next__())

# # iter(fr1)
# for value in fr1:
#     print(value)

fr2 = FRange2D(1, 12, 0.79, 5)

for row in fr2:
    for value in row:
        print(value, end=' || ')
    print('\n')



