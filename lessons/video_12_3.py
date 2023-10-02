#12. Магический метод __call__. Функторы и классы-декораторы
# dunder-методы (анг. сокр. double underscope)

# Применяется:
# 2. Реализация Декораторов
# Пример Вычисление Производной

import math
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        delta = (self.__fn(x+dx) - self.__fn(x)) / dx
        return delta

# Вариант Декоратора "в ЛОБ"
def df_sin(x):
    return math.sin(x)

# Вариант с Применением конструкции Декоратор
@Derivate
def df_sin_decorate(x):
    return math.sin(x)

# --- RUN -------------------------------------------------

res1 = df_sin(math.pi/3) # Значение в Точке pi/3

df_sin = Derivate(df_sin) # Превратили Функцию в Экзепляр Класса (1й вариант)
res2 = df_sin(math.pi/3) # Значение Производной в Точке pi/3

res3 = df_sin_decorate(math.pi/3) # (2й вариант) Значение Производной в Точке pi/3

print(res1, res2, res3)
