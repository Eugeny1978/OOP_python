#25. Множественное наследование
# class classA(ClassA1, ClassA2, ... ClassAN)
# Применяется не часто.
# Пример: миксины - Примеси - mixins
# Порядок наследования - Method Resolution Order (MRO)
# В данном случае порядок: NoteBook -- Goods -- MixinLog -- object (см. NotoBook.__mro__)
# Структуру Вспомогательных Классов следует продумывать так, чтобы они имели только один параметр self
# Особенно еслит таких Классов несколько.
# Иначе в процессе при поддержке и расширении кода будут возникать трудности,
# Там один там два параметра здесь так месттами поставили а предполгалось по другому порядок

class Goods:
    def __init__(self, name, weight, price):
        print('init Goods')
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')

class MixinLog:
    ID = 0
    def __init__(self):
        self.ID +=1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id} || Товар был продан в 00:00 часов')

    def print_info(self):
        print('print_info Из Класса MixinLog')

class NoteBook(Goods, MixinLog):
    def print_info(self): # Переопредел метод для постоянног риспользования
        MixinLog.print_info(self)


# --- RUN ---------------------------------------

n1 = NoteBook('Acer', 1.5, 50000)
n1.print_info()
n1.save_sell_log()
print(NoteBook.__mro__)
# Чтобы исполнить метод print_info из вспомогательного класса при наличии такого же метода в Основном классе
#1 вариант (если в частном случае)
MixinLog.print_info(n1)
#2 вариант (если в постоянно) - Переопределить этот метод в Дочернем Классе ( в данн случае в NoteBook)

