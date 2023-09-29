#8. Паттерн "Моносостояние"
# Все Экземпляры будут иметь единый набор ЛОКАЛЬНЫХ Атрибутов с едиными значениями

# Выполнить Через Консоль - Отслеэивать Панель Справа: как изменяются значения во всех Экземплярах

# В ПАНЕЛИ / 1. Загрузить Класс
class ThreadData:
    __shared_attrs = {
        'name': 'tread_`1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


# В ПАНЕЛИ / Загружать последовательно строки кода:
tr1 = ThreadData()
tr2 = ThreadData()
tr3 = ThreadData()

tr2.id = 400
tr3.name = 'thread_55'
tr1.attr_new = 'new attribute'
tr2.rrr = 5100
del tr1.rrr # Удаляет Атрибут
