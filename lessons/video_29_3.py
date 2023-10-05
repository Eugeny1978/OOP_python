# 29. Обработка исключений. Блоки finally и else
#  finally выполняется ДО оператора return
#  Вложенные Блоки try / except

def div_zero(a, b):
    try:
        result = a / b
    except ZeroDivisionError as error:
        print(error)

def get_values():
    try:
        print(f'Введите 2 Целых числа:')
        x, y = map(int, input().split())
        div_zero(x, y)
        # try: # Вложеный try
        #     result = x / y
        # except ZeroDivisionError as error:
        #     print(error)
        return x * 2, y * 2
    except ValueError as error:
        print(error)
        return 0, 0
    finally:
        print('finally выполняется ДО оператора return')

x, y = get_values()
print(x, y)

