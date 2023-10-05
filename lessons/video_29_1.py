# 29. Обработка исключений. Блоки finally и else

try:
    print(f'Введите 2 Целых числа:')
    x, y = map(int, input().split())
    result = x/y
except ValueError as error: # В error попадает соответствующий Объект со стандарт. сообщением прописаным разработчиками
    print(error.__class__)
    print(error)
except ZeroDivisionError as error:
    print(error)
except Exception as error: # Обработаются Все остальные Случаи Исключений
    print(error)
else:
    print('Вы ввели корректные Числа. Исключений не возникло')
finally:
    print('Блок finally выполняется ВСЕГДА')