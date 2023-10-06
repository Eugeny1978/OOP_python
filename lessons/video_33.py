#33. Вложенные классы
# В данн примере Вложенный класс создается для того чтобы избежать конфликта данных (ordering)
# Мы можем обращаться мз Внешноего Класса ко Вложенному Классу. Наоборот делать НЕ Следует
# Логику программы следует делать такой, чтобы Вложенный Класс не был связан данными с Внешним Классном
# Те Только Внешний Класс использует Внутренний но не наоборот.
# Все что можно делать через Вложенные Классы можно делать и без них используя обычные независимые объявления

class Women:
    title = '| объект класса для поля title |'
    photo = '| объект класса для поля photo |'
    ordering = '| объект класса для поля ordering |'
    def __init__(self, user, password):
        self._user = user
        self._password = password
        access = f'{user}@{password}'
        self.meta = self.Meta(access) # если необходимо также создать и Экземляр Вложенного класса
    class Meta:
        ordering = ['id']
        #t = Women.title # Ошибка - тк Класс Women в данной точке исполнения кода ЕЩЕ не определен
        def __init__(self, access):
            self._access = access
            self._t = Women.title # Так можно НО не Следует


# --- RUN -----------------------------------

# print(Women.ordering)
# print(Women.Meta.ordering)
w1 = Women('User_123', 'pass_123')
# print(w1.ordering)
# print(w1.Meta.ordering)
print(w1.__dict__)
print(w1.meta.__dict__)
