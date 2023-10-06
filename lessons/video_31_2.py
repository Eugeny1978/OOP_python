#31. Инструкция raise и пользовательские исключения
# raise генерирует Исключения

class ExeptionPrint(Exception):
    """Общий Класс исключений Принтера"""

class ExeptionPrintSendData(ExeptionPrint):
    """Класс Исключений при Отправки данных на Принтер"""
    def __init__(self, *args):
        self.message = args[0] if args else None
    def __str__(self):
        return f'Ошибка: {self.message}'


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            # raise Exception('Принтер НЕ отвечает')
            raise ExeptionPrintSendData('Принтер НЕ отвечает')

    def send_to_print(self, data):
        return False

# --- RUN ---------------------------

pd1 = PrintData()
# pd1.print('строка для печати')
try:
    pd1.print('строка для печати')
except ExeptionPrintSendData as error:
    print(error)
except ExeptionPrint:
    print('Общая ошибка печати')