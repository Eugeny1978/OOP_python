#28. Введение в обработку исключений. Блоки try / except
# Исключения (Ошибки) бывают:
# В момент исполнения.
# При компиляции (до исполнения кода).
# В данном занятии нас Интересуют Исключения в момент исполнения (во время исполнения кода)
# См. файл TypeExeptions_video_28.png - в котором показана схема Иерархии Классов Исключений
# Как видно Большая часть в классе Exeption
# При отлавливании Искючений Можно указывать как более Базовые(Общие Классы) так и Дочерние (более конкретные)

ex1 = 'Example 1'
path_to_file_1 = 'TypeExeptions_video_28.png'
path_to_file_2 = 'TypeExeptions_video_.png'

def open_file(path_to_file):
    try:
        file = open(path_to_file)
        print(f'{ex1}. Штатное Выполнение.')
    except FileNotFoundError:
        print(f'{ex1}. Невозможно открыть файл: {path_to_file}')

open_file(path_to_file_1)
open_file(path_to_file_2)

ex2 = 'Example 2'
try:
    print(f'{ex2}. Введите 2 Целых числа:')
    x, y = map(int, input().split())
    result = x/y
    print(f'{ex2}. Штатное Выполнение')
except ValueError: # Можно прописывать несколько Типов Исключений в кортеже: (ValueError, ZeroDivisionError)
    print(f'{ex2}. Ошибка Ввода')
except ZeroDivisionError:
    print(f'{ex2}. Второе чило не должно быть 0: Деление на Ноль')
except: # Обработаются Все остальные Случаи Исключений
    print(f'{ex2}. Что-то пошло не так...')

print('\nEND Programm || Штатное Завершение Программы')





