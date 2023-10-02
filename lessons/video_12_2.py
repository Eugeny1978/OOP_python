#12. Магический метод __call__. Функторы и классы-декораторы
# dunder-методы (анг. сокр. double underscope)

# Применяется:
# 1. Замена Замыкания Функций (поспотреть примеры из Базового курса)
# Пример Удаление "мусорных" символов в начале и конце строк
class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    # Для того чтобы можно было вызывать Экземпляр Объекта  используя ()
    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str): # Если 0-й Элемент НЕ является Строкой
            raise TypeError('Аргумент должен быть Строкой')

        return args[0].strip(self.__chars)
# --- RUN -------------------------------------------------

c1 = StripChars('!?:;., ')
c2 = StripChars(' !')
c3 = StripChars(' ')
frase = '  !!!!? Hello, world.!?!!   '
res1 = c1(frase)
res2 = c2(frase)
res3 = c3(frase)
print(res1, res2, res3, sep='\n')
