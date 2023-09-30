#10. Пример использования объектов property
from string import ascii_letters
class Person:

    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weigth):

        self.verivy_fio(fio)
        # Проверки ЗАШИТЫ в Функциях-СЕТТЕРАХ
        # self.verify_old(old)
        # self.verify_passport(ps)
        # self.verify_weigth(weigth)

        self.__fio = fio.split()
        # Значения устанавливаю, Используя Функции-Сеттеры
        self.old = old       # self.__old
        self.passport = ps   # self.__passport
        self.weigth = weigth # self.__weigth

    @classmethod
    def verivy_fio(cls, fio):
        fio_words = fio.split()
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        if type(fio) != str:
            raise TypeError('ФИО - должен задаваться типом данных "Строка"')
        if len(fio_words) != 3:
            raise TypeError('Неверный Формат Записи. Пример: Сидоров Иван Петрович')

        for word in fio_words:
            invalidsimbols = word.strip(letters)
            if len(invalidsimbols) !=0:
                print(f'Есть Недопустимые Символы в ФИО: {word}')
                raise TypeError('В ФИО можно ипользовать ТОЛЬКО Eng, Rus Буквы и Дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            print(f'Неверная Запись Возраста: {old}, Тип: {type(old)}')
            raise TypeError('Вес Должен быть записан в виде Целого Числа, Больше 14 и Меньше 120')

    @classmethod
    def verify_passport(cls, ps):
        if type(ps) != str:
            print(f'Паспорт: {ps}. Тип Данных: {type(ps)}')
            raise TypeError('Даные Паспорта необходимо ввести в Цифрами виде Строки')

        ps_list = ps.split()
        if len(ps_list) !=2:
            raise TypeError('Данные Должны Содержать Серию и Номер через Пробел')
        for s in ps_list:
            if not s.isdigit():
                raise TypeError('В Данных Паспорта содержатся Символы НЕ Цифры')
        if len(ps_list[0]) !=4:
            raise  TypeError('Серия Паспорта должна состоять из 4х Цифр')
        if len(ps_list[1]) !=6:
            raise  TypeError('Номер Паспорта должен состоять из 6ти Цифр')

    @classmethod
    def verify_weigth(cls, weigth):
        if type(weigth) not in (int, float) or weigth < 40:
            print(f'Неверная Запись Веса: {weigth}, Тип: {type(weigth)}')
            raise TypeError('Вес Должен быть записан в виде Числа и Более 40')

    @property
    # Getter
    def fio(self):
        return self.__fio

    @property #Getter
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property #Getter
    def passport(self):
        return self.__passport
    @passport.setter
    def passport(self, ps):
        self.verify_passport(ps)
        self.__passport = ps

    @property  # Getter
    def weigth(self):
        return self.__weigth
    @weigth.setter
    def weigth(self, weigth):
        self.verify_weigth(weigth)
        self.__weigth = weigth


# RUN ---------------------------------------------------------------------------------------

person_1 = Person('Барханов Абдулла Михайлович', 35, '0306 270923', 68.4)
print(person_1.__dict__)

print(person_1.fio)

person_1.old = 37
print(person_1.old)

person_1.passport = '3255 607890'
print(person_1.passport)

person_1.weigth = 79
print(person_1.weigth)

print(person_1.__dict__)