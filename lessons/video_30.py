#30. Распространение исключений (propagation exceptions)

# Исключения можно обрабатывать на любом ровне Стека Исключений (стек исключений см. в сообщенииях об ошибке)
# Как правило Обработка исключений осущ. в функциях "верхних уровнях"
# Тогда как в "нижних уровнях" прописывается остальная логика.

def func1():
    try:
        return 5/0
    except Exception as error:
        print(f'|| func1: {error} ||')

def func2():
    try:
        return func1()
    except Exception as error:
        print(f'|| func2: {error} ||')

print('Я Вам пишу, чего же боле?')
print('Что я могу нще сказать?')
print('Теперь, я знаю, в Вашей воле')
try:
    func2()
except Exception as error:
    print(f'|| Body Programm: {error} ||' )
print('Меня презреньем наказать.')
print('Но Вы, к несчастной моей доле')
print('Хоть каплю жалости храня')
print('Вы не оставите меня')
