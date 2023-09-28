# Паттерн Singleton
# Подразумеваента что может создаваться ТОЛЬКО Один Экземляр Класса
# Например База Данных

class DataBase:

# <----- Код определяющий Паттерн Singleton
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.__instance = None
# </----
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def wtite(self, data):
        print(f'Запись в БД: {data}')


db1 = DataBase('root_1', 'psw_1', 'port_1')
print(f'На данный момент создана ТОЛЬКО БД1. ID БД1: {id(db1)}')
db2 = DataBase('root_2', 'psw_2', 'port_2')
db3 = DataBase('root_3', 'psw_3', 'port_3')
print(f'ID БД1: {id(db1)}')
print(f'ID БД2: {id(db2)}')
print(f'ID БД3: {id(db3)}')
db1.connect() # print(f'Параметры БД1: {db1.__dict__}')
db2.connect() # print(f'Параметры БД2: {db2.__dict__}')
db3.connect() # print(f'Параметры БД3: {db3.__dict__}')

# Как видим это не совсем то что мы хотели.
# Да - у нас 1 Экземляр, он имеет ID первого созданного Экземпляра,
# но Параметры переопределены от последнего созданного экземляра.
# Чтобы это исправить необходимо переопределить еще один метод __call__
# Но это в следующих занятиях