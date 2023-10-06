#32. Менеджеры контекстов. Оператор with - это класс, в котором реализованы методы:
# __enter__() - срабатывает в момент создания Объекта менеджера контекста
# --exit__() - срабатывает в момент завершения работы менеджера контекста или возникновения исключения

# Общая схема синаксиса
# with <менеджер контекста> as <Переменная>:
#   Список инструкций языка Python

# Если не предполагаем работать с самим Объектом менеджера контекста, то можно записать так:
# with <менеджер контекста>:
#   Список инструкций языка Python


class DefendorVector:
    def __init__(self, vector):
        self.__v = vector

    def __enter__(self):
        self.__temp = self.__v[:] # создаю копию вектора
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False # Исключения обрабатываются ВНУТРИ менеджера контекста


v1 = [2, 4, 7]
v2 = [3, 5]
# v2 = [10, 10, 10]

try:
    with DefendorVector(v1) as dv:
        for index, value  in enumerate(dv):
            dv[index] += v2[index]
except:
    print('Что-то пошло не так...')

print(f'Vector V1: {v1}')

