#14 Магические методы __add__, __sub__, __mul__, __truediv__

# __add__       / (a+b) Прибавить
# __sub__       / (a-b) Отнять
# __mul__       / (a*b) Умножить
# __truediv__   / (a/b) Разделить
# __floordiv__  / (a//b) Целое от Деления
# __mod__       / (a%b) Остаток от Деления
# __r(func)__   / Действие когда Класс находится спава (например: 100 + Class(400))
# __i(func)__   / += -= *= /= //= %=


class Clock:
    __DAY = 86400 # num sec per day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть Целым Числом')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        result = f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'
        # result = f'{h:02d}:{m:02d}:{s:02d}' # аналог предыдущ строки чб не прописывать функцию
        return result

    @classmethod
    def __get_formatted(cls, x):
        result = str(x).rjust(2, '0')
        return result

    # ПРИМЕР __add__
    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый Операнд должен быть int или Clock')
        cs = other
        if isinstance(other, Clock):
            cs = other.seconds
        result = Clock(self.seconds + cs)
        return result

    # Если int Слева а Класс Clock справа (Например: 1200 + Clock(2300))
    def __radd__(self, other):
        print('Отрабатывает Метод: __radd__')
        return self + other

    # Если Например: c6 += 1500
    def __iadd__(self, other):
        print('Отрабатыывает Метод: __iadd__')
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый Операнд должен быть int или Clock')
        cs = other
        if isinstance(other, Clock):
            cs = other.seconds
        self.seconds += cs
        return self

    # ПРИМЕР __sub__
    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый Операнд должен быть int или Clock')
        cs = other
        if isinstance(other, Clock):
            cs = other.seconds
        result = Clock(self.seconds - cs)
        return result

    # Если int Слева а Класс Clock справа (Например: 1200 - Clock(2300))
    def __rsub__(self, other):
        print('Отрабатывает Метод: __rsub__')
        return self - other

    # Если Например: c6 += 1500
    def __isub__(self, other):
        print('Отрабатыывает Метод: __isub__')
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый Операнд должен быть int или Clock')
        cs = other
        if isinstance(other, Clock):
            cs = other.seconds
        self.seconds -= cs
        return self
# --- RUN -----------------------------------------------------

c1 = Clock(1000)
# c1.seconds = c1.seconds + 100
# c1 = c1 + 100
c2 = Clock(2000)
c3 = Clock(4000)
c4 = c1 + c2 + c3
print(c1.get_time())
print(c2.get_time())
print(c3.get_time())
print(c4.get_time())
c5 = 1200 + c4
print(c5.get_time())
c5 += 2000
print(c5.get_time())
print('\n')
c6 = 25000 - c5
print(f'c6 = {c6.get_time()}')
c7 = c5 - 2500
print(f'c7 = {c7.get_time()}')
c8 =  c6 - c1 - c2 - c3
print(f'c8 = {c8.get_time()}')
c8 -= 600
print(f'c8 = {c8.get_time()}')

# А ТЕПЕРЬ ИЗМЕНИ КОД ЧТОБЫ НЕ БЫЛО ФУНКЦИОНАЛЬНОЙ ПОВТОРЯЕМОСТИ ?
# Используй Дескрипторы (см. video_11_2)