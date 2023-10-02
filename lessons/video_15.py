#15. Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие

# __eq__ / ==
# __ne__ / !=
# __lt__ / <
# __le__ / <=
# __gt__ / >
# --ge__ / >=
# Если в Классе нет метода __ne__, то Интерпретатор ищет метод __eq__
# и выполняет инверсию: not(c1 == c2)
# Аналогично. Если нет __gt__, то Интерпретатор ищет метод __lt__
# и выполняет ПЕРЕСТАНОВКУ операндов: Было: c1 > c2 / Стало: c2 < c1

class Clock:
    __DAY = 86400 # num sec per day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды необходимо вводить целым Числом')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый Операнд должен быть int или Clock')
        result = other if isinstance(other, int) else other.seconds
        return result

    def __eq__(self, other):
        print('Выполняется Метод (Равно): __eq__')
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        print('Выполняется Метод (Меньше): __lt__')
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        print('Выполняется Метод (Больше): __gt__')
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __ge__(self, other):
        print('Выполняется Метод (Больше ИЛИ Равно): __ge__')
        sc = self.__verify_data(other)
        return self.seconds >= sc

    def __le__(self, other):
        print('Выполняется Метод (Меньше ИЛИ Равно): __lt__')
        sc = self.__verify_data(other)
        return self.seconds <= sc

# --- RUN -------------------------------

c1 = Clock(1552)
c2 = Clock(1552)
c3 = Clock(5000)
print('Проверки на Равенство -----------------')
print(c1 == c2)
print(c1 == c3)
print(c1 == 1552)
print('Проверки на НЕ Равенство -----------------')
print(c1 != c2)
print(c1 != c3)
print(c1 != 1557)
print('Проверки на Меньше -----------------')
print(c1 < c2)
print(c1 < c3)
print(c1 < 1557)
print('Проверки на Больше -----------------')
print(c1 > c2)
print(c1 > c3)
print(c1 > 1557) # При отсутствии метода __gt__ в данн случае выдаст ошибку, тк пытается найти в int Св-во seconds
print('Проверки на Меньше ИЛИ Равно -----------------')
print(c1 <= c2)
print(c1 <= c3)
print(c1 <= 1557)
print('Проверки на Больще ИЛИ Равно -----------------')
print(c1 >= c2)
print(c1 >= c3)
print(c1 >= 1557)




